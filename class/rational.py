class Rational:
    def __init__(self,numer,denom = 1):
        def gcd(a,b):
            a = abs(a)
            b = abs(b)
            while max(a,b)%min(a,b) != 0:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            return min(a,b) 
        if denom == 0:
            raise ZeroDivisionError('chutiye 0 denominator aa raha hai!!!')
        elif numer == 0:
            self.numerator = 0
            self.denomenator = 1
        else:
            g = gcd(numer,denom)
            self.numerator = (numer//g)*(denom//abs(denom))
            self.denomenator = abs(denom)//g

    def printit(self):
            return [self.numerator,self.denomenator]

    @classmethod
    def add(cls,r1,r2):
        n1 = r1.numerator
        n2 = r2.numerator
        d1 = r1.denomenator
        d2 = r2.denomenator
        return cls.printit(cls((n1*d2+n2*d1),d1*d2))
        
    @classmethod
    def sub(cls,r1,r2):
        n1 = r1.numerator
        n2 = r2.numerator
        d1 = r1.denomenator
        d2 = r2.denomenator
        return cls.printit(cls((n1*d2-n2*d1),d1*d2))

    @classmethod
    def mul(cls,r1,r2):
        n1 = r1.numerator
        n2 = r2.numerator
        d1 = r1.denomenator
        d2 = r2.denomenator
        return cls.printit(cls(n1*n2,d1*d2))

    @classmethod
    def div(cls,r1,r2):
        n1 = r1.numerator
        n2 = r2.numerator
        d1 = r1.denomenator
        d2 = r2.denomenator
        return cls.printit(cls(n1*d2,n2*d1))      

r1 = Rational(0,8)
r2 = Rational(4,9)
print(Rational.div(r2,r1))