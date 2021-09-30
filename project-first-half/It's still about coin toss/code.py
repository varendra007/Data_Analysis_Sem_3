import pandas as pd

import xlrd

# reading excel file (I converted csv file to excel file because of non-readalble format in .csv type)

df = pd.read_excel('data_200010055.xlsx', index_col=0, header=None)


exp_noise = 0
exp_coin_toss = 0
prob_head = 0
exp_total = 0;


i = 0 

# calculating expectation value of noise
while i< 1000 : 
    exp_noise += df.index[i]
    i+=1

exp_noise = exp_noise/1000


# calculating expectation value of coin toss
while i<11000:
    exp_total += df.index[i]
    i+=1

exp_total = exp_total/10000

exp_coin_toss = exp_total - exp_noise


# calculating bias of coin toss i.e. probabilty of head (prob_head)
prob_head = exp_coin_toss/5

print(exp_noise,prob_head)

