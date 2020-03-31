import math
import matplotlib.pyplot as plt
x = []
y = []
c0=1
c1=1
a=0.01
e=0.00001
f = open("data1.txt")
for line in f:
    temp = line.split(" ")
##    print(temp)
    x.append(float(temp[0]))
    y.append(float(temp[1]))
def h(c0,c1,x):
    return c0+c1*x


def J(c0,c1):   
    s = 1/(2*len(x))
    sum = 0
    for i in range(len(x)):
        sum = sum + (h(c0,c1,x[i]) - y[i])**2
        
        
    j = s*sum
    return j

def Jc0(c0,c1):
    sum = 0
    for i in range(len(x)):
        sum =sum + h(c0,c1,x[i]) - y[i]
    m = (1/len(x))*sum
    return m
def Jc1(c0,c1):
    sum = 0
    for i in range(len(x)):
        sum = sum + (h(c0,c1,x[i]) - y[i])*x[i]
    m = (1/len(x))*sum
    return m
raznost = 10000
Jarr = []
while raznost > e:
    Jarr.append(J(c0,c1))
    mark=J(c0,c1)

    temp0 = c0 - a * Jc0(c0,c1)
    temp1 = c1 - a * Jc1(c0,c1)
    c0=temp0
    c1=temp1
    mark2=J(c0,c1)
    
    raznost = math.fabs(mark - mark2)
    


y1=0
arrX = []
arrY = []

for i in range(len(x)):
    plt.scatter(x[i],y[i])
    

for x1 in range(5,25):
    y1 = c1*x1+c0
    arrX.append(x1)
    arrY.append(y1)
plt.plot(arrX,arrY)
plt.show()

xx=0

for d in range(len(Jarr)-1):
    
    plt.scatter(xx,Jarr[d],s=1,color = '#539caf')
    xx=xx+1
    
plt.show() 



       
   
