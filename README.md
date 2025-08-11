# decor
Spreading code design: optimizing binary spreading codes, or pseudorandom noise
(PRN) codes to have low auto-correlation and cross-correlation. Contains
efficient implementations of bit-flip descent methods that iteratively
*decorrelate* a set of codes.

Accompanies the paper:

A. Yang, T. Mina, S. Boyd, and G. Gao. Large-Scale GNSS Spreading Code Optimization. 
Proceedings of the 37th International Technical Meeting of the Satellite Division 
of the Institute of Navigation (ION GNSS+ 2024)

Paper link: https://stanford.edu/~boyd/papers/code_design.html

## Overview
`decor` is a Python package for designing and optimizing binary spreading codes,
also known as pseudorandom noise (PRN) codes. These codes are optimized to have
low auto-correlation and cross-correlation properties, making them suitable for
applications in communication systems, such as CDMA and GPS.

## Features
- Generate binary spreading codes
- Optimize codes for low auto-correlation and cross-correlation
- Gold and Weil Codes

## Usage

Example usage:
```
import decor

# Generate 63 random binary spreading codes, each length 1023
# objective function with parameter p=6
codes = decor.random_code_family(63, 1023, p=6)

# Generate Gold codes
gold_codes = decor.gold_code_family(63, 1023, p=6)

# evaluate correlation values
codes.correlation()

# evaluate objective function
codes.objective()

# optimize codes
optimizer = AdaptiveKGreedyCodeOptimizer()
optimizer.optimize(codes, n_iter=1000)
```

The `scripts` directory contains an `example.py` file. To run the example, use:
```
python3 -m scripts.example
```
# File Description
- `NavIc_code_generator.py` and `GPS_code_generator.py` are the main file to generate PRN codes for GPS L1 C/A and for NavIC L5 and S band.
- decor is used in both this files to check whether codes are getting optimized or not.
- `acr_ccr_function.py` is to check the acr and ccr value before optimization and after optimization.
- All other `.txt` files contains the output of NavIC and GPS codes.
