import os

#getting the list of the files in a folder
inp = str(input("Enter your directory: \n   "))
inp = inp.replace('\\','/')

lists = os.listdir(inp)


#the following function is for better organization

def printf(a):
    for i in a:
        print(i)


# a more general approach to find srt files

srt = []
for file in lists:
    if file[-3:] == "srt":
        srt.append(file)

printf(srt)

#now we need to have the name of the episode
print("Enter the name of the episode: ")
ep_name = str(input("\"Please replace the number of the episode with {b} in order for the program to work properly\"\n"))

#the following renames the ep numbers
#with the 01 format
#exmple: 04, 05, 10
k = 1
b = "0"
for file in srt:
    if k < 10:
        b = "0" + str(k)
        k += 1
    else:
        k += 1
    os.rename(f"{inp}" + "/" + f"{file}",f"{inp}" + "/" + f"{ep_name}")
