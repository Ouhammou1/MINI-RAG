filea = open("file.txt" , "r+")

print(filea.read())

filea.write("hello world! ")
filea.close()