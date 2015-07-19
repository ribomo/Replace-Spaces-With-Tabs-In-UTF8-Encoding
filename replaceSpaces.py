import codecs
import sys
import re

print('Open file')
file_ob = codecs.open('d:\\1.txt','r','utf-8')
file_out = codecs.open('d:\\1.txt','w','utf-8')
fileLines = 3000000 #Replace this with the how many line your file contains.
try:
    print('Start')
    i = 1
    isDone = 0
    while(isDone != 1):
            line = file_ob.readline()
            if(line != ''):
                    if(i%50000==0):
                        print(str(i*100/fileLines)+"%")
                    i+=1

                    line = line.rstrip()
                    elements = re.split(r'\s{9,}',line)
                    info = "\t".join(elements)
                    info += "\n"
                    file_out.write(info)
            else:
                    isDone = 1
finally:
	file_ob.close()
	file_out.close()
	print('Exit')
