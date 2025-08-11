import numpy as np

from acr_ccr_function import compute_acr
from decor import SpreadingCodes, AdaptiveKGreedyCodeOptimizer


def generate_ca_code(prn: int) -> list:
    if not (1 <= prn <= 63):
        raise ValueError("PRN must be in the range 1–63")

    if prn > 36:
        g2_initials = {
            38: '1111000000',
            39: '1000011010',
            40: '0011001111',
            41: '1001011001',
            42: '1001010111',
            43: '1100001000',
            44: '1100011010',
            45: '0110001011',
            46: '1010110001',
            47: '0010111011',
            48: '1010111101',
            49: '1000011011',
            50: '1110101101',
            51: '0111001111',
            52: '1011100111',
            53: '0100000001',
            54: '1011000001',
            55: '0110110111',
            56: '1111111000',
            57: '1101011101',
            58: '0110100010',
            59: '1110100100',
            60: '0110001010',
            61: '0111101100',
            62: '1101101101',
            63: '1010011111'
        }

        g2_init = g2_initials[prn]
        G2 = [int(b) for b in g2_init]
        G1 = [1]*10

        prn = []
        for i in range(1023):
            prn.append(G1[9] ^ G2[9])  # Output taken from register[-1], BEFORE shifting!
            g1_fb = G1[2] ^ G1[9]
            g2_fb = G2[1] ^ G2[2] ^ G2[5] ^ G2[7] ^ G2[8] ^ G2[9]
            # Now, do the shift
            G1 = [g1_fb] + G1[:-1]
            G2 = [g2_fb] + G2[:-1]
        return prn


    # G2 tap pairs: (check ICD-GPS-200 Table 3-II)
    g2_taps = [
        (2, 6), (3, 7), (4, 8), (5, 9), (1, 9), (2, 10), (1, 8), (2, 9),
        (3, 10), (2, 3), (3, 4), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10),
        (1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9), (1, 3), (4, 6),
        (5, 7), (6, 8), (7, 9), (8, 10), (1, 6), (2, 7), (3, 8), (4, 9),
        (5, 10), (4, 10), (1, 7), (2, 8)
    ]

    tap1, tap2 = g2_taps[prn - 1]
    tap1 -= 1  # adjust to 0-indexed
    tap2 -= 1

    # Initialize shift registers
    g1 = [1] * 10
    g2 = [1] * 10

    ca_code = []

    for _ in range(1023):
        g1_out = g1[-1]
        g2_out = g2[tap1] ^ g2[tap2]
        ca_code.append(g1_out ^ g2_out)

        # Feedback and shift for G1: feedback from bits 3 and 10
        g1_feedback = g1[2] ^ g1[9]
        g1 = [g1_feedback] + g1[:9]

        # Feedback and shift for G2: feedback from bits 2,3,6,8,9,10
        g2_feedback = g2[1] ^ g2[2] ^ g2[5] ^ g2[7] ^ g2[8] ^ g2[9]
        g2 = [g2_feedback] + g2[:9]

    return ca_code


def save_all_prns_to_file(n, filename="ca_codes.txt"):
    gps_code = []
    with open(filename, "w") as f:
        for prn in range(1, n + 1):
            if prn == 37:
                continue
            code = generate_ca_code(prn)
            print(f"PRN {prn}: first 10 bits: {''.join((map(str, code[:10])))} octal: {oct(int(''.join((map(str, code[:10]))),2))}")
            code = [1 - 2 * bit for bit in code]
            gps_code.append(code)
            f.write('[')
            for ele in code:
                f.write(str(ele))
                f.write(',')
            f.write(']')
            f.write('\n')
    print(f"Saved all PRN sequences to {filename}")
    return gps_code


# Run the export
if __name__ == "__main__":
    gpsCode = save_all_prns_to_file(63)
    # print(gpsCode)

    np_gps = np.array(gpsCode)
    # print(np_gps)

    x = SpreadingCodes(len(np_gps), 1023,np_gps, p=6)
    print("objective_before_optimization: ",x.objective())

    optimizer = AdaptiveKGreedyCodeOptimizer()
    optimizer.optimize(x,1000000)

    print("objective_after_optimization: ", x.objective())

    with open("gps_ca_optimized.txt", 'w') as optimize:
        for val in x.value:
            optimize.write('[')
            for ele in val:
                optimize.write(str(ele))
                optimize.write(',')
            optimize.write(']')
            optimize.write('\n')

"""
objective_before_optimization:  0.029849514252163555
Objective: 0.016 Best: 0.016 improvement: 45.729%: 100%|██████████| 1000000/1000000 [16:48:16<00:00, 16.53it/s]
objective_after_optimization:  0.01619973753046759
"""
