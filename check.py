file = open('model.py', 'r')
line = file.readlines()
number=line[19][2:len(line[0])-1]
number=int(number)+1
number=str(number)
#print(number)
line[0] = line[0][0:6] + number + line[0][len(line[0])-1]
file = open('model.py', 'w')
file.writelines(line)