# class Robot:
#     pass

# if __name__ == "__main__":
#     x = Robot()
#     y = Robot()
#     y2 = y
#     print(y==y2)
#     print(y==x)

# class Robot:
#     def __init__(self, name=None, build_year=None):
#         self.name = name
#         self.build_year = build_year

#     def say_hi(self):
#         if self.name:
#             print('Hi, I am '+self.name)
#         else:
#             print('I do not have a name')
#         if self.build_year:
#             print('I was built in', self.build_year)
#         else:
#             print('I do not know when I was built')
        
#     def set_name(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name

#     def set_build_year(self, build_year):
#         self.build_year = build_year

#     def get_build_year(self):
#         return self.build_year
        

# x = Robot()
# x.set_name('Henry')
# x.say_hi()
# y = Robot(x.get_name(), 2008)
# # y.set_name(x.get_name())
# print(y.get_name())
# y.say_hi()

class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = self.build_year

    def __repr__(self):
        return "Robot(\""+self.name+"\","+str(self.build_year)+")"

    def __str__(self):
        return 'Name:'+self.name+", Build Name:"+str(self.build_year)

if __name__=="__main__":
    x = Robot("Marvin", 1979)
    x_repr = repr(x)
    print(x_repr, type(x_repr))
    new = eval(x_repr)
    print(new)
    print('Type of new:', type(new))