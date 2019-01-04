from BANKCLASSES import *
def writeAccounts(seamenBank):
    file=open("Account.txt","w")
    for x in range(0,len(seamenBank.accID)):
        file.write("%s\nBalance : %d\n"%(seamenBank.accID[x],seamenBank.accBals[x]))
    file.close()
def readAccounts(seamenBank):
    file=open("Account.txt","r+")

    for x in file.readlines():
        if x[0:9]=="Balance :":
            bal=int(x[10:].replace(" ",""))
            cust=Customer(bal)
            cust.setName(name)
            acc=Account(cust)
            seamenBank.addAcc(acc)
        elif x[0:9]!="":
            y=x.split()
            name=""
            for i in range(0,len(y)):
                if name!="":
                    name=name+" "+y[i]
                else:
                    name=y[i]


    file.close()
