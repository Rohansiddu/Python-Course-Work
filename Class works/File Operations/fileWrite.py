try:

    file=open('C:/Users/S.ROHAN/Desktop/Python course work/Python-Course-Work/Class works/File Operations/A2.txt','w')
except Exception as e:
    print(f'Error Occured: {e}')
else:
    file.write("New file created")
    file.close()