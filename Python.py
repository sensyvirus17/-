from math import *
from colorama import *
init()
def daraje():
    za1 = int(input("radian mored nazar ra vared konid => "))
    print(radians(za1))
def radian():
    za1 = int(input("daraje mored nazar ra vared konid => "))
    print(degrees(za1))
def zarb():
	za1 = int(input("add mored nazar ra vared konid => "))
	za2 = int(input("add dovom mored nazar ra vared konid => "))
	print(za1*za2)
def jam():
	za1 = int(input("add mored nazar ra vared konid => "))
	za2 = int(input("add dovom mored nazar ra vared konid => "))
	print(za1+za2)
def menha():
	print("ravesh kar add - add dovom ")
	za1 = int(input("add mored nazar ra vared konid => "))
	za2 = int(input("add dovom mored nazar ra vared konid => "))
	print(za1-za2)

def tanx():
	try:
		za1 = int(input("zavie mored nazar ra vared konid => "))
		print(tan(za1))
	except:
		print("just number !")
def cosx():
	try:
		za1 = int(input("zavie mored nazar ra vared konid => "))
		print(cos(za1))
	except:
		print("just number !")
def sinx():
	try:
		za1 = int(input("zavie mored nazar ra vared konid => "))
		print(sin(za1))
	except:
		print("just number !")
def cot():
	try:
		za1 = int(input("zavie mored nazar ra vared konid => "))
		print(sin(za1))
	except:
		print("just number !")
def main():
    while True:
        try:
            item = int(input("enter the item => "))
            if item == 1: 
                mos()
            elif item == 2:
                tavanm()
            elif item == 3:
                break
            elif item == 4:
            	zarb()
            elif item == 5:
            	jam()
            elif item == 6:
            	menha()
            elif item == 7:
            	print(pi)
            elif item == 8:
            	radian()
            elif item == 9:
            	daraje()
        except:
            print("pleas just enter the  number !")
def tavanm():
    print("ravesh kar = x be tavan y")
    x = int(input("enter the x => "))
    y = int(input("enter the y => "))
    print(pow(x,y))
def mos():
    print(Fore.GREEN +'''
        [1]tan
        [2]cos
        [3]sin
        [4]cot
        [5]exit
        ''')
    try:
        mos2 = int(input("enter the item => "))
        if mos2 == 1:
           tanx() 
        elif mos2 == 2:
           cosx()
        elif mos2 == 3:
           sinx()
        elif mos2 == 4:
           cotx() 
        elif mos2 == 5:
            main()
    except:
    	print("just number !")

print(Fore.RED +'''


      ##############################
      ##############################
      ###[/]   welcome to     [/]###
      ###[/]   sensy math     [/]###
      ###[/]        .         [/]###
      ###[/]        .         [/]###
      ############################## 
      ##############################
      items :
            [1]mosalasat
            [2]tavan
            [3]khoroj
            [4]zarb
            [5]jam
            [6]menha
            [7]add pi
            [8]radian be zavie
            [9]zavie be radian
            

	  ''')

main()
