with open("codingal.txt",'w') as file:
    file.write("Hi my name is Sravan and I am 10 years old")
file.close()

with open("codingal.txt",'r') as file:
    a=file.readlines()
    for i in a:
        data=i.split()
        print(data)
file.close()


# newfile=open("sravan.txt",'x')

import os
if os.path.exists("abc.txt"):
    os.remove("abc.txt")
else:
    print("There is no such file/1")


file=open("sr.txt",'a')
file.write("My school name is GURU THE GLOBAL SCHOOL."
" It is in Hyderabad Nigampet MITHRA HILls colony")
file.write("My hobbies are drawing,painting,Art,playing .")
file.close()
       
