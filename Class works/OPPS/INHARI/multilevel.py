# A -> B

class InstagramV1:
    def post(self):
        print("You can post your images")
    def reel(self):
        print("You con upload your videos")

class InstagramV2(InstagramV1):
    def story(self):
        print("You can upload the 24 hrs story")
    def restriction(self):
        print('You can restrict the account')

class InstagramV3(InstagramV2):
    def note(self):
        print("You can add note")
    def highlights(self):
        print('You can add stories to highlights')
        
print("Abhinoc - InstagramV1")
abhinov = InstagramV1()
abhinov.post()
abhinov.reel()

print("Dhanush - InstagramV2")
dhanush = InstagramV2()
dhanush.post()
dhanush.reel()
dhanush.story()
dhanush.restriction()

print("Vijay - InstagramV3")
Vijay = InstagramV3()
Vijay.post()
Vijay.reel()
Vijay.story()
Vijay.restriction()
Vijay.note()
Vijay.highlights()