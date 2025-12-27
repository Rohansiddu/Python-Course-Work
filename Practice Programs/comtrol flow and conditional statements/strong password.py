'''Validate strong password (min 8 chars, 1 uppercase, 1 digit, 1 special
char)
Question: Use nested if-else or multiple checks.
Test Cases:
Input: "Abcdef@1" → Output: Strong Password
Input: "abc123" → Output: Weak Password'''

pwd=input("password: ")
if len(pwd)>=8:
    s=set()
    for i in pwd:
        if i.isupper():
            s.add("u")
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
    if len(s)==4:
        print("Strong password")
    else:
        print("week password")
else:
    print("too short")
