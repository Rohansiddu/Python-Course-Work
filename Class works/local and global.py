'''def display():
    name="Rohith"             #local
    print(f'Inside: {name}')
name='Abhi'        #Global
display()
print(f'Outside: {name}')'''
#local change does not effect global vairabl

'''def display():
    global name   #used to effect globally
    name="Rohith"             #local
    print(f'Inside: {name}')
name='Abhi'        #Global
display()
print(f'Outside: {name}')'''

#Non local
def display(course):
    print(f'Starting: {course}')

    def change():
        nonlocal course
        course = "Python Full Stack"
        print(f'change: {course}')
    change()

    print(f'Final course: {course}')

course='Java Full Stack'
display(course)