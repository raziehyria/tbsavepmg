import os
import os
from PIL import Image


#pip install matplotlib
import matplotlib.pyplot as plt
s1 = []
s2 = []
s3 = []
s4 = []
once = False
with open(os.path.join('map.pgm'), 'rb') as pgmf:
    #print(pgmf)
    #for i in range(0,100):
    #    print(pgmf.readline())
    im = list(zip(range(1,10000),plt.imread(pgmf)))
for i in range(0,len(im)):
    im[i] = list(im[i])
    im[i][1] = list(im[i][1])
for i in im:
    if once:
        s1.append(i)
    elif not all(x == i[1][0] for x in i[1]):
        once = True
        s1.append(i)

#for i in s1:
#    print(i)

s1.reverse()
once = False
for i in s1:
    if once:
        s2.append(i)
    elif not all(x == i[1][0] for x in i[1]):
        once = True
        s2.append(i)
s2.reverse()
#for i in s2:
#    print(i)

once = False
s3 = s2
#print(type(s3))
#print(len(s2[0][1]))
#print(s2[0][1][0])
#print([x[1][0] for x in s3])
while not once:
    if all(x[1][0] == s2[0][1][0] for x in s3):
        for i in range(0,len(s3)):
            del s3[i][1][0]
    else:
        once = True

#for i in s3:
#    print(i)

#print(len(s1[0][1]))
#print(len(s3[0][1]))
    
once = False
s4 = s3
while not once:
    if all(x[1][-1] == s3[0][1][-1] for x in s4):
        for i in range(0,len(s4)):
            del s4[i][1][-1]
    else:
        once = True
#for i in s4:
#    print(i)
#print(len(s1[0][1]))
#print(len(s3[0][1]))
l = len(s4[0][1])
w = len(s4)
print(len(s4[0][1]))
print(len(s4))
s = ""
for i in range(0,len(s4)):
    for j in range(0,len(s4[0][1])):
        s += chr(s4[i][1][j])
#print(s)

with open(os.path.join('map.pgm'), 'r') as pgmf:
    header = []
    for i in range(0,4):
        if i != 2:
            header.append(pgmf.readline())
        else:
            pgmf.readline()
            header.append(str(l) + " " + str(w) + "\n")
        print(i)
header.append(s)

filename = "Croppedmap.pgm"
with open(os.path.join(filename), 'w') as pgmf:
    pgmf.writelines(header)
    
for file in os.listdir():
    filename, extension  = os.path.splitext(file)
    if extension == ".pgm":
        new_file = "{}.png".format(filename)
        with Image.open(file) as im:
            im.save(convertedPGM)
