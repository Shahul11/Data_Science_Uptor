# import matplotlib.pyplot as plt
#
# """Sample Scatter graph plotting thru pyplot - bivaraite"""
#
# x = [1,2,3,4,5,6]
# y = [8,2,5,4,5,6]
#
# # plt.scatter(x,y, c=x, cmap='rainbow')
# plt.scatter(x,y, c=x, cmap='magma')
# plt.colorbar() #shows number to color mapping in the side of graph
# plt.show()



"""Below code is using seaborn library to generate  graphs for visualization"""

# import matplotlib.pyplot as plt
# import  seaborn as sns
# import pandas as pd

"""Sample Scatter graph plotting thru pyplot - bivaraite"""

# x = [1,2,3,4,5,6]
# y = [8,2,5,4,5,6]
#
# df = pd.DataFrame({"key1":x,"key2":y})
#
# """Even  when we generate scatter plot through seaborn we visualize it thru matplotlib
# seaborn process plots faster than matplotlib
# when we pass the df to scatterplot directly to scatterplot, it plots as x and y seperately
#
# Python allows 2 kinds of arguments - positional  and keyword
# read more on user define functions in python to understand this
# """
#
# sns.scatterplot(x='key1', y='key2',data=df)
#
# plt.show()




"""Used when you have one category  and another is numerical used bar plot
bar chart aggregates the value of duplicate values
"""


# import matplotlib.pyplot as plt
# team =['csk','rcb','mi','csk','mi','kkr']
# trophy = [1,1,4,11,1,2]
#
# plt.bar(team, trophy)
# plt.show()
#



"""Pie chart"""

# import matplotlib.pyplot as plt
# import  numpy as np
#
# team =['csk','rcb','mi','csk','mi','kkr']
# # trophy = [1,1,4,11,1,2]
#
# trophy = np.array([1,1,4,11,1,2])
#
#
# """Plotting graph for category vs count"""
# plt.pie(trophy, labels=team, autopct='%1.1f%%')
# plt.show()
#
# # labels maps teh value to each entity of the numerics
# #autopct  show the break up with % lable on pie chart





"""Finding Outlier"""

import matplotlib.pyplot as plt
import  numpy as np

age = [3,5,67,700,8000,-600]
plt.boxplot(age)
plt.show()



