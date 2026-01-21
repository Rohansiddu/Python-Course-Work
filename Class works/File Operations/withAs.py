#need not to close the file once opened while using "with as"
#better option 
with open('C:/Users/S.ROHAN/Desktop/Python course work/Python-Course-Work/Class works/File Operations/A1.txt','r') as file:
    print(file.read())