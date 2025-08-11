# ✅ Compute balance of a sequence
import numpy as np

def calculate_balance(sequence):
    d = np.sum(sequence)
    return len(sequence) - 2 * d

# ✅ Function to compute autocorrelation using sequence differences
def compute_difference(sequence):
    N = len(sequence)
    results = []
    for k in range(N):
        shifted_sequence = np.roll(sequence, k)
        agreements = np.sum(sequence == shifted_sequence)
        disagreements = N - agreements
        result = agreements - disagreements
        results.append(result)
    return results

def compute_acr(binary_sequence):
    unique_vals = compute_difference(binary_sequence)
    unique_vals = [abs(val) for val in unique_vals]
    acr_max = max(set(unique_vals[1:])) if len(unique_vals) > 1 else 0

    return acr_max


from itertools import combinations

import numpy as np

def compute_cross_correlation(seq1, seq2):
    seq1 = np.array(seq1)
    seq2 = np.array(seq2)
    N = len(seq1)
    results = []
    for k in range(N):
        shifted_seq2 = np.roll(seq2, k)
        agreements = np.sum(seq1 == shifted_seq2)
        disagreements = N - agreements
        result = agreements - disagreements
        results.append(int(result))
    return results


def compute_ccr(list_of_binary_sequence):
    ccr_results = {}
    for seq1, seq2 in combinations(list_of_binary_sequence, 2):
        seq1_str = ''.join(str(x) for x in seq1)
        seq2_str = ''.join(str(x) for x in seq2)
        cc = compute_cross_correlation(seq1, seq2)
        ccr_max = max(abs(val) for val in cc)
        ccr_results[(seq1_str, seq2_str)] = ccr_max
    max_pair = max(ccr_results, key=ccr_results.get)
    # print(ccr_results)
    return max_pair,ccr_results[max_pair],ccr_results


def to_binary(seq):
    return [0 if x == -1 else 1 for x in seq]



