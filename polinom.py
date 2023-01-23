# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5*x**2 + 3*x
# 2.  3*x**2 + x + 8
# 3. Результат: 8*x**2 + 4*x + 8
import re
import itertools
  
def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
        pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

def fold_pols(pol1, pol2):   
    dict = {}
    # x= (max(max(pol1),max(pol2)))
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:   
         x[i[1]] += i[0]
         res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    print(x)
    return res

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)


data = open('polinoms1.txt', encoding='utf-8')
polin1 = data.readline()
# polinom1 = str(polin1.split(' +'))
data = open('polinoms2.txt', encoding='utf-8')
polin2 = data.readline()
# polinom2 = str(polin2.split(' +'))


data.close

file_sum = 'sum_polinoms.txt'
dictinary = convert_pol(polin1)  
dictinary2 = convert_pol(polin2)

print(polin1)
print(polin2)    
print(dictinary)
print(dictinary2)

pol_sum = get_sum_pol(fold_pols(dictinary, dictinary2))
write_to_file(file_sum, pol_sum)








