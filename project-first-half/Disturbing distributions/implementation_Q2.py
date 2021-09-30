import pandas as pd
import numpy as np

df = pd.read_excel('Proj_Comp2_data_200010055.xlsx', index_col=0, header=None)

exp_Z = 0
var_Z = 0
i=0 

data = []

while (i < 50000) :
	data.append(df.index[i])
	i+=1

exp_Z = sum(data) / 50000

var_Z  = np.var(data)

M= exp_Z 
V = var_Z


k_exp = M * M / (V - 3)
k_R = (M * M *(4 - np.pi)) / (4 * (V- 3))

k_N = (M * M * (np.pi - 2)) / (2 * (V - 3))

# print((k_exp),(k_N),(k_R))
print("Mean of Z, i.e mean_Z = ", M)
print("Variance of Z, i.e. var(Z) = ", V)
print('For Exponential destribution k = ', k_exp)
print('For Rayleigh destribution k = ', k_R)
print('For Half-normal destribution k = ', k_N)

exp_lambda = (10 * M) / (V - 3)

print('Since k value for exponential destribution is closed to 3 which belongs to given set of possible values for k. Hence, given distribution describes exponential destribution with k = ', round(k_exp), 'and lambda = ', round(exp_lambda))
