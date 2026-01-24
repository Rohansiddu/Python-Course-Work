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
class Autoscroll:
    def scroll(self):
        print("Now you can turn on the autoscroll")
class Summarize:
    def summarizemsg(self):
        print("Now the mwssage can be simmarized")
class InstagramV4(InstagramV3,Autoscroll,Summarize):
    def repost(self):
        print("You can re-post the stories")

        
print("Abhinov - InstagramV1")
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

print("Rohan - InstagramV4")
Rohan = InstagramV4()
Rohan.post()
Rohan.reel()
Rohan.story()
Rohan.restriction()
Rohan.note()
Rohan.highlights()
Rohan.scroll()
Rohan.summarizemsg()
Rohan.repost()