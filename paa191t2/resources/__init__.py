# UBNLP: Unconstrained Binary NonLinear Program
# Input
# Line 1: n m z
# n: number of logical variables
# m: number of terms (coefficient and variable product)
# z: value of the best known solution
# Line 2: i1, i2, ..., ik
# Best known solution is x_i1 = x_i2 = ... = x_ik = 1 and 0 otherwise
# Lines 3 to m+1: id coeff card i_1 ... i_card
# id: number of the term (id=1,...,m)
# coeff: coefficient 
# card: number of variables in the product
# i_1 ... i_card: list of variables in the product
