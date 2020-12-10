from sourcecode import main #import the sourcecode.py and class main
def initial():
    x=main()#create the object 
    print('''    1. Create file and store data
    2. Read data
    3. Delete data''')
    choice=int(input("ENTER THE CHOICE..."))
    if(choice==1):
        
        x.create()#call the create method
    elif (choice==2):
        x.read();#call the read method
    elif(choice==3):
       x.delete();#call the delete method
    else:
        print("Invalid choice\n")
        print("Please try again\n")
        initial()#if the option is wrong then call the function again
        
initial()#call the initial fucntion to start the process
