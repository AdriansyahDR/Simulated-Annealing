from random import *
from math import *

def rumus(x1,x2) :
    f = ((2*pow(x1,2))+(pow(x2,4))/3)*pow(x1,2) - x1*x2+(4*pow(x2,2)*pow(x2,2))
    return f
def P(E,T) :
    return exp(-E/T)

x1 = uniform(-1,1)
x2 = uniform(-1,1)
Tawal = 200000
Takhir = 0
CR = 0.2


CS = rumus(x1,x2)
BSF = CS
while Tawal != Takhir :
    x1 = uniform(-1,1)
    x2 = uniform(-1,1)
    NS = rumus(x1, x2)
    E = NS - CS
    if E < 0 :
        CS = NS
        BSF = NS
    else :
        R = random()
        if P(E, Tawal) > R :
            CS = NS
            BSF = NS
    Tawal = Tawal * CR
print("x1 = ",x1," x2 = ",x2)
print(BSF)