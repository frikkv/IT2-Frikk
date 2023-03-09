import matplotlib.pyplot as plt 

#x = [0,1,2,3,4,5]
#y = [0,2,4,6,8,10]

#plt.plot(x,y) # opretter et plott
#plt.show() # viser plottet 

# plott funksjonen f(x) = 3*x + 2, med x fra 0 til 5 


def f(x):
    3*x+2

x = []
y = []
for i in range(6):
    y.append(f(i))
    x.append(i)


plt.scatter(x,y)
plt.show()

