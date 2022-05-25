import os
import datetime
class UI(): 
    def __init__(self):
        self.greeting = str((datetime.datetime.now()).strftime("%Y-%m-%d %H:%M"))
        Parser("entr()# ","Commands.Entry.") # Parser[0] is what the user sees, Parser[1] is where code is called from
#class Logic():
#    def time_of_day():
#        print("It is x time of day")

class Commands:
    class Entry:
        def greeter(arg):
            print("Hi " + arg)

def Parser(prompt,cmdclass):
    while True:
        usercmd = input(prompt)
        usercmd = usercmd.split(" ")
        command = cmdclass + usercmd[0] + "("+"'"+usercmd[1]+"'"+")" # The arguments need to passed as a string, otherwise eval thinks this is some type of variable
        eval(command)

UI()                        
