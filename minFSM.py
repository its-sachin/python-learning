a1 = {
    "a" : ["a","b","c", "", 0],
    "b" : ["d","b","", "", 0],
    "c" : ["p","","c", "", 0],
    "d" : ["d","e","f", "", 0],
    "e" : ["g","e","", "", 0],
    "f" : ["m","","f", "", 0],
    "g" : ["g","h","i", "", 0],
    "h" : ["j","h","", "", 0],
    "i" : ["a","","i", "", 1],
    "j" : ["j","k","l", "", 0],
    "k" : ["a","k","", "", 1],
    "l" : ["a","","l", "", 1],
    "m" : ["m","n","o", "", 0],
    "n" : ["a","n","", "", 1],
    "o" : ["a","","o", "", 1],
    "p" : ["p","r","s", "", 0],
    "r" : ["t","r","", "", 0],
    "s" : ["a","","s", "", 1],
    "t" : ["t","u","v", "", 0],
    "u" : ["a","u","", "", 1],
    "v" : ["a","","v", "", 1]

}

array = {
    "a" : ["a","b","c", "", 0],
    "b" : ["k","b","", "h", 0],
    "c" : ["f","","c", "m", 0],
    "d" : ["d","e","j", "", 1],
    "e" : ["a","e","", "m", 0],
    "f" : ["f","l","j", "", 0],
    "g" : ["d","g","", "h", 0],
    "h" : ["","g","j", "h", 1],
    "j" : ["f","","j", "h", 0],
    "k" : ["k","l","c", "", 1],
    "l" : ["a","l","", "h", 0],
    "m" : ["","g","c", "m", 1]
}
hai = []
nah = []

def reverse(str):
        out = ""
        for i in str:
            out = i + out

        return out

def isEqual(a1, a2):
    if (a1 == "" or a2 == "") :
        return True
    else:
        return a1==a2

def isInNah(a1,a2):
    str = a1+a2
    for i in nah:
        if (str == i or reverse(str) == i):
            return True
    return False


def isComp(a1,a2):
    if (a1==a2):
        return True
    else:
        if (array[a1][4] != array[a2][4]):
            nah.append(a1+a2)
            return False
        else:
            for i in range(4):
                if (isEqual(array[a1][i],array[a2][i]) == False and (array[a1][i]!=a1 or array[a2][i]!=a2)):
                    if (isInNah(array[a1][i],array[a2][i])== True):
                        return False
                    elif (isComp(array[a1][i],array[a2][i]) == False):
                        nah.append(a1+a2)
                        return False 
            return True

def main():
    for i in array:
        for j in array:
            if (i != j and isComp(i,j) == True):
                hai.append(i+j)


def deCode(array):
    out = []
    for i in array:
        a = i[0]
        b = i[1]
        done = False
        for j in out:
            for k in j:
                if (k == a or k == b):
                    j = j + i
                    done = True
        if (done == False):
            out.append(i)
    return out

main()
print(deCode(hai))
# print(nah)