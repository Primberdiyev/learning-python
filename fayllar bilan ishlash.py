with open('yangi.txt') as file:
    obyekt=file.read()
#print(obyekt)
with open('yangi.txt','w') as file:
    obyekt1=file.write('you will be a strong senior developer')

with open('yangi.txt','a') as file:
    obyekt2=file.write('\nwouldn\'t you ')

obyekt=obyekt.replace('\n',' ')
#print(obyekt)
with open('yangi.txt') as file:
    for line in file:
        print(line)
with open('yangi.txt') as file:
    gaplarim=file.readlines()
gaplarim=[gap.rstrip() for gap in gaplarim]
print(gaplarim)

    



