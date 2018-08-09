import random

list = []
listn = []

with open('list', 'r') as f:
    line = f.readline()
    while line:
        list.append(int(line))
        line = f.readline()

while len(listn) < 90000:
    n = int(random.random()*(10**14))
    if n not in list and n > 9999999999999 and n not in listn:
        listn.append(n)
# f = open('list', 'w')
# for elm in list:
#     f.writelines(str(elm)+'\n')
# f.close()

with open('listn','w') as f:
    for elm in listn:
        f.write(str(elm)+'\n')
