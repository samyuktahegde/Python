# class C:
#     counter = 0
#     def __init__(self):
#         type(self).counter += 1
#     def __del__(self):
#         type(self).counter -= 1

# if __name__ == "__main__":
#     x = C()
#     print('Number of instances: '+str(C.counter))
#     y = C()
#     print('Number of instances: '+str(C.counter))
#     del x
#     print('Number of instances: '+str(C.counter))
#     del y
#     print('Number of instances: '+str(C.counter))

class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    # def RobotInstances(self):
    #     return Robot.__counter

    @staticmethod
    def RobotInstances():
        return Robot.__counter

if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())

