#!/usr/bin/python3
 


import matplotlib.pyplot as plt
import numpy as np
print(__name__)
#x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
#plt.plot(x, np.sin(x))       # Plot the sine of each x point
#plt.show()                   # Display the plot

def fun():
    print("Hello, World!")

    list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
    tinylist = [123, 'runoob']
    
    print (list)            # 输出完整列表
    print (list[0])         # 输出列表第一个元素
    print (list[1:3])       # 从第二个开始输出到第三个元素
    print (list[2:])        # 输出从第三个元素开始的所有元素
    print (tinylist * 2)    # 输出两次列表
    print (list + tinylist) # 连接列表