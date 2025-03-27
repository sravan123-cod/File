file=open("mno.txt",'w')
file.write("I love coding")
file.write("\n")
file.write("I love html")
file.write("\n")
file.write("I love css")
file.write("\n")
file.write("I love bootstrap")
file.write("\n")
file.write("I love java")
file.write("\n")
file.write("I love python")
file.write("\n")
file.close()


file1=open("mno.txt",'r')
print(file1.read(7))
print(file1.readline())
file1.close()


file2=open("mno.txt",'r')
for a in file2:
    print(a)
file2.close()
