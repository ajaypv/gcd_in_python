#  decleaing a  funcation gcde
import gc
from tkinter import N


def gcde():
    # taking a input from command prompt
    m = int(input('enter a m value'))
    n = int(input('enter a n value'))
    if m<n:
        (m,n)= (n,m)
    while n !=0:
        r = m%n
        m=n 
        n=r
    return m
print(gcde())

def gcdcc():
    m = int(input('enter a m value'))
    n = int(input('enter a n value'))
    t = min(m,n)
    while t > 0:
        if m%t == 0 and n%t ==0:
            return t
        t = t-1
print(gcdcc())