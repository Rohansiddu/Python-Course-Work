try:

    file=open('C:/Users/S.ROHAN/Desktop/Python course work/Python-Course-Work/Class works/File Operations/A1.txt','r')
except Exception as e:
    print(f'Error Occured: {e}')
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    file.close()