class User:
    def __init__(self, name, age:int):
        self.name = name
        self.age = age


user1 = User('sama',22 )
print(user1.name)
print(user1.age)
