'''
Recursion implementation in Python
'''


def openRussianDoll(doll):
    if doll==1:
        print("The doll is opened")
    else:
        openRussianDoll(doll-1)


#testing the recursive function
openRussianDoll(6)