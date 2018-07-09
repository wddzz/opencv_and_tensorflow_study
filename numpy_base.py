import numpy as np


data1 = np.array([1,2,3,4,5])
print(data1)
data2 = np.array([[1,2,3],
                  [4,5,6]])
print(data2)
# 维度
print(data1.shape,data2.shape)
# zero ones
print(np.zeros([2,3]),np.ones([2,2]))
# 改查
data2[1,0] = 5
print(data2)
print(data2[1,1])
# 基本运算
data3 = np.ones([2,3])
print(data3+1)
print(data3-1)
print(data3*3)
print(data3/2)
# 两个矩阵的运算
print(data2+data3)
print(data2-data3)
print(data2*data3)
print(data2/data3)


