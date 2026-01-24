class Whatsapp:
    def status(self):
        print("Upload a photo video")
class Whatsapp1:
    def status(self):
        print("upload a caption and emojis")
class Whatsapp2(Whatsapp,Whatsapp1):
    def status(self):
        Whatsapp.status(self)
        Whatsapp1.status(self)
        print("Like option")
Rohan = Whatsapp()
print("Rohan")
Rohan.status()

Subhash = Whatsapp1()
print("Subhash")
Subhash.status()

Dhanush = Whatsapp2()
print("Dhanush")
Dhanush.status()