menu=0
word=[]
s=0
del_s=0
while menu!=4:
    print("***************************************************")
    print("*              Sookmyung Dictionary               *")
    print("***************************************************")
    print("                1.Save words                       ")
    print("                2.Delete words                     ")
    print("                3.Print all words                  ")
    print("                4.Exit                             ")
    print("===================================================")
    menu=int(input("Select  >>"))
    if menu==1:
        print("Enter word to save. Press 'Enter' to finish.\n")
        while True:
            print("Word :",end='')
            s=input()
            if len(s)==0:
                break
            if s in word:
                print("Already Exist")
            else:
                word.append(s)
            
    elif menu==2:
        print("Enter word to delete\n")
        while True:
            print("Word:",end='')
            del_s=input()
            if del_s not in word:
                print("No Exist")
            else:
                word.remove(del_s)
                print("Deletion complete")
                
    elif menu==3:
        print()
        for s in word:
            print(s)
    elif menu==4:
        break
    else:
        print("You entered wrong menu")
        
