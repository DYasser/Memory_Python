#Nabil Yasser
#Python3~

from random import *
import time
def RESTART():
    variables = {'x1':1, 'x2':2, 'x3':3, 'x4':4, 'x5':5, 'x6':6, 'x7':7, 'x8':8, 'x9':9, 'x10':10, 'x11':11, 'x12':12, 'x13':13, 'x14':14, 'x15':15, 'x16':16, 'x17':17}
    lost = 0
    lost1 = 0
    lost2 = 0
    lost3 = 0
    p=1
    X=1
    print("\n\n\n                         How much players want to play?\n(Choices choose between 2 and 3)")
    Play = input("Choice: ")
    while Play.isdigit() == False or int(Play) not in range(2,4):
        print("A number in the choices please")
        Play = input("Please, rewrite it: ")
    print("\n\n\n\n                                        WELCOME!!!\n         I'll explain all the details of this little game, but first tell me your names.")
    x1 = input("\nPlayer 1's name?> ")
    while x1.isalpha() == False:
        print("Just letters please.")
        x1 = input("Re-Write your name please: ")
    x2 = input("Player 2's name?> ")
    while x2.isalpha() == False:
        print("Just letters please.")
        x2 = input("Re-Write your name please: ")
    if int(Play)==3:
        x3 = input("Player 3's name?> ")
        while x3.isalpha() == False:
            print("Just letters please.")
            x3 = input("Re-Write your name please: ")
    print("\n                           ALRIGHT!   WELCOME To My Game!\n                This game will test your memory.\n            So you'll first type the successive numbers that are present from 1 to 17.\n              in the end the player who typed 17 will have the honor to change a random number to any number of his choice.")
    Y = input("")
    print("If you still didn't understood. Here are the numbers you will write: '1', the next player will write '2' etc.\n However when the player who wrote 17, will change for example the 7th element, which is 7\n You will write 1 - 2 -..-6 - the number he chose!")
    Y = input("")
    print("                                You will loop another time, and each time the player who wrote 17 will change a random number.")
    print("                                    Simple right! It will be a shame if you lost.")
    Y = input("")
    print("                                            So, let's begin!")
    Y = input("")
    start = int(time.time())
    
    while int(Play) == 2:# In This While Loop Plays The Code responsible of 2 players' game !
        if p%2 == 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x1,"'s Turn================================]")
            Y = input("The Number> ")
            while Y.isdigit() == False:
                print("Write a number please!")
                Y = input("The Number> ")
            if int(Y) == variables['x'+'{}'.format(X)]:
                print("Good job")
                X+=1
                p+=1
                if p >2:
                    p = 1
            else:
                print(x1,"LOST")
                lost = 1
                lost1 = 1
                break
        elif p%2 != 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x2,"'s Turn================================]")
            Y = input("The Number> ")
            while Y.isdigit() == False:
                print("Write a number please!")
                Y = input("The Number> ")
            if int(Y) == variables['x'+'{}'.format(X)]:
                print("Good job")
                X+=1
                p+=1
                if p >2:
                    p = 1
            else:
                print(x2,"LOST")
                lost = 1
                lost2 = 1
                break
        if X > 17:
            X = 1
            vary = randint(1,17)
            print("\n\nNow you can choose a Number to replace the element number:",vary,"of the list!")
            variables['x'+"{}".format(vary)] = int(input("Element will change to: "))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while lost == 1:
        end = int(time.time())
        if lost1 == 1:
            print(x2,"Won !!!")
        elif lost2 == 1:
            print(x1,"Won !!!")
        print("Congratulation to everyone for staying",end - start,"seconds, or maybe it is more confortable to see it in minutes:",round(((end-start)/60),1),"minutes")    
        print("\n\nDo you want to restart?")
        Y = input("type Y for Yes and anyother thing for No: ")
        if Y == "y" or Y == "Y":
            RESTART()
        else:
            print("Have a nice day")
            break
        
    while int(Play) == 3:# In This While Loop Plays The Code responsible of 3 players' game !
        if p%3 == 1:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x1,"'s Turn================================]")
            Y = input("The Number> ")
            while Y.isdigit() == False:
                print("Write a number please!")
                Y = input("The Number> ")
            if int(Y) == variables['x'+'{}'.format(X)]:
                print("Good job")
                X+=1
                p+=1
                if p >3:
                    p = 1
            else:
                print(x1,"LOST")
                lost1 +=1
                # THE GAME CONTINUES HERE FOR THE TWO OTHERS PLAYER if the 1st Player lost
                p = 1
                while lost1 == 1:
                    if p%2 == 0:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x2,"'s Turn================================]")
                        Y = input("The Number> ")
                        while Y.isdigit() == False:
                            print("Write a number please!")
                            Y = input("The Number> ")
                        if int(Y) == variables['x'+'{}'.format(X)]:
                            print("Good job")
                            X+=1
                            p+=1
                            if p >2:
                                p = 1
                        else:
                            print(x2,"LOST")
                            lost = 1
                            lost2 += 1
                            break
                    elif p%2 != 0:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x3,"'s Turn================================]")
                        Y = input("The Number> ")
                        while Y.isdigit() == False:
                            print("Write a number please!")
                            Y = input("The Number> ")
                        if int(Y) == variables['x'+'{}'.format(X)]:
                            print("Good job")
                            X+=1
                            p+=1
                            if p >2:
                                p = 1
                        else:
                            print(x3,"LOST")
                            lost = 1
                            lost3 += 1
                            break
                    if X > 17:
                        X = 1
                        vary = randint(1,17)
                        print("\n\nNow you can choose a Number to replace the element number:",vary,"of the list!")
                        variables['x'+"{}".format(vary)] = int(input("Element will change to: "))
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                while lost == 1:
                    if lost3 == 1:
                        print(x2,"WON !!!")
                    else:
                        print(x3,"WON !!!")
                    end = int(time.time())
                    print("Congratulation to everyone for staying",end - start,"seconds, or maybe it is more confortable to see it in minutes:",round(((end-start)/60),1),"minutes")    
                    print("\n\nDo you want to restart?")
                    Y = input("type Y for Yes and anyother thing for No: ")
                    if Y == "y" or Y == "Y":
                        RESTART()
                    else:
                        print("Have a nice day")
                        break
                break
            
        elif p%3 == 2:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x2,"'s Turn================================]")
            Y = input("The Number> ")
            while Y.isdigit() == False:
                print("Write a number please!")
                Y = input("The Number> ")
            if int(Y) == variables['x'+'{}'.format(X)]:
                print("Good job")
                X+=1
                p+=1
                if p >3:
                    p = 1
            else:
                print(x2,"LOST")
                lost2 += 1
                # THE GAME CONTINUES HERE FOR THE TWO OTHERS PLAYER if the 2nd Player lost
                p = 1
                while lost2 == 1:
                    if p%2 == 0:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x1,"'s Turn================================]")
                        Y = input("The Number> ")
                        while Y.isdigit() == False:
                            print("Write a number please!")
                            Y = input("The Number> ")
                        if int(Y) == variables['x'+'{}'.format(X)]:
                            print("Good job")
                            X+=1
                            p+=1
                            if p >2:
                                p = 1
                        else:
                            print(x1,"LOST")
                            lost = 1
                            lost1 += 1
                            break
                    elif p%2 != 0:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x3,"'s Turn================================]")
                        Y = input("The Number> ")
                        while Y.isdigit() == False:
                            print("Write a number please!")
                            Y = input("The Number> ")
                        if int(Y) == variables['x'+'{}'.format(X)]:
                            print("Good job")
                            X+=1
                            p+=1
                            if p >2:
                                p = 1
                        else:
                            print(x3,"LOST")
                            lost = 1
                            lost3 += 1
                            break
                    if X > 17:
                        X = 1
                        vary = randint(1,17)
                        print("\n\nNow you can choose a Number to replace the element number:",vary,"of the list!")
                        variables['x'+"{}".format(vary)] = int(input("Element will change to: "))
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                while lost == 1:
                    if lost3 == 1:
                        print(x1,"WON !!!")
                    else:
                        print(x3,"WON !!!")
                    end = int(time.time())
                    print("Congratulation to everyone for staying",end - start,"seconds, or maybe it is more confortable to see it in minutes:",round(((end-start)/60),1),"minutes")    
                    print("\n\nDo you want to restart?")
                    Y = input("type Y for Yes and anyother thing for No: ")
                    if Y == "y" or Y == "Y":
                        RESTART()
                    else:
                        print("Have a nice day")
                        break
                break

            
        elif p%3 == 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x3,"'s Turn================================]")
            Y = input("The Number> ")
            while Y.isdigit() == False:
                print("Write a number please!")
                Y = input("The Number> ")
            if int(Y) == variables['x'+'{}'.format(X)]:
                print("Good job")
                X+=1
                p+=1
                if p >3:
                    p = 1
            else:
                print(x3,"LOST")
                lost3 += 1
                # THE GAME CONTINUES HERE FOR THE TWO OTHERS PLAYER if the 3rd Player lost
                p = 1
                while lost3 == 1:
                    if p%2 == 0:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x1,"'s Turn================================]")
                        Y = input("The Number> ")
                        while Y.isdigit() == False:
                            print("Write a number please!")
                            Y = input("The Number> ")
                        if int(Y) == variables['x'+'{}'.format(X)]:
                            print("Good job")
                            X+=1
                            p+=1
                            if p >2:
                                p = 1
                        else:
                            print(x1,"LOST")
                            lost = 1
                            lost1 += 1
                            break
                    elif p%2 != 0:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[================================",x2,"'s Turn================================]")
                        Y = input("The Number> ")
                        while Y.isdigit() == False:
                            print("Write a number please!")
                            Y = input("The Number> ")
                        if int(Y) == variables['x'+'{}'.format(X)]:
                            print("Good job")
                            X+=1
                            p+=1
                            if p >2:
                                p = 1
                        else:
                            print(x2,"LOST")
                            lost = 1
                            lost2 += 1
                            break
                    if X > 17:
                        X = 1
                        vary = randint(1,17)
                        print("\n\nNow you can choose a Number to replace the element number:",vary,"of the list!")
                        variables['x'+"{}".format(vary)] = int(input("Element will change to: "))
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                while lost == 1:
                    if lost2 == 1:
                        print(x1,"WON !!!")
                    else:
                        print(x2,"WON !!!")
                    end = int(time.time())
                    print("Congratulation to everyone for staying",end - start,"seconds, or maybe it is more confortable to see it in minutes:",round(((end-start)/60),1),"minutes")    
                    print("\n\nDo you want to restart?")
                    Y = input("type Y for Yes and anyother thing for No: ")
                    if Y == "y" or Y == "Y":
                        RESTART()
                    else:
                        print("Have a nice day")
                        break
                break
            
        elif X > 17:
            X = 1
            vary = randint(1,17)
            print("\n\nNow you can choose a Number to replace the element number:",vary,"of the list!")
            variables['x'+"{}".format(vary)] = int(input("Element will change to: "))
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

RESTART()
