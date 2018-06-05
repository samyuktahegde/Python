# class Robot:
#     __counter = 0

#     def __init__(self):
#         type(self).__counter+=1

#     @classmethod
#     def RobotInstances(cls):
#         return cls, Robot.__counter


# if __name__ == "__main__":
#     print(Robot.RobotInstances())
#     x = Robot()
#     print(x.RobotInstances())
#     y = Robot()
#     print(x.RobotInstances())
#     print(Robot.RobotInstances())

# class fraction(object):
#     def __init__(self, n, d):
#         self.numerator, self.denominator = fraction.reduce(n, d)

#     @staticmethod
#     def gcd(a,b):
#         while b!=0:
#             a,b = b, a%b
#         return a

#     @classmethod
#     def reduce(cls, n1, n2):
#         g = cls.gcd(n1, n2)
#         return (n1//g, n2//g)

#     def __str__(self):
#         return str(self.numerator)+'/'+str(self.denominator)

# class Pets:
#     name = "pet animals"

#     # @staticmethod
#     # def about():
#     #     print("This is a class about {}!".format(Pets.name))
#     @classmethod
#     def about(cls):
#         print("This is a class about {}!".format(cls.name))

# class Dogs(Pets):
#     name = "'man's best friends' (Frederick II)"

# class Cats(Pets):
#     name = "cats"

# p = Pets()
# p.about()
# d = Dogs()
# d.about()
# c = Cats()
# c.about()

# class P:
#     def __init__(self, x):
#         self.__x = x

#     def get_x(self):
#         return self.__x

#     def set_x(self, x):
#         self.__x = x
# class P:
#     def __init__(self, x):
#         self.x = x

#     def get_x(self):
#         return self.x

#     def set_x(self, x):
#         self.x = x

# class P:
#     def __init__(self, x):
#         self.set_x(x)

#     def get_x(self):
#         return self.__x

#     def set_x(self, x):
#         if x<0:
#             self.__x = 0
#         elif x>1000:
#             self.__x = 1000
#         else:
#             self.__x = x

class P:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x<0:
            self.__x = 0
        elif x>1000:
            self.__x = 1000
        else:
            self.__x=x
