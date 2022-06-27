#Built_in functions
 #=>len()
 #=>upper()
#=>lower()
#=>in
#=>replace()
#=>find()
#=>title()
#=>count()
#=>isalpha()
#=>isnum()
#=>isalnum()
#=>lstrip()
#=>rstrip()


course="Welcome to Thundersoft"
print(len(course))   #22
print(course[0])     #W
print(course[0:])     #Welcome to Thundersoft
print(course[2:5])    #lco
print(course.upper())  #WELCOME TO THUNDERSOFT
print(course.find('T'))  #11
be=course.lower()
print(be)      #welcome to thundersoft 
print(course[-2:])   #ft
print(course[ :-2])   #Welcome to Thunderso
print(course[1::])    #elcome to Thundersoft 
print(course.find('Welcome')) # 0
print('Welcome' in course)   # True
print('welcome' in course)   #False =>w is lowercase
print('thundersoft' not in course) #True
print("Thundersoft" not in course)  #False
print('Thundersoft' in course)      #True
print(course.find('h'))          #12
print(course.replace('Welcome','Heartly Welcome'))  #Heartly Welcome to Thundersoft =>replace 'Heartly  Welocome' in 'Welcome' place
print('Karnataka' in course)  #False
print("Karnataka" not in course)  #True
print(course.replace('W','F'))  #Felcome to Thundersoft  =>replace 'F' in 'W' position
print(course.title())   #Welcome To Thundersoft  =>word starts with upper case letter
print(type(course))   #<class 'str'>
python="TATA PROJECT"
print(type(python))   #<class 'str'>
print(course.count('e'))  # 3   =>counnt repeated elements
print(course.count('m'))   #1
print(course.count('t'))    #2
print(course.isalpha())     #False
print(course.isalnum())     #False
coursy="    Hello Bangalore    "
print(coursy.lstrip())   #****Hello Bangalore----  =>remove left side space  (*)  
print(coursy.rstrip())   #----Hello Bangalore****  =>remove right side space (*)




