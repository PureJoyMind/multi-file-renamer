import os

#getting the list of the files in a folder

lists = os.listdir("C:/Users/hp/Desktop/book2/jpg")

#the following function is for better organization

def printf(a):
    for i in a:
        print(i)


# a more general approach to find srt files

srt = []
for file in lists:
    if file[-3] == "srt":
        srt.append(file)

printf(srt)

#i have to write sth
#to make the 0number work.
#exmple: 04, 05, 10
k = 1
b = "0"
for file in srt:
    if k < 10:
        b = "0" + str(k)
        k += 1
    else:
        k += 1
    os.rename(f"C:/Users/hp/Desktop/book2/jpg/{file}",f"C:/Users/hp/Desktop/book2/jpg/{b}")
