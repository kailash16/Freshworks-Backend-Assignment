import os
class main:
    def __init__(self):
        #d={}
        pass;
        




        
    def create(self):#for create operation
         d={}#'d' is the dictionary in which we store data
         key=input("ENTER THE KEY(MAXIMUM LENGTH OF 32 AND MUST BE A STRING): ");#user can enter the key value
         filename=key;
         if(len(key)>32):#constraints for input key_name capped at 32char
              print("Memory limit exceeded !")#error message when key constraints not satisfy
              print("Please try again\n")
              print("----------------------------\n")
              create();# It will start the session again
         elif(key.isalpha())==False:#constraints for input key_name should be string
             print("Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message when key constraints not satisfy
             print("Please try again\n")
             print("----------------------------\n")
             create();#It will start the session again
        
         value=input("ENTER THE VALUE(MAXIMUM LENGTH 16):");
    
         if(len(d)<(1024*10245*1024) and len(value)>(16*1024*1024)):#constraints for file size less than 1GB and Jasonobject value less than 16KB
            print("Memory limit exceed !\n")#error message when value and file size constraints not satisfy
            print("Create key once again/")
            print("----------------------------\n")
            create();#It will start the session again
         else:
            
            try:
                f = open(filename, 'x') #It will create a file
                print("Key is created")
                f.close()
            except:
                print("Key already exits")# It will show error when the file already exits
                exit();
            try:
                d[key]=value;
                f=open(filename,'wt')
                f.write(str(d))#It will write the data in the file
                f.close()
            except:
                print("Unable to store data")#It will show error when unable to store the data

                
    def parse(self,d): #This function is used read data from a text file as a string and convert that data into a dictionary and return the dictionary
        
        dictionary = dict()
        # Removes curly braces and splits the pairs into a list
        pairs = d.strip('{}').split(', ')
        for i in pairs:
            pair = i.split(': ')
            # Other symbols from the key-value pair should be stripped.
            dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
        
        return dictionary

    def read(self):#for read operation
        flag=0;
        d={}#'d' is the dictionary in which we store data
        key=input("ENTER THE KEY NAME: ");
        filename=key;
       
        try:
            file = open(filename, 'rt')#for read the textfile
            
            lines = file.read().split('\n')
            
            for l in lines:
                if l != '':
                    dictionary = self.parse(l)
                    #print(dictionary)
                    for keys, value in dictionary.items():
                        if keys==key:
                            print(dictionary[keys])#It will show the value for the respective key that users gave as a input
                            flag=1; #if the key is found assign flag to 1;
                            break;
                        
            if(flag==0):#if the key is not found then the key is invalid
                print("Key is invalid");
                    
            file.close()
        except:#if the file is not exits
            print("Key not found! ")

            
    def delete(self):#for delete operation
        key=input("ENTER THE KEY NAME: ")
        filename=key
        
        
        try:
            
            
            os.remove(filename)
            print("Key is deleted")
            
       
       
        
            
            
        except Exception as e:# if the file is not found  then show file not exits
            print("Key not exits!")
            
            
            
            
                
       
        
                
                    
    


    
    
    
        
        












