file=open("abc.txt",'w')
file.write("Hi my name is Sravan iam writing in a file")
file.close()

file1=open("abc.txt",'r')
print(file1.read())
file1.close()

file2=open("abc.txt",'a')
file2.write("I love coding")
file2.close()