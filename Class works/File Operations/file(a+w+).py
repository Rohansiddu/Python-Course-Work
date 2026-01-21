try:

    file=open('C:/Users/S.ROHAN/Desktop/Python course work/Python-Course-Work/Class works/File Operations/A1.txt','a+')
except Exception as e:
    print(f'Error Occured: {e}')
else:
    file.write("\t Info added \t done for the day")
    file.seek(0)
    print(file.read())
    file.close()