import numpy as np 

data = np.array([112.32, 139.527, 128.009, 146.805,157.172])


data_Sum = data + 2
data_Sub = data - 2
data_Mul = data * 2
data_Div_float = data / 2
data_Div_int = data // 2
data_Mod = data % 2
data_Pow = data ** 2



print(data_Sum, " ", data_Sub, " ", data_Mul, " ", data_Div_float, " ", data_Div_int, " ", data_Mod, " ", data_Pow)