if __name__ == "__main__":
    gold_codes = [[ 1,  1, -1,  1,  1,  1, -1, -1,  1,  1,  1, -1,  1, -1,  1,  1, -1, -1,
  -1,  1,  1,  1, -1, -1, -1,  1, -1,  1,  1,  1,  1,],
 [-1, -1, -1,  1, -1, -1, -1, -1,  1, -1,  1, -1,  1,  1, -1,  1, -1, -1,
  -1, -1, -1,  1,  1,  1,  1,  1,  1, -1,  1, -1, -1,],
 [ 1,  1,  1, -1, -1, -1,  1,  1, -1,  1,  1, -1, -1, -1, -1,  1,  1,  1,
   1, -1, -1, -1, -1,  1,  1, -1,  1,  1, -1, -1,  1,],
 [-1, -1,  1, -1, -1,  1, -1, -1, -1, -1,  1,  1, -1, -1,  1, -1, -1,  1,
  -1,  1,  1,  1,  1,  1,  1, -1,  1, -1, -1, -1, -1,],
 [ 1,  1,  1,  1, -1, -1, -1,  1, -1,  1, -1, -1,  1,  1,  1, -1,  1, -1,
  -1,  1,  1, -1,  1,  1, -1, -1, -1, -1,  1, -1, -1,],
 [-1,  1, -1,  1,  1,  1, -1,  1,  1,  1, -1,  1,  1, -1,  1, -1,  1, -1,
   1, -1, -1,  1,  1,  1,  1, -1,  1,  1, -1, -1,  1,],
 [-1,  1, -1, -1,  1, -1, -1,  1, -1,  1, -1, -1,  1, -1,  1,  1,  1, -1,
   1,  1, -1,  1, -1,  1, -1, -1,  1,  1, -1, -1, -1,],
 [-1,  1,  1, -1, -1, -1,  1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1, -1,
   1,  1, -1,  1,  1,  1,  1,  1,  1, -1,  1,  1,  1,],
 [-1,  1, -1,  1, -1, -1, -1,  1,  1, -1,  1, -1,  1, -1, -1, -1, -1,  1,
  -1, -1, -1, -1,  1, -1,  1, -1, -1,  1, -1,  1,  1,],
 [ 1, -1, -1, -1,  1, -1, -1,  1,  1,  1, -1, -1,  1, -1,  1,  1,  1,  1,
   1, -1, -1, -1, -1,  1, -1, -1,  1, -1,  1, -1,  1,],
 [ 1, -1,  1,  1,  1, -1, -1,  1,  1, -1, -1, -1,  1, -1,  1,  1, -1,  1,
   1, -1, -1, -1,  1,  1, -1, -1, -1,  1,  1, -1,  1,],
 [-1,  1,  1, -1,  1,  1,  1,  1,  1, -1,  1, -1,  1,  1, -1,  1, -1,  1,
  -1, -1,  1, -1,  1, -1, -1,  1,  1,  1, -1, -1,  1,],
 [-1,  1, -1, -1, -1, -1, -1,  1,  1,  1,  1, -1, -1, -1,  1,  1, -1, -1,
   1, -1, -1, -1,  1, -1, -1, -1, -1, -1,  1,  1,  1,],
 [ 1, -1, -1, -1,  1, -1, -1,  1,  1,  1, -1,  1,  1, -1,  1,  1, -1,  1,
   1, -1,  1, -1, -1,  1,  1,  1,  1, -1, -1,  1,  1,],
 [ 1,  1,  1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1, -1,  1,  1, -1, -1,
  -1,  1,  1,  1,  1,  1, -1, -1,  1, -1,  1,  1,  1,],
 [-1,  1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1,
   1, -1,  1, -1,  1, -1, -1, -1,  1, -1,  1,  1, -1,],
 [ 1, -1,  1, -1,  1, -1, -1, -1, -1, -1, -1,  1, -1,  1,  1, -1, -1,  1,
  -1, -1,  1, -1,  1,  1,  1, -1, -1,  1, -1, -1,  1,],
 [ 1, -1,  1, -1,  1, -1, -1,  1, -1,  1, -1,  1,  1,  1,  1, -1,  1, -1,
  -1,  1,  1, -1, -1, -1,  1,  1, -1,  1, -1, -1, -1,],
 [-1, -1, -1, -1,  1,  1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1, -1, -1,
   1,  1, -1, -1,  1, -1, -1,  1, -1, -1, -1,  1,  1,],
 [-1, -1,  1, -1, -1,  1,  1, -1, -1,  1, -1,  1, -1,  1, -1,  1, -1,  1,
  -1, -1, -1,  1,  1,  1, -1,  1, -1,  1,  1, -1,  1,],
 [-1, -1, -1,  1, -1, -1, -1,  1, -1, -1,  1, -1,  1,  1,  1, -1, -1, -1,
  -1,  1,  1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1,],
 [ 1, -1,  1,  1, -1,  1,  1, -1, -1,  1,  1, -1,  1,  1,  1,  1, -1, -1,
  -1, -1, -1, -1, -1, -1,  1, -1,  1, -1,  1, -1, -1,],
 [ 1, -1, -1,  1, -1, -1,  1,  1, -1, -1, -1, -1, -1,  1, -1, -1, -1,  1,
   1,  1, -1,  1, -1,  1, -1,  1,  1, -1, -1,  1, -1,],
 [ 1, -1, -1,  1, -1,  1,  1,  1,  1,  1, -1, -1,  1,  1,  1,  1,  1, -1,
   1, -1, -1, -1,  1,  1, -1, -1, -1,  1,  1,  1,  1,],
 [ 1, -1, -1, -1,  1,  1, -1, -1,  1,  1,  1,  1,  1,  1, -1,  1,  1,  1,
   1, -1,  1, -1, -1,  1, -1, -1,  1, -1, -1, -1, -1,],
 [ 1, -1,  1, -1,  1,  1,  1, -1, -1, -1,  1,  1, -1, -1, -1, -1,  1, -1,
   1,  1,  1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1,],
 [ 1,  1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1, -1,  1,  1,  1,  1,  1,
  -1, -1,  1, -1, -1, -1,  1,  1, -1, -1,  1,  1, -1,],
 [-1,  1, -1, -1, -1,  1, -1, -1, -1, -1, -1,  1,  1, -1,  1,  1, -1,  1,
   1, -1,  1, -1,  1,  1,  1,  1,  1,  1,  1, -1,  1,],
 [-1, -1,  1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1, -1,  1, -1,  1,
  -1, -1, -1,  1, -1, -1, -1, -1,  1,  1,  1,  1, -1,],
 [ 1, -1, -1,  1,  1,  1,  1, -1, -1, -1, -1,  1, -1, -1,  1,  1,  1,  1,
  -1, -1,  1,  1, -1,  1,  1,  1, -1, -1, -1, -1, -1,],
 [-1, -1,  1,  1,  1, -1, -1, -1,  1, -1,  1,  1, -1, -1, -1,  1,  1,  1,
   1, -1, -1,  1, -1,  1, -1,  1, -1,  1, -1,  1, -1,],
 [ 1,  1, -1,  1,  1,  1, -1, -1, -1,  1, -1,  1, -1, -1,  1, -1,  1,  1,
   1,  1, -1, -1,  1,  1, -1, -1,  1, -1,  1,  1,  1,]]
    optimized_codes =  []

    # with open("random_code.txt",'r') as file:
    #     for line in file:
    #         line = line.strip().strip('[]').rstrip(',')
    #         # Skip empty lines
    #         if not line:
    #             continue
    #         # Convert to list of ints
    #         arr = [int(x) for x in line.split(',') if x.strip()]
    #         gold_codes.append(arr)
    #
    # with open("NavIc_S_optimized.txt",'r') as file:
    #     for line in file:
    #         line = line.strip().strip('[]').rstrip(',')
    #         # Skip empty lines
    #         if not line:
    #             continue
    #         # Convert to list of ints
    #         arr = [int(x) for x in line.split(',') if x.strip()]
    #         optimized_codes.append(arr)



    print("auto correlation")
    temp = []
    for item in gold_codes:
        acr = compute_acr(item)
        print(acr)
        temp.append(acr)
    # print(max(temp))

    ccr = compute_ccr(gold_codes)
    print("cross correlation")
    print(ccr[0],ccr[1],ccr[2])

    # print("for optimized code")
    # print("auto correlation")
    # temp2 = []
    # for item in optimized_codes:
    #     acr = compute_acr(item)
    #     print(acr)
    #     temp2.append(acr)
    # print("maximum : ",max(temp2))
    #
    # ccr = compute_ccr(optimized_codes)
    # print("cross correlation")
    # print(ccr[0], ccr[1])

