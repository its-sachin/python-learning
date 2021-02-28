with open ('links.txt', 'r') as html:
    with open ('output.txt', 'w') as write:
        for line in html.readlines():
            if '<a href =' in line:
                i = 0
                while line.find('<a href =',i) >= 0:
                    pos = line.find('<a href =',i)
                    first_quote = line.find('\"',pos)
                    second_quote = line.find('\"',first_quote+1)
                    url = line[first_quote+1:second_quote]
                    write.write(url + '\n')
                    i += second_quote +1
                