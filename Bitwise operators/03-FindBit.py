# Find the ith bit of a number

"""
1 0 1 1 0 1 1 0  --> find 5th bit

do & operation with the mask --> 0 0 0 1 0 0 0 0

mask --> 1 << 4 => 1 0 0 0 0

so, n & ( 1 << (n - 1))

"""
