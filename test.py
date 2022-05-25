import os
import datetime
class UI():
    def __init__(self):
        self.greeting = str((datetime.datetime.now()).strftime("%Y-%m-%d %H:%M"))
        #print(self.greeting)
#class Logic():
#    def time_of_day():
#        print("It is x time of day")

UI()                        
