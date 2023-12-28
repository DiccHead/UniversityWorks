f = open("periodictable.csv", "r")

lines = f.readlines()



def writ():
    list = []
    for i in lines:
        i = i.split(",")
        list.append(i)
    return list