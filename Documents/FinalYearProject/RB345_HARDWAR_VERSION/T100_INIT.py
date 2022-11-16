'''-----------------------------------------------------------------------------------------------------#
#                                                                                                       #
# Program : Initialization for a 6DOF robot arm                                                         #
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

from IKT100 import IKT100 as _6DOF

class T100_INIT:
    
    T100 = _6DOF()
    #===========================================================================================================
    def setPosition(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        #=======================================================================================================
    def setOrientation(self, y=0.1,p=0.1,r=0.1):
        self.yaw = y
        self.pitch = p
        self.roll = r
        #=======================================================================================================
    def Start(self):
        #DESIRED END EFFECTOR POSITION VECTOR FOR ALL CONDITIONS OF PX !> A1 + A2 + A3 + D6 && PY !> A1 + A2 + A3 + D6 && PZ !> A1 + A2 + A3 + D6 + D1
        self.T100.setPosition(self.x,self.y,self.z) #Initial position
        self.T100.setRPY(90,0,0)#Initial orientation
        #=======================================================================================================
        self.T1 = self.T100.GET_TH1_DEG()#Inital value of theta_1
        self.T2 = self.T100.GET_TH2_DEG()#Initial value of theta_2
        self.T3 = self.T100.GET_TH3_DEG()#Initial value of theta_3
        #=======================================================================================================
        self.T100.setPosition(self.x,self.y,self.z)
        #=======================================================================================================
        self.T100.setT1(self.T1)
        self.T100.setT2(self.T2)
        self.T100.setT3(self.T3)
        #=======================================================================================================
        self.T100.setRPY(self.roll,self.pitch,self.yaw) #Roll,Pitch,(Yaw = 90 deg default)
        #=======================================================================================================
        self.T1o = self.T100.GET_TH1_DEG()
        self.T2o = self.T100.GET_TH2_DEG()
        self.T3o = self.T100.GET_TH3_DEG()
        #=======================================================================================================
    def getT1(self):
        return round(self.T1o)
    def getT2(self):
        return round(self.T2o)
    def getT3(self):
        return round(self.T3o)
    def getT4(self):
        return round(self.T100.GET_TH4_DEG())
    def getT5(self):
        return round(self.T100.GET_TH5_DEG())
    def getT6(self):
        return round(self.T100.GET_TH6_DEG())
    

    




