print("let's start studying about OOP")

# #To create an empty class
# class StarCookie:
#     pass

#To create a non-empty class
class StarCookie:

    def __init__(self,weight,color='brown'):
        self.weight=weight
        self.color=color
    
    def eat_cookies(self,cons_weight):
        self.weight-=cons_weight


cookie1=StarCookie(8)

print(cookie1.color)
print(f"Weight of original cookie: {cookie1.weight}")
cookie1.eat_cookies(2)
print(f"Weight of cookie after it is being eaten: {cookie1.weight}")


