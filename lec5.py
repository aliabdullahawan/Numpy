import numpy as np

data1 = np.array([1, 2, 3])
print(data1)
data2 = np.array([4, 5, 6])
print(data2)

data_elementWise_Sum = data1 + data2
print(data_elementWise_Sum)
data_elementWise_Sub = data1 - data2
print(data_elementWise_Sub)
data_elementWise_Mul = data1 * data2
print(data_elementWise_Mul)
data_elementWise_Div_float = data1 / data2
print(data_elementWise_Div_float)
data_elementWise_Div_int = data1 // data2
print(data_elementWise_Div_int)
data_elementWise_Pow = data1 ** data2
print(data_elementWise_Pow)
data_elementWise_Mod = data1 % data2
print(data_elementWise_Mod)

score = np.array([54, 76, 80, 94, 34])
print(score)

print(score == 100)
print(score <= 87)
print(score > 35)
print(score != 76)

score[score < 60] = 0
print(score)






