file = open('KeygenMe.jad', 'r')
line = file.readline()

arr = ['' for i in range(35)]
while(line):
    index = line.find('charAt')
    eindex = line.find('!=')
    if index > -1:
        num = line[index+7: index+9]
        if num[1] == ')': num = num[0]
        num = int(num)

        arr[num] = line[eindex + 4]

    line = file.readline()

print(''.join(arr))
