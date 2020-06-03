
def monthlyMortgage(a, b, c):
    """Returns the monthly payment amount for a mortgage.
        Takes the form(a,b,c) where a is principal
        b is interest (APR) and c is number of years"""
    P = a
    r = b/100/12
    n = c*12

    A = (P*r*(1+r)**(n))/(((1+r)**n)-1)

    print (A)

def testmM():

    a = 310000
    b = 3.4
    c = 25

    monthlyMortgage(a,b,c)

def 
