import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""================== For Normal Data=============="""


# normal_data = np.random.normal(50,10,100)
#
# """
# 1000 indicates total number of data
# 10 indicates standard deviation
# 50 mean/average
# """
# print(normal_data)
# print(type(normal_data)) #helps know the type of the data created
# print(normal_data.ndim) #1 Dimension means series of data
#
# df = pd.DataFrame(normal_data, columns=["normal_data"])
# print(df)
#
# """Plotting this in graph"""
# df["normal_data"].plot(kind="hist", bins=30, color="yellow", edgecolor="black") #histogram
# plt.xlabel("value")
# plt.ylabel("Frequency")
# plt.show()

"""================== For Uniform Data=============="""

uniform_data = np.random.uniform(50,10,100)

print(uniform_data)
print(type(uniform_data))
print(uniform_data.ndim)

df = pd.DataFrame(uniform_data, columns=["UniformData"])
print(df)
df["UniformData"].plot(kind="hist", bins=30, color="yellow", edgecolor="black") #histogram
plt.xlabel("value")
plt.ylabel("Frequency")
plt.show()

