# import matplotlib.pyplot as plt
#
# """Sample Scatter graph plotting thru pyplot - bivaraite"""
#
# x = [1,2,3,4,5,6]
# y = [8,2,5,4,5,6]
#
# plt.scatter(x,y, color='red')
# plt.show()



import matplotlib.pyplot as plt

"""Sample Scatter graph plotting thru pyplot - bivaraite"""

x = [1,2,3,4,5,6]
y = [8,2,5,4,5,6]

# plt.scatter(x,y, c=x, cmap='rainbow')
plt.scatter(x,y, c=x, cmap='magma')
plt.colorbar() #shows number to color mapping in the side of graph
plt.show()


