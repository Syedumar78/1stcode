#----What is the correct syntax to output the type of a variable or object in Python ?---------# 	
Syed_umar = 10
print(type(Syed_umar))
#---------------------------------#
_Syed_umar = 1.20
print(type(_Syed_umar))
#------------------#
_Umar = 'lasson'
print(type(_Umar))
#----Which method can be used to remove any whitespace from both the beginning and the end of a string ?---#
syedumar = "                            'assalamu-alaikum wahrahmatullahi wo barkatuhu'                     "
cleaned_syedumar = syedumar.strip()
print(cleaned_syedumar)
#-------------Which method can be used to return a string in upper case letters ?-------#
__name__ = "  'syed umar' "#
upper_aim = __name__.upper()
print(upper_aim)
#--------Which method can be used to return a string in lower case letters ?--------------#
_Icony = "'BGMI'"
lower_Icony = _Icony.lower()
print(lower_Icony)
#-----------Which method can be used to replace parts of a string ?-------------#
_Umariconic_ = " 'syed nawaz', 'syed muhit'"
_umariconic = _Umariconic_.replace('syed nawaz', 'syed umar',)
print(_umariconic) 
#--------------------tuples operations --------------------------------------------------------------------#
fruits = ('apple', 'banana', 'cherry', 'date')
print(fruits)
print( "first friuts:",   fruits[0])  
print("last fruits:", fruits[2])
print("number of fruits:", len(fruits))
print("All fruits:",)
for fruit in fruits:
    print(fruit)
if 'banana' in fruits:
    print("banana is in fruits", fruits[1])
    add_fruits = ('rasberry', 'kiwi')
total_fruits = (fruits + add_fruits)
print(total_fruits)

#get  ASCIIletters
#import string
#ascii_letters = string.ascii_letters + string.digits + string.punctuation
#acsii_letters = string.ascii_lowercase
#sacii_letters = string.ascii_uppercase
#ii_as = string.punctuation
#asiiic= string.digits
#print(ascii_letters)
#print(sacii_letters)
#print(acsii_letters)
#print(ii_as)
#print(asiiic)
