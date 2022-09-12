import os
os.system('cls')

#All of the text letters

a = ['  A   '
,' A A  '
,'A   A '
,'AAAAA '
,'A   A '
,'A   A '
,'A   A ']

b = ['BBBB '
,'B   B'
,'B   B'
,'BBBB '
,'B   B'
,'B   B'
,'BBBB ']

c = [' CCC  '
,'C   C '
,'C     '
,'C     '
,'C     '
,'C   C '
,' CCC  ']

d = ["DDDD "
,"D   D"
,"D   D"
,"D   D"
,"D   D"
,"D   D"
,"DDDD "]

e = ["EEEEE"
,"E    "
,"E    "
,"EEE  "
,"E    "
,"E    "
,"EEEEE"]

f = ["FFFFF"
,"F    "
,"F    "
,"FFF  "
,"F    "
,"F    "
,"F    "]

g = [" GGG "
,"G   G"
,"G    "
,"GGGGG"
,"G   G"
,"G   G"
," GGG "]

h = ["H   H"
,"H   H"
,"H   H"
,"HHHHH"
,"H   H"
,"H   H"
,"H   H"]

i = ["IIIII"
,"  I  "
,"  I  "
,"  I  "
,"  I  "
,"  I  "
,"IIIII"]

j = ["JJJJJ"
,"  J  "
,"  J  "
,"  J  "
,"J J  "
,"J J  "
," JJ  "]

k = ["K   K"
,"K  K "
,"K K  "
,"KK   "
,"K K  "
,"K  K "
,"K   K"]

l = ["L    "
,"L    "
,"L    "
,"L    "
,"L    "
,"L    "
,"LLLLL"]

m = ["M   M"
,"MM MM"
,"MM MM"
,"M M M"
,"M   M"
,"M   M"
,"M   M"]

n = ['N   N '
,'NN  N '
,'N N N '
,'N  NN '
,'N   N '
,'N   N '
,'N   N ']

o = [' OOO  '
,'O   O '
,'O   O '
,'O   O '
,'O   O '
,'O   O '
,' OOO  ']

p = ["PPPP "
,"P   P"
,"P   P"
,"PPPP "
,"P    "
,"P    "
,"P    "]

q = [" QQQ "
,"Q   Q"
,"Q   Q"
,"Q   Q"
,"Q   Q"
,"Q  Q "
," QQ Q"]

r = ["RRRR "
,"R   R"
,"R   R"
,"RRRR "
,"R R  "
,"R  R "
,"R   R"]

s = [" SSS  "
,"S   S "
,"S     "   
," SSS  "
,"    S "
,"S   S "
," SSS  "]

t = ["TTTTT "
,"  T   "
,"  T   "
,"  T   "
,"  T   "
,"  T   "
,"  T   "]

u = ["U   U"
,"U   U"
,"U   U"
,"U   U"
,"U   U"
,"U   U"
," UUU "]

v = ['V   V '
,'V   V '
,'V   V '
,'V   V '
,'V   V '
,' V V  '
,'  V   ']

w = ["W   W"
,"W   W"
,"W   W"
,"W W W"
,"WW WW"
,"WW WW"
,"W   W"]

x = ["X   X"
,"X   X"
," X X "
,"  X  "
," X X "
,"X   X"
,"X   X"]

y = ["Y   Y"
," Y Y "
,"  Y  "
,"  Y  "
,"  Y  "
,"  Y  "
,"  Y  "]

z = ["ZZZZZ"
,"    Z"
,"   Z "
,"  Z  "
," Z   "
,"Z    "
,"ZZZZZ"]

inp = input("What do you want to be turned into block letters? \n")

inpLength = len(inp)

inpL = inp.replace("", "|").split("|")

inpList = ["","","","","","","",""]

list1 = 0

#Make sure the code runs at smaller messages

if inpLength <= 7:
    while list1 < inpLength + 1:
        inpList[list1] = inpL[list1]
        list1 += 1
else:
    inpList = inp.replace("", "|").split("|")

counter = 0
counter2 = 0
message = ""

os.system('cls')

#Making the block letters

while counter2 < 7:
    if inpList[counter + 1] == "a":
        message = message + a[counter2]
    elif inpList[counter + 1] == "b":
        message = message + b[counter2]
    elif inpList[counter + 1] == "c":
        message = message + c[counter2]
    elif inpList[counter + 1] == "d":
        message = message + d[counter2]
    elif inpList[counter + 1] == "e":
        message = message + e[counter2]
    elif inpList[counter + 1] == "f":
        message = message + f[counter2]
    elif inpList[counter + 1] == "g":
        message = message + g[counter2]
    elif inpList[counter + 1] == "h":
        message = message + h[counter2]
    elif inpList[counter + 1] == "i":
        message = message + i[counter2]
    elif inpList[counter + 1] == "j":
        message = message + j[counter2]
    elif inpList[counter + 1] == "k":
        message = message + k[counter2]
    elif inpList[counter + 1] == "l":
        message = message + l[counter2]
    elif inpList[counter + 1] == "m":
        message = message + m[counter2]
    elif inpList[counter + 1] == "n":
        message = message + n[counter2]
    elif inpList[counter + 1] == "o":
        message = message + o[counter2]
    elif inpList[counter + 1] == "p":
        message = message + p[counter2]
    elif inpList[counter + 1] == "q":
        message = message + q[counter2]
    elif inpList[counter + 1] == "r":
        message = message + r[counter2]
    elif inpList[counter + 1] == "s":
        message = message + s[counter2]
    elif inpList[counter + 1] == "t":
        message = message + t[counter2]
    elif inpList[counter + 1] == "u":
        message = message + u[counter2]
    elif inpList[counter + 1] == "v":
        message = message + v[counter2]
    elif inpList[counter + 1] == "w":
        message = message + w[counter2]
    elif inpList[counter + 1] == "x":
        message = message + x[counter2]
    elif inpList[counter + 1] == "y":
        message = message + y[counter2]
    elif inpList[counter + 1] == "z":
        message = message + z[counter2]
    elif inpList[counter + 1] == " ":
        message = message + "  "
    counter += 1
    message = message + " "
    if counter == inpLength:
        counter = 0
        counter2 += 1
        print(message)
        message = ""