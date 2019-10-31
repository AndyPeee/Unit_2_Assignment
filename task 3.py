listtoread = []  # this makes the list that will be printed with all the info. It is a list because it needs to be appended to
print("Enter space if unknown")
lname = input("LName ").lower()
fname = input("FName ").lower()
grade = input("Grade ").lower()
house = input("House ").lower()
adviser = input("Adviser ").lower()
allthelist = [lname, fname, grade, house, adviser]  # makes a list of their answers that will be compared to the txt document
f = open("studentinfo.txt", "r")
info = f.readlines()  # reads the lines of the txt document to be compared
line1 = (info[1].strip("\n"))  # assignes each of the students with a variable
line2 = (info[2].strip("\n"))
line3 = (info[3].strip("\n"))
line4 = (info[4].strip("\n"))
line5 = (info[5].strip("\n"))
listofinfo = [line1, line2, line3, line4, line5]  # puts the students in a list to be compared to
for x in range(len(listofinfo)):  # looks through every part of the list of info given and compares to the students info, if the student has data that compares, it appends to a master list
    if lname in listofinfo[x]:
        listtoread.append(listofinfo[x])
        lname = "done"
    elif fname in listofinfo[x]:
        listtoread.append(listofinfo[x])
        fname = "done"
    elif grade in listofinfo[x]:
        listtoread.append(listofinfo[x])
        grade = "done"
    elif house in listofinfo[x]:
        listtoread.append(listofinfo[x])
        house = "done"
    elif adviser in listofinfo[x]:
        adviser = "done"
        listtoread.append(listofinfo[x])
print(str(listtoread).strip("[]"+","+"'"))  # the master list that has all of the compared data is printed (without brackets and commas)
