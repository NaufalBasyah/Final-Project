import random                                                                   #importing random library

def randomText(list,list2):                                                     #a method to open one of three text file to use for the game
    a=random.randint(1,3)                                                       #random int from 1 to 3 to decide which text file will be used
    num=a
    wordset=""
    if a==1:
        wordset="Gatsby.txt"
    elif a==2:
        wordset="Macbeth.txt"
    else:
        wordset="beatles.txt"
    f=open(wordset,"r")                                                         #opening the txt file to read

    for line in f.readlines():
        if "#" not in line:                                                     #this loop will turn each line from the txt file into a list of words
            list.append(line.replace("\n",""))
            a=line.replace("’","'").replace("\n","").replace("—","--").split()      #replacing some symbols or notations that might be a problem later
            for x in a:
                list2.append(x)

    return num                                                                  #this method will also return the variable num as an indicator of which file is used
def CheckScore(list1,list2,list3):                                              #This method will check the score from the txt file and turning it into a series of lists
    file=open("GameScore.txt","r")                                              #opening the file to read
    for line in file.readlines():
        if line[0:15]=="DUCK DODGE-RS: ":
            list1.append(float(line[15:]))
        elif line[0:12]=="F1 CIRCUIT: ":
            list2.append(float(line[12:]))
        elif line[0:8]=="GATSBY :":
            data=line[8:].split(",")
            scores=[]
            for x in data:
                scores.append(float(x))
            list3.append(scores)
        elif line[0:8]=="MACBETH:":                                         #all the scores are put into the list1 list2 and list3 respectively
            data=line[8:].split(",")
            scores=[]
            for x in data:
                scores.append(float(x))
            list3.append(scores)
        elif line[0:8]=="BEATLES:":
            data=line[8:].split(",")
            scores=[]
            for x in data:
                scores.append(float(x))
            list3.append(scores)
    file.close()                                                               #closing the file to avoid corruption of the file
    print(list1,list2,list3)
def writeScore(list1,list2,list3):                                              #this will read the list of highscores in game and writing them down to a txt file with a specific format
    file=open("GameScore.txt","w")
    file.write("SCORE BOARD\n")
    file.write("____________\n")
    file.write("DUCK DODGE-RS: %.3f\n"%(list1[0]))
    file.write("F1 CIRCUIT: %.3f\n"%(list2[0]))
    file.write("KEYBOARD WARRIOR\n")
    file.write("GATSBY :%.2f,%.2f\n"%(list3[0][0],list3[0][1]))
    file.write("MACBETH:%.2f,%.2f\n"%(list3[1][0],list3[1][1]))
    file.write("BEATLES:%.2f,%.2f\n"%(list3[2][0],list3[2][1]))
    file.close()
    file=open("GameScore.txt","r")
    for line in file.readlines():
        print(line)
    file.close()
