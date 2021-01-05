import pylab
import math

k=40
theta=[]
r=[]
for i in range (2,k):
    for m in range (2,int(math.sqrt(i))):
        if (i%m!=0):
            theta.append(i)
    

#theta=range(10000)

#r=range(10000)

print(r)
print(theta)
#pylab.polar(theta,r,ls='',marker='o')
#pylab.show()


#pylab.plot(range(10), linestyle='', marker='o', color='b')
#pylab.show()
