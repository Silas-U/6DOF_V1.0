'''-----------------------------------------------------------------------------------------------------#
#                                                                                                       #
# Program : Main activation code for a 6DOF robot arm                                                   #
# Author  : Udofia, Silas Silas                                                                         #
# Project : ROBOT ARM                                                                                   #
# Model   : RB346A                                                                                      #
# Ser_Nom : RB346A6DOFUSSOCT92022                                                                       #
# Date    : October 9, 2022                                                                             #
#                                                                                                       #   
# (inverse kinematics) Given the desired end effector position vector and orientation, solves           #
# for the joint variables th1, th2, th3, th4, th5, th6                                                  #
#                                                                                                       #
-----------------------------------------------------------------------------------------------------'''

from T100_INIT import T100_INIT 

class T100_SETUP:

    RB = T100_INIT()
    #==========================================================================================================
    def Run(self, arr=0):
        for i in range(len(arr)):
            self.RB.setPosition(arr[i][0][0],arr[i][0][1],arr[i][0][2])
            self.RB.setOrientation(arr[i][1][0],arr[i][1][1],arr[i][1][2])
            self.RB.Start()
            print(self.RB.getT1())
            print(self.RB.getT2())
            print(self.RB.getT3())
            print(self.RB.getT4())
            print(self.RB.getT5())
            print(self.RB.getT6())
            print('\n')         
    #==========================================================================================================        
    def Move(self, arr=0):
        self.RB.setPosition(arr[0][0],arr[0][1],arr[0][2])
        self.RB.setOrientation(arr[1][0],arr[1][1],arr[1][2])
        self.RB.Start()
        print(self.RB.getT1())
        print(self.RB.getT2())
        print(self.RB.getT3())
        print(self.RB.getT4())
        print(self.RB.getT5())
        print(self.RB.getT6())
        print('\n')
        

        


