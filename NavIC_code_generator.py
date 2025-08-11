import numpy as np

from decor import SpreadingCodes, AdaptiveKGreedyCodeOptimizer


def navic_prn_gen(g2_init):
    G1 = [1]*10
    G2 = [int(b) for b in g2_init]
    prn = []
    for i in range(1023):
        prn.append(G1[9] ^ G2[9])  # Output taken from register[-1], BEFORE shifting!
        g1_fb = G1[2] ^ G1[9]
        g2_fb = G2[1] ^ G2[2] ^ G2[5] ^ G2[7] ^ G2[8] ^ G2[9]
        # Now, do the shift
        G1 = [g1_fb] + G1[:-1]
        G2 = [g2_fb] + G2[:-1]
    return prn

def save_to_files(g2_initials,filename):
    navic_code = []
    with open(filename,'w') as file:
        for prn, g2init in g2_initials.items():
            bits = navic_prn_gen(g2init)
            print(f"PRN {prn}: first 10 bits: {''.join((map(str, bits[:10])))} octal: {oct(int(''.join((map(str, bits[:10]))), 2))}")
            code = [1 - 2 * bit for bit in bits]
            navic_code.append(code)
            file.write('[')
            for ele in code:
                file.write(str(ele))
                file.write(',')
            file.write(']')
            file.write('\n')
    print(f"Saved all PRN sequences to {filename}")
    return navic_code

def optimizer_function(num_codes,code_length,code_arr,output_file):

    x = SpreadingCodes(num_codes, code_length, code_arr, p=6)
    print("objective_before_optimization: ", x.objective())

    optimizer = AdaptiveKGreedyCodeOptimizer()
    optimizer.optimize(x, 1000000)

    print("objective_after_optimization: ", x.objective())

    with open(output_file, 'w') as optimize:
        for val in x.value:
            optimize.write('[')
            for ele in val:
                optimize.write(str(ele))
                optimize.write(',')
            optimize.write(']')
            optimize.write('\n')


if __name__ == "__main__":
    g2_initials_L5 = {
        1: '1110010111',
        2: '0110010000',
        3: '0010110001',
        4: '0100111010',
        5: '0000110111',
        6: '1101011000',
        7: '0010100000',
        8: '0000110010',
        9: '0001100100',
        10: '0010011011',
        11: '0011001000',
        12: '0011111011',
        13: '0100101101',
        14: '0101011110'
    }
    navic_L5_codes = save_to_files(g2_initials_L5,"NavIc_L5_code.txt")
    #print(navic_codes)

    np_navicL5 = np.array(navic_L5_codes)
    # print(np_navic)

    g2_initials_S = {
        1: '1111011100',
        2: '1011111010',
        3: '1000110001',
        4: '1101010100',
        5: '1000100101',
        6: '0011010010',
        7: '0111000100',
        8: '0110010010',
        9: '0111000011',
        10:'0111110101',
        11:'1000100111',
        12:'1001011011',
        13:'1010001010',
        14:'1011000010'
    }

    navic_S_codes = save_to_files(g2_initials_S, "NavIc_S_code.txt")

    np_navicS = np.array(navic_S_codes)

    optimizer_function(len(np_navicS),1023,np_navicS,"NavIc_S_optimized.txt")


"""
L5 band:
objective_before_optimization:  0.0016148415664429866
Objective: 0.001 Best: 0.001 improvement: 67.036%: 100%|██████████| 1000000/1000000 [7:54:52<00:00, 35.10it/s]
objective_after_optimization:  0.0005323159121113449

S band:
objective_before_optimization:  0.0016177299521994866
Objective: 0.001 Best: 0.001 improvement: 67.270%: 100%|██████████| 1000000/1000000 [4:12:12<00:00, 66.08it/s]
objective_after_optimization:  0.000529480576221153
"""