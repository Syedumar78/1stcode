#**********1st program *******
a = 30
b = 70
c = a+b
print(c)
#-----------2nd program-------------------#
A = 70
B = 90
C = B*A
D = C*B
print(C)
print(D)
#-----------3rd program--------------------#
_p = 1
_q = 3
_r = 8
print((_p * _q + _r // _q))
#-----------4th program-------------------#
_No_of_students = 1500
_no_of_teachers = 100
print((_No_of_students *_no_of_teachers))
#-------shorter way to re-assingn the values on a variable (_No_of_students [+ =] 500)you can change with any operator with this method --------------------------------- 
_No_of_students = _No_of_students + 500
print(_No_of_students + _no_of_teachers)
#-----------5th programm-------concatenation----method--used--to--integer--and--string------#
N = 18
n = 21
print(f"{N + n}" + " " + ("are their total age"))
#---------6th programme-----condition---statement---(if, else, elif)---------#
#--------if----else-----programme------#
_FYLE = 80
_KYLE = 90
if _FYLE >= _KYLE :
    print("_FYLE is greater than _KYLE")
else :
    print("_KYLE is greater than _FYLE")
#-----------if---elif--else--programme------------#
_FLY = 300
_CRY = 600 
if _FLY >=_CRY :
    print("_FLY has the highest rate")
elif _FLY<=_CRY :
    print("_CRY has the highest rate")   
else :
    print(" E_R_R_O_R, I_N, C_A_L_C_U_L_A_T_O_N ")
#--------7th programm--user--input--string--#
user_input = input("Enter your favorite food name?:")
print("your favorite food name is "+ user_input)
#------8th programm--user_input---in--conditional--statements---------integer--#
_Input =input("enter a number :  ")
number = float(_Input)
if number >= 1000000000000000000000000000000000 :
    print("you have entered the number out of the limit ")
elif number <= 1000000000000000000000000000000000 :
    print("you have entered a lesser number") 
else :
    print("WRONG CLACULATION")
#------------9th programm--user_input---in--conditional--statment----string--#
human_input = input("Enter a word : ") 
if human_input == ("hello") :
    print("hi buddy")
elif human_input == ("bye") :
    print("good bye buddy ")
else :  
    print("the give input is wrong")
#-----------10th programm-------#
num = int(input("input a number:"))
if num > 0:
    print("it is positive number")
else :
    print("it is a negative number ")