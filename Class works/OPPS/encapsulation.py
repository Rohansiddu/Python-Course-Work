class Facebook:
    def __init__(self,username,password,Ppic):
        self.username=username
        self.__password=password  # __ is for private
        self._Ppic=Ppic # _ is for protected
    @property
    def profileaccess(self):
        return self._Ppic
    
    @profileaccess.setter
    def profileaccess(self,nPic):
        self._Ppic=nPic
    
    def getpwd(self):
        return self.__password
    def setpwd(self,newpwd):
        self.__password = newpwd

abhi=Facebook('Abhi','123456','abhi.png')
print(f"Before:{abhi.username}")
abhi.username='Dhanush'
print(f'After: {abhi.username}')

#Private

print(f'Before: {abhi.getpwd()}')
abhi.setpwd('alskfdj23r2')
print(f'After: {abhi.getpwd()}')


#Protected
print(f'Before: {abhi.profileaccess}')
abhi.profileaccess='DHANUSH.png'
print(f'After: {abhi.profileaccess}')
