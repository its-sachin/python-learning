with open ('file1.txt', 'r') as read:
    with open ('file2.txt', 'w') as write:
        for a in read.readlines():
            name,salary = a.split(',')
            write.write(f'{name} has a salary of {salary}')
        