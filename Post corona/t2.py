
import numpy as np

# Question 1
    
# Addition

# for the sake of simplicity in all asserts and invariants d(a[0...k]) represents decimal expansion of all a[0....k] ie = a[k] + 10*a[k-1] +.......+ 10^k*a[0]                                   
# and represents decimal expansion of all elements in a if no limit mentioned.
    
def add_array(a1,a2,n):
        # assert : array a1 is established; array a2 is established; size of a1 = size of a2 = n
        add = []
        carry = 0
        i = n-1
        # INV : d(add) + 10^(n-i+1)*carry = d(a1[i+1...n-1]) + d(a2[i+1...n-1]); 0 <= i <= n-1; (d(a) is merely a nomenclature defined in line 7,8)
        while (i >=0):
                add = [(a1[i] + a2[i]+carry)%10] + add
                carry = (a1[i] + a2[i]+carry)//10
                i = i - 1
        add = [carry] + add
        # assert : array add such that d(add) = d(a1[0....n-1]) + d(a2[0....n-2]); (d(a) is merely a nomenclature defined in line 7,8)
        return add
# n = 5
# a1 = np.random.randint(0,10,n)
# print(a1)
# a2 = np.random.randint(0,10,n)
# print(a2)

# print(add_array(a1,a2,n))
def filter(a):
        #assert : array a is established having entries only 1, 2 or 3

        i = 0 
        while (i < len(a)):
                j = len(a) - 1
                while (j > i):
                        if (a[j] == a[i]):
                                a[j],a[i+1] = a[i+1],a[j]
                                i = i+1
                        else:
                                j = j-1
                i = i+1
        return a
# a = [1,3,1,1,2,2,3,1,2,1,3,3,2]
# print(filter(a))

def ques3(n):
        # assert : number n is established
        def is_prime(k):
                # number k is established
                i = 2
                # INV : (k%i != 0) 2 <= i <= sqrt(k)
                while (i < k*k):
                        if (k%i == 0):
                                return False
                        i = i+1
                # (True => if k is prime); (False is k is not prime)
                return True
        def remove_factor(k):
                # number k is established
                a = k
                # INV : k = (2^x)*a; (0 <= x <= log2(k))
                while (a%2 == 0):
                        a = a//2
                # INV :a%2 != 0;  k = (2^x)*(3^y); (0 <= x <= log2(k)); (0 <= y <= log3(k))
                while (a%3 == 0):
                        a = a//3
                # INV : a%2 != 0; a%3 != 0; k = (2^x)*(3^y)*(5^z)*a ; (0 <= x <= log2(k)); (0 <= y <= log3(k)); (0 <= z <= log5(k))
                while (a%5 == 0):
                        a = a//5
                # a such that a%2 != 0; a%3 != 0; a%5 != 0; k = (2^x)*(3^y)*(5^z)*a ; (0 <= x <= log2(k)); (0 <= y <= log3(k)); (0 <= z <= log5(k))
                return a
        a = []
        i = 2
        # INV : all a[0....l-1]%k != 0 where k is any prime != 2 or 3 or 5; 0 <= l <= n
        while (len(a) < n):
                if (is_prime(remove_factor(i)) == True):
                        a = a + [i]
                i = i+1
        return a

        # array a such that all a[0...n-1]%k != 0 where k is any prime != 2 or 3 or 5

# print(ques3(10))

def mult_array(a1,a2,n):
        # assert : array a1 is established; array a2 is established; size of a1 = size of a2 = n
        c = []
        i = n-1
        #INV : d(c) = d(a1[0...n-1])*d(a2[i+1...n-1]); -1 <= i <= n-1; (d(a) is merely a nomenclature defined in line 7,8)
        while (i >= 0):
                j = n-1
                carry = 0
                inter = []
                # INV : d(inter) + 10^(n-j+1)*carry  = d(a2[i]) * d(a1[j+1...n-1]); (d(a) is merely a nomenclature defined in line 7,8)
                while (j >= 0):
                        inter = [(a1[j]*a2[i]+carry)%10] + inter
                        carry = (a1[j]*a2[i] + carry)//10
                        j = j-1
                inter = [carry] + inter
                inter = inter + [0 for i in range(n-i-1)]
                c = [0 for i in range(len(inter)-len(c))] + c
                c = add_array(c,inter,len(c))
                i = i - 1
        # assert: array c such that d(c) = d(a1[0....n-1]) * d(a2[0...n-1]); (d(a) is merely a nomenclature defined in line 7,8)
        return c

n = 5
a1 = np.random.randint(0,10,n)
print(a1)
a2 = np.random.randint(0,10,n)
print(a2)
print(mult_array(a1,a2,n))

