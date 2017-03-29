import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
 #label可以使用内嵌Latex引擎，color可以用0到1范围内三个元素的元组表示(1.0,0.0,0.0)也表示红色，linwidth:指定曲线的宽度，可以不是整数，也可以缩写为1w.
plt.plot(x, z, "b--",label = "$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
'''
xlim()、ylim()分别表示x,y轴的显示范围
'''
plt.title("PyPlot First Example")
plt.legend()#显示图示，图中每条曲线的标签所在的矩形区域,loc参数可调整位置。
plt.savefig("c:\\figure1.png")
