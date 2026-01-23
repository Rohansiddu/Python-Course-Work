class flipkart():
    discount=20
    @classmethod
    def getdisc(cls):
        print(cls.discount)
    @staticmethod
    def banner():
        print("Flipkart buy 1 get 1 sale is going on. \n \t---------Shop Now-----------")

    def __init__(self,name, password,mobileno):
        self.name=name
        self.password=password
        self.mobileno=mobileno
        print(f"Name: {name}\nPassword: {password}\nMobile no: {mobileno}")

abhi=flipkart('Abhi','w3r2342','123456785855899')
abc=flipkart('Abc','asdljhf0923r','6487917924792489')

flipkart.banner()
abhi.banner()

flipkart.getdisc()
abhi.getdisc()


# need not to call method saperately 
# automatically called when the object is created