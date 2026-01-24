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