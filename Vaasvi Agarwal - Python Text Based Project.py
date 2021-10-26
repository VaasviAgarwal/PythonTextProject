#Python Text Based Project
#Menu driven program for all various basic Python Programs

"""Note the alignments are all made on IDLE so they might not look aligned on notepad as far as the spaces in the output and the comments here are considered - Vaasvi Agarwal"""

#importing all the libraries at the begining so they can be accessed through out the project
import math
import csv


"""The Menu that will be printed for the user after each iteration"""

def menu(): #function for printing the main menu of guideline programs when called to display it to the user
    print("\n\n*****************************************************************************************************************************************************************************")                                                                                                                                                                                             #extra line so that the output from user's choice is crearly visible
    print('Enter 1 for execution of expressions involving arithmetic, relational, logical operators.')
    print('Enter 2 for production of two patterns  \n*\n**\n***\nfor n lines and \n$$$$\n$     $\n$     $\n$$$$\nfor 5 lines')
    print('Enter 3 for a program to calculate the roots of a quadratic equation using suitable functions from math.h')
    print('Enter 4 for a python program to generate a table of sins, cosine and tangents for each value of x (variable x in range from o to 2pi in steps of (pi/4)')
    print('Enter 5 for a menu driven program to invoke functions to calculate the area of square, rectangle, circle and triangle using suitable assertions')
    print('Enter 6 for a python function that takes a number as an input from the user and compute its factorial (using recursions). Then find the sum of the n terms of the following series :1-1/1! + 1/2! - 1/3! + ..... + 1/n')
    print('Enter 7 for a python program with both iteractive and recursive implementation of python function to return nth terms of Fibonacci series')
    print('Enter 8 for a function that takes a number as an input and find its reverse and compute the sumof its digits')
    print('Enter 9 for a function that takes two numbers as an input parameters and returns their least common multiple')
    print('Enter 10 for a a function that takes number as an input and determine whether it is prime or not This function would be used to display all prime numbers till the provided number n')
    print('Enter 11 for a menu driven program using in-built string functions to do the following tasks. ')
    print("1 to look for a substring in the given string and returns its position.")
    print("2 to replace substring 'good' with 'best' in the given string.")
    print("3 to find all the substring in the string which are separated by delimited.")
    print("4 to convert the given text into title form.")
    print("5 to convert lowercase to uppercase and uppercase to lowercase in the given string.")
    print("6 to Exit")
    print('Enter 12 for a class STUDENT to store his/her name, roll number and marks in three subjects and class variable to store maximum of average marks of the class using constructor/ destructor to initialise/delete the values to data members and define following user defined function members:')
    print("• Display the member's values with average mark.")
    print("• Display the maximum average Marks of the students.")
    print('Enter 13 for a function that reads a text file and calculate the frequency of vowels.Use a variable of dictionary type to maintain the count.')
    print('Enter 14 for a Python function that prints a dictionary where the keys are numbers between 1 and 5 and values are cubes of the keys.')
    print('Enter 15 for tuple t1=(1,2,5,7,9,2,4,6,8,10).Write a program to perform following functions :')
    print('(a) Print half the values of tuple in one line and other half in the next line.')
    print('(b) Print another tuple whose values are even numbers in the given tuple.')
    print('(c) Concatenate a tupal t2 = (11,13,15) with t1.')
    print('(d) Return maximum and minimum value from the tuple.')
    print('Enter 16 for a menu driven program to do the following functions : \n•Selection sort \n•Insertion sort')
    print('Enter 17 for a menu driven program to do the following functions : \n•Linear search\n• Binary search')
    print('Enter 18 for a program to implement a class for finding area and perimeter of a rectangular playground. Write Constructor, destructor and functions for calculating area and perimeter')
    print('Enter 19 for a program to perform the following functionality using csv files.')
    print('• Create a csv files for maintaining student records containing name and total marks obtained.')
    print('• Read the file created above to display the details of every third student.')
    print('Enter 20 that performs the following functions using list :')
    print('•Find whether all elements in list are numbers or not.')
    print('•If numeric list then count number of odd values in it.')
    print('•If string list then display the largest string in this list.')
    print('•If all elements are string then count numeric string and string with alphabets only')
    print('Enter 21 for a program that accepts two things and perform the following using sets.')
    print('• Convert each string into separate set.')
    print('•Identify and display the common characters between the two sets.')
    print('•Identify and display the distinct characters between the two sets.')
    print('Enter 0 to exit the menu driven program')    #last option to come out of the loop when the user does not want to choose anymore
    print()                                                                     #extra line so that the output from user's choice is crearly visible
    #menu ends


"""Checking for different datatypes of values entered by the user as it would be needed in the future for many GP programs. It gives true when the value is not of
required datatype or style as when called in if loops it is better to first get the invalid statements out of the way and leave the loops instead of doing it at the end so we need those if conditions
to be true if the values are not not either of those things  [We initially think that the values are invalid and if they are not then it goes to do further things]"""

def checkfloat(n):  #function that check if a number is a float number using exception handling
    try:
        n = float(n)                                                         #trys to convert the element passed in the arguement
    except ValueError:
        return 1                                                             #if argument was a string value or any value which cannot be converted to float True will be returned as when checking we will go backwards
    else:
        return 0                                                             #if argument was a value  that can be converted to float False will be returned as when checking we will go backwards


def checkint(n):  #function that check if a number is a int number using exception handling
    try:
        n = int(n)                                                            #trys to convert the element passed in the arguement
    except ValueError:
        return 1                                                             #if argument was a string value or any value which cannot be converted to int True will be returned as when checking we will go backwards
    else:
        return 0                                                             #if argument was a value  that can be converted to int False will be returned as when checking we will go backwards


def checkwholenum(n):#function that check if a number is a positive integer value (A whole number) using if and else
    if n.isnumeric():
        return 0                                                              #returning false if our assumption about the value being invalid is False
    else:
        return 1                                                              #returning true if our assumption about it being invalid was True


"""Functions to create a lists of strings as it might be required in programs where we perform the sorting and searching of elements. It is string so in GP16 and GP17 everything will happen based on ASCII
values"""

def createlist():
    n = input('Enter the size of the list: ')                    #accepting the size of the array. Assuming the user enters a positive integer
    if checkwholenum(n):                                              #checking if the user entered an invalid entry ie. not a postive integer
        print('Invalid entry so list cannot be created for the required functions')                                                                      
        return 1                                                              #returning 1 so when we check if it is wrong it we give True
    if n == '0':                                                              #Checking if the user wants to give an empty list as that cannot be worked with
        print('Empty list cannot be used to perform functions upon')
        return 1
    print('Enter the elements')
    l = []                                                                        #creating an empty list initially
    for i in range(int(n)):                                               #till int(n) elements so it will go from 0 to n-1 which is also the indexing
        l.append(input())                                                   #creating the list using append function to add the elements entered by the user 
    return l                                                                    #returning the list


""" GUIDELINE PROGRAM 1
Execution of expressions involving arithmetic, relational, logical operators."""

def gp1(): #function that performs the operations in GP 1 which is to display the use of arithmetic, logical and relational operators (There is no seperate function as all the functions can be easily performed here
    print('Your choice is GUIDELINE PROGRAM 1 where the use of all operators will be displayed') #informing the user of their choice
    print('Arithmetic operators :-')                                #Displaying the use of arithmetic operators +, -, *, /, **, //, %
    print('5+11 = ',(5+11))                                                #Using addition operator 5 plus 11
    print('5-11 = ',(5-11))                                                 #Using subtraction operator 5 minus 11
    print('5*11 = ',(5*11))                                                #Using multiplaction operator 5 into 11
    print('5/11 = ',(5/11))                                                #Using division operator 5 divided by 11
    print('5//11 = ',(5//11))                                            #Using floor division operator 5 divided by 11 rounded off to nearest integer
    print('5**11 = ',(5**11))                                             #Using exponent/power operator 5 to the power of 11
    print('5%11 = ',(5%11))                                              #Using modulus operator 5 mode 11
    print('Relation operators :-')                                     #Displaying the use of arithmetic operators <, >, <=, >=, ==, !=
    print('5==11 = ',(5==11))                                             #Using equals to operator returns True if 5 is equal to  11 else False
    print('5!=11 = ',(5!=11))                                               #Using is not equals to operator returns True if 5 is not equal to 11 else False
    print('5<11 = ',(5<11))                                                 #Using is less than operator returns True if 5 is less than 11 else False
    print('5>11 = ',(5>11))                                                 #Using is greater than operator returns True if 5 is greater than 11 else False
    print('5<=11 = ',(5<=11))                                              #Using is less than or equal to operator returns True if 5 is less than or equal to 11 else False
    print('11>=11 = ',(11>=11))                                            #Using is greater than equal to operator returns True if 11 is greater than or equal to 11 else False
    print('Logical Operators :-')                                      #Displaying the use of logical operators and, or and not
    print('not True =', (not True))                                    #Using not operator which given the opposite answer ie, False for True and True for False
    print('not False =', (not False))
    print('True and True =', (True and True))                  #Using and operator which given True if and only if all conditions are True  or else it gives False
    print('True and False =', (True and False))
    print('False and True =', (False and True))
    print('False and False =', (False and False))
    print('True or True =', (True or True))                      #Using or operator which given False if and only if all conditions are False or else it gives True
    print('True or False =', (True or False))
    print('False or True =', (False or True))
    print('False or False =', (False or False))

       
"""GUIDELINE PROGRAM 2
Write a python function to produce following outputs :
(a) *
      * *
      * * *
      * * * *
      * * * * *
(b) $ $ $ $ $
      $           $
      $           $
      $           $
      $ $ $ $ $"""

def gp2pattern1(n):      #function to print the first pattern in GP 2 for argument n  passed in parameter
    print('Pattern 1')
    if n < 1 :                                                                       #telling user that their entry was invalid as its less than one
        print("A pattern for 0 rows is not possible ")
    else :
        for i in range(n) :                                                     #running it for less than i times so that we can print one * at the end to add a new line in end (maintains the rows)
            for j in range(i) :                                                 #loop to print the columns in the rows (till one less so that when last element in the row is printed outside the loop it can be ended with a new line
                print('*',end='')                                              #ending with '' to avoid going to next line
            print("*")                                                             #the last element of that row

def gp2pattern2():      #function to print the second pattern of GP 2 for 5 number of rows
    """This pattern will be correctly aligned if run on IDLE. For proof I have added the screenshot of only this output along with the other files because if opened on any other interpreter it will not be
    aligned. Sorry for the inconvinience"""
    print("Pattern will be aligned if run on IDLE. For proof I have attached a screenshot of it with the output's .py file")
    print('Pattern 2')
    for i in range(5) :                                                        #Printing the first row of the program
        print("$",end='')
    print()                                                                         #print statement so that next lines are not concatinated
    for i in range(3) :                                                        #to print the line with $ on the beginning and ending with space in between for 3 rows
        print("$",end='')                                                     #printing the $ in the beginning
        for j in range(7) :
            print(" ",end='')                                                   #printing the extra spaces so that it can align on my interpreter
        print("$")                                                                #printing the last dollar in those 3 lines
    for i in range(5) :                                                        #printing the last 5th row of the pattern
        print("$",end='')

def gp2():      #defining the function for GP2 which will call the pattern functions and be called when user chooses it
    print('Your choice is GUIDELINE PROGRAM 2 where the generation of the patterns \n*\n**\n***\nfor n lines and \n$$$$\n$     $\n$     $\n$$$$\nfor 5 lines will take place') #informing the user of their choice
    n = input('Enter the number of rows n you want in the first pattern (Please enter a postive integer greater than 0): ') #accepting the number
    if checkwholenum(n):                                                  #making sure the user enters a postive numeric value (will not check for 0) and will go to next line if user entered something wrong to display a message
        print('Invalid Entry')
    else:                                                                            #correct entry as far as datatype is concerned so calling pattern 1 function with int of n
        gp2pattern1(int(n))
    gp2pattern2()                                                             #calling for function with second pattern irrespectively as it is a static one


"""GUIDELINE PROGRAM 3
Write a python program to calculate the roots of a quadratic equation. Use suitable functions from math.h"""

def gp3():      #direct function to calculate the roots as no need for a seperate function because only one task is being performed
    print('Your choice is GUIDELINE PROGRAM 3 that solves a quadratic equation to find the roots using math.h funcitons') #informing the user of their choice
    print('Enter a, b, c for ax^2 + bx + c = 0 to find the roots of the equation : ') #accepting a b and c for ax^2 + bx + c = 0 (Entering any other datatype wil stop the program from executing)
    a,b,c= input("Enter a : "), input("Enter b : "), input("Enter c : ")                                                                                          
    if checkfloat(a) or checkfloat(b) or checkfloat(c):      #checking if value entered by the user is of correct datatype
        print('Invalid entry')
        return                                                                     #returning so further lines of gp3 cannot be executed
    a,b,c = float(a), float(b), float(c)                                  #since we have already checked that they can be converted to float we will just convert them for future calculations
    dis = (b*b) - (4*a*c)                                                    #finding discriminant
    if dis < 0 :                                                                   #if discriminant is less than zero then imaginary roots
        print("The roots will be imaginary and cannot be calculated")
    else :
        ur = math.sqrt(dis)                                                   #finding root of equation by using math library function for finding under root of discriminant
        root1= round( ((-b + ur)/2), 2)                                 #finding roots and rounding them off to 2 decimal places
        root2= round( ((-b - ur)/2), 2)
        print("The roots of the equation are",root1,"and",root2) #printing the answers


"""GUIDELINE PROGRAM 4
Write a python program to generate a table of sins, cosine and tangents. Make a variable x in range from o to 2pi in steps of (pi/4). For each value of x, print the value of sin(x), cos(x) and tan(x)."""

def gp4angle(n):            #function to find the angle in radians that returns the value of the angle passed in radians                                                                           
    return (n/180)*(22/7)

def gp4angdis(x):         #funciton to print the angle in terms of pi (ending all statements with tab for a tabular form
    if x%180==0:                                                               #for 0, 180 and 360 degreees
        print('(',x//180,')pi', sep='',end='\t')
    elif x%90==0:                                                              #for 90 and 270 degrees
        print('(',x//90,'/2)pi', sep='', end='\t')
    else:                                                                            #for 45, 135, 225 and 315 degrees
        print('(',x//45,'/4)pi', sep='', end='\t')

def gp4anstab(n):       #function that prints the value of sin, cos tan of the angle for till decimal value for angle n passed in the argument
    print(round(math.sin(n), 1), round(math.cos(n), 1), round(math.tan(n), 1), sep='\t') #tab used so the thing is printed in angular form

def gp4():          #function where all the required functions are called as an when necessary to perform the task in GP4 and this function will be finally called if the user chooses 4 in the main menu
    print('Your choice is GUIDELINE PROGRAM 4 where a trignometric table of sine, cosine and tangent will be printed. ') #informing the user of their choice
    print('angle x', 'sin(x)', 'cos(x)', 'tan(x)', sep='\t')    #first line is printing the headings (tab for distinct visibility                                                                                                             
    for x in range(0,361,45):                                             #using for loop to traverse with x as loop variable because of the question
        a = gp4angle(x)
        gp4angdis(x)
        gp4anstab(a)                                                            #function will print values for when tan is infinite because due to rounding off the value of x would never really be equal to 90 or 270 degrees
        

"""GUIDELINE PROGRAM 5
Write a menu driven program to invoke functions to calculate the area of square, rectangle,
circle and triangle. Use suitable assertions."""

def gp5menu():          #function that will print the menu of the GP5 when called
    print("Enter 1 if you want to calculate the area of a square")
    print("Enter 2 if you want to calculate the area of a rectangle")
    print("Enter 3 if you want to calculate the area of a circle")
    print("Enter 4 if you want to calculate the area of a triangle")
    print("Enter 0 if you want to exit GP5")

def gp5square() :       #function that returns area of a square of side entered by the user using appropriate assertions but will give an error if user does not enter a float or int value
    side = input("Enter the length of the square in : ")
    assert not checkfloat(side), 'Invalid datatype'           #asserting that the user enters correct datatype (not as the function was sending True if it was invalid)
    side = float(side)
    assert side>=0 , 'length entered is less than zero'      #asserting that the user does not enter a negative value as the length                                                                              
    print('Area of the square is', (side*side) , 'units')     #printing answer

def gp5rectangle():  #function that returns area of a rectangle of sides entered by the user using appropriate assertions but will give an error if user does not enter a float or int value
    length = input("Enter the length of the rectangle : ")
    breadth = input("Enter the breadth of the rectangle : ")
    assert not (checkfloat(length) or checkfloat(breadth)), 'Invalid entry'  #asserting not checkfloat as the funciton was returning True if value was invalid                                                                                                                                  
    length, breadth = float(length), float(breadth)
    assert length>=0 and breadth>=0  , 'invalid value entered as at least one of the sides entered is less than zero' #asserting that the user does not enter a negative value as the length and breadth
    print('Area of the rectangle is', (length*breadth) , 'units')   #printing answer

def gp5circle():        #function that returns area of a circle of radius entered by the user using appropriate assertions but will give an error if user does not enter a float or int value
    radius = input("Enter the radius of the circle : ")
    assert not checkfloat(radius), 'Invalid datatype'        #asserting that the user enters correct datatype (not as the function was sending True if it was invalid)
    radius = float(radius)
    assert radius>=0 , 'radius entered is less than zero'   #asserting that the user does not enter a negative value as the radius
    print('Area of the circle is', (radius*radius*(22/7)), 'units')  #printing answer

def gp5triangle():  #function that returns area of a triangle of base and height entered by the user using appropriate assertions but will give an error if user does not enter a float or int value
    height = input("Enter the height of the triangle : ")
    base = input("Enter the length of base of the triangle : ")
    assert not (checkfloat(height) or checkfloat(base)), 'Invalid entry'   #asserting not checkfloat as the funciton was returning True if value was invalid
    height, base = float(height), float(base)
    assert height>=0 and base>=0  , 'invalid value entered as at least one of the sides entered is less than zero'      #asserting that the user does not enter a negative value as the height and 
    print('Area of the triangle is', (height*base*0.5) , 'units')       #printing answer

def gp5():              #function that calls all the supporting functions for gp5 as and when required and will be called when the user chooses 5 in the main menu
    print('Your choice is GUIDELINE PROGRAM 5 where you will be given a menu of shapes of whose area you want to be calculated. ')  #informing the user of their choice
    choice = 99                                                                 #putting choice ourselves 99 to go into the while loop
    while choice!='0':                                                        #while user does not want to quit
        gp5menu()                                                               #printing the menu the first time so that user can make his choice
        choice = input('Enter your choice : ')                       #accepting the choice
        if choice == '1':                                                       #comparing choice as string itself so no issue in conversion and if user enters another datatype by mistake
            gp5square()
        elif choice == '2':
            gp5rectangle()
        elif choice =='3':
            gp5circle()
        elif choice =='4':
            gp5triangle()
        elif choice == '0':
            pass                                                                    #as we do not want to print the invalid entry statement but also not perform any other function
        else:
            print('Invalid Entry')
        print()                                                                     #printing empty line to differentiate the run of each iteration
    print('GP5 terminated as you entered 0')                    #terminating the loop and informing the user


"""GUIDELINE PROGRAM 6
Write a python function that takes a number as an input from the user and compute its factorial (using recursions). Then find the sum of the n terms of the following series :
1-1/1! + 1/2! - 1/3! + ..... + 1/n"""

def gp6fact(n):        #recursive function for calculating the factorial of a number
    if n==1:
        return 1                                                                   #the factorial will be calculated be multiplying the numbers backwards unlike that in for loop
    return gp6fact(n-1)*n

def gp6pn(n) :     #function to see if the factorial should be postive or negative
    if n%2==0 :
        return 1                                                                  #the function returns 1 if the number passed is even and -1 if the number passes is positive
    return -1                                                                     #the value returned by the function can be multiplied in the value that will be added to the series

def gp6():         #function which will calulate the answer to the series by calling the supporting functions and will be called when user choosed gp6 to be performed
    print('Your choice is GUIDELINE PROGRAM 6 where the factorial of a number and the sum of the series 1-1/1! + 1/2! - 1/3! + ..... + 1/n will be calculated')  #informing the user of their choice
    n = input("Enter the n value of n which is greater than or equal to 0 : ")
    if checkwholenum(n) :                                                 #if the user has entered a value less than 0 or not int then there will be a message displayed explaining
        print("Invalid value of n entered")                           #return statement will bring us out of the main function so that no further code will be run
        return
    n = int(n)
    s = 1.0                                                                         #sum is equal to 1 initially so that the loop only needs to calculate the factorials starting from 14                                                                                                                                                                                                                                    
    for i in range(1,n+1):                                                    #loop starts from 1 as we do not need to calculate the factorial for 0th term and if the value of n = 0 then the answer will be 1
        s = s + ( ( 1 * gp6pn(i) ) / gp6fact(i) )
    print('Answer =',s)


"""GUIDELINE PROGRAM 7
Write both iteractive and recursive implementation of python function to return nth terms of
Fibonacci series."""

def gp7iter(n): #function to print the finbonnaci series for n terms using iteration
    print("The result without recursion is")
    if n < 1 :                                                                      #cannot print a series for 0 or less terms therefore invalid entry
        print("Invalid entry")
    elif n == 1 :                                                                  #since only one term, no calculation possible so printing the first term we know the answer of
        print('0')
    elif n == 2 :                                                                 #since only 2 terms, no caluclation possible so printing the first two terms we know the answer 
        print('0\t1',end='')
    else :
        a = 0                                                                        #first term  stored in a so initially zero
        b = 1                                                                        #second term stored in b so initially one
        print('0\t1',end='')                                                 #printing the first two terms so the series can be printed from the next term
        for i in range(2,n) :                                                  #first two terms already printed so starting at two as 2 will be included and n will not be included making the total terms being printed n-2
            c = a+b                                                                 #in fibonnaci series every term from third term is sum of the preivous two terms therefore c = a+b
            print('\t',c,end='')                                              #printing the term c
            a = b                                                                    #updating the value of a to the next term (b for that iteration)
            b = c                                                                    #updating the values of b to the next term(c for that iteration)
    print()                                                                          #printing a blank statement so next statement is printed in a new line as before this we were ending each print with '' to keep it in the same line

def gp7rec(n): #function in which a recursive function to print the fibonnaci series will be defined which will be called in the final program for gp7
    print("The result with recursion is")
    def fib(a,b,c,m) :      #recursive function to print the fibonnaci series
        if m<1 :                                                                    #if number of terms passed are less than 1 intitally then invalid entry
            print("Invalid entry")
            return                                                                 #returning as no need to perform future lines
        if c>m :                                                                    #base conditon. c is the count of terms that has being printed 
            return                                                                                  
        print(a,end='\t')                                                     #printing the term a (initally the first term and then goes on)
        b = a+b                                                                    #term after 0 for the next recursion would be sum of itself and a
        a = b-a                                                                     #updating the value of a to the preivous value of b
        return fib(a,b,c+1,m)                                               #recursion
    fib(0,1,1,n)                                                                  #calling the function the first time where first term a = 0, second term b = 1, the first time term will be printed so c = 1 and n is number of terms needed

def gp7(): #function that will be called when GP 7 will be chosen by the user and is calling the supporting programs as and when required
    print('Your choice is GUIDELINE PROGRAM 7 where the fibonnaci series for n terms will be printed recursively and iteratively (i.e. two times)') #informing the user of their choice
    n = input('Enter the number of terms n [postive integer value] : ')
    if checkwholenum(n):                                                   #checking if user did not enter a positive integer value
        print('Invalid Entry')
        return                                                                     #returning so rest of the lines of GP 7 cannot be printed
    gp7iter(int(n))                                                             #converting the value to n and then passing
    gp7rec(int(n))


"""GUIDELINE PROGRAM 8
Write as function that takes a number as an input and find its reverse and compute the sum of its digits."""

def gp8fun(n) : #function that performs the operations of reversing and computing the sum of digits that are mentioned in the option
    if n<0 :                                                                        #if number is negative we will store a copy of its positive version in a to compute the answer eg |-2| = -2-(-2*2) = -2 + 4 = 2
        a = n-(2*n)
    else :
        a = n                                                                        #if the number is positive then the copy will store itself only
    r = 0                                                                            #initializing the sum and reverse at 0         
    s = 0
    while a > 0 :                                                                 #the loop will go till |n|=a>0 as the digits will be extracted for reverse and sum from there only
        r = (r*10) + (a%10)                                                   #calculating the reverse of of the number it will work like if a = 87 for iteration 1, 0*10+87%10 = 0+7 =7 then a = 8 so for next iteration 7*10+8%10 = 70+8 =78
        s = s + (a%10)                                                          #caluctlating the sum like a = 87, for iteration 1, 0+87%10 = 0+7 then a//10 = a =8 so for next iteration 7+8%10 = 7+8 =15
        a = a//10                                                                 #updating the value of a after last digit it will be 0 after which the loop will end
    if n < 0 :
        r = -r
    print("reverse of the number is",r)
    print("sum of the digits of the number is",s)

def gp8(): #function that calls the function defined for GP8 by passing the parameters it receives as an input from the user
    print('Your choice is GUIDELINE PROGRAM 8 where a function is defined that reverses the number and finds the sum of its digits that is passed in the parameter')                                          #informing the user of their choice
    n = input('Enter an integer number n : ')
    if checkint(n):                                                             #checking if the value entered by the user is not an integer value
        print('Invalid entry')
        return                                                                     #returning so next statement is not executed if invalid input is given
    gp8fun(int(n))                                                              #calling the function defined for as per the instruction in the program with int of the input given as we already know that the input can easily be converted to int


"""GUIDELINE PROGRAM 9
Write a function that takes two numbers as an input parameters and returns their least common multiple."""

def gp9lcm(x, y) : #function that is asked to be defined in the question for GP9 which returns the lcm of the two numbers passed as its  parameters
    if x<1 or y<1 :                                                              #checking if the number is 0 because we already checked in the main function if the element was a whole number and the only whole number whose lcm cannot be calculated is 0
        return 'At least one of the numbers you entered was 0 so no LCM can be calculated'
    else :                                                                           #since we know that he numbers number is eligible we find the lcm
        ans = 1                                                                     #answer starts at 1 as the number could also be 1 and 1 and then it can keep incrementing if ans is not the lcm 
        while True :                                                            #while loop will run till the time the lcm is not found
            if ans%x==0 and ans%y==0 :                                #if both the numbers are completely divisibe by ans (mode is 0 for both) then ans will be the lcm
                return ans                                                       #returning ans as it is the lcm because both numbers are divisible by it completely
            ans=ans+1                                                            #since ans was not the lcm for that iteration it is incremented by 1

def gp9(): #function that calls the lcm function that has to be written for GP9. This function will be called when the user chooses 9 from the main menu
    print('Your choice is GUIDELINE PROGRAM 9 where a function is defined that returns the lcm of the numbers entered by the user') #informing the user of their choice
    print('Enter the integer numbers x and y  greater than 0 that you want to find the lcm of')
    x, y = input(), input()
    if checkwholenum(x) or checkwholenum(y):                 #checking if the number is not a whole number and not a negative integer or is something that does not belong to the int datyape
        print('Invalid entry as LCM can only be taken out of two whole numbers')
        return                                                                     #returning so that the next statement is not reached and the control goes back to where the main menu was
    print('The LCM of the numbers entered by you is:', gp9lcm(int(x), int(y)) )


"""GUIDELINE PROGRAM 10
Write a function that takes number as an input and determine whether it is prime or not. Use this function to display all prime numbers till the provided number n."""

def gp10prime(m) :      #function that has been asked to be defined in the program which returns True if the number passed in the parameter is prime else it returns False
    a = 1                                                                            #a is the number which will be checked if it is a factor of m
    c = 0                                                                            #c is the count of factors and has been initalized to 0 and will increment as 
    while a <= m :                                                               #while loop will stop as soon as a is greater than m as a number cannot be another number's factor if it is greater than it
        if (m%a)==0 :                                                           #if the remainder on dividing m by a is 0 then it is a factor
            c = c+1                                                                 #if a is a factor then c will increase
        a = a+1                                                                     #a will increase so the next number can be checked
    if c == 2 :                                                                    #if a number has exactly 2 factors( therefore cannot be one as it has only 1 factor) then it is a prime number so if m has only 2 factors it returns True
        return True
    else :                                                                           #else since the number does not have exactly two factors(1 and itself) the function returns False
        return False

def gp10(): #function that calls the prime function wrttien for gp10 to print all he numbers till n that are prime. This function will be called when the user chooses 10 from the main menu
    print('Your choice is GUIDELINE PROGRAM 10 where a function is defined that returns if a number is prime or not and then is used to print all the list of all the prime number till n') #informing the user of their choice
    n = input("Enter a natural number n : ")
    if checkwholenum(n) :                                                  #checking if the user entered something invalid and if does a message is displayed after which the fuction is returned so future statements cannot be checked
        print("Your entry is invalid")
        return                                                                                                                              
    if int(n)<1:                                                                    #since we already know that the number is a positive numeric number as the function did not get returned after the first condition
        print('0 is not a natural number')                             #0 is not a natural number so it is not a valid entry. Thus, message is dispalyed and the function is returned so future statements cannot be checked
        return
    print("The list of all prime numbers till",n,"are :")        #printing a statement to distinguish user entry from list of prime number going to be printed
    for i in range(1,int(n)+1) :                                             #till int(n)+1 as otherwise the last number will not be included. From 1 as we do not consider 0. int(n) as before this n was a string
        if gp10prime(i) :
            print(i)


"""GUIDELINE PROGRAM 11
Write a menu driven program using in-built string functions to do the following tasks. Menu should be displayed and user must be promoted to enter choice. Repeat this sequence till user enters exit option.
MENU
1. Look for a substring in the given string and returns its position.
2. Replace substring 'good' with 'best' in the given string.
3. Find all the substring in the string which are separated by delimited.
4. convert the given text into title form.
5. Convert lowercase to uppercase and uppercase to lowercase in the given string.
6. Exit"""

def gp11pos():      #function to find the position entered by the user  and will give the answer as the position and not the index number
    s = input("Enter the string in which substring wil be looked for : ")
    a = input("Enter the substring we are looking for : ")
    x = 1+s.find(a)#using find function to find the substring as it will give 0 incase of not present which will be easier to work with when displaying postion and +1 as we want to print the position not the index number
    if x == 0 :                                                                                                                                         
        print("The substring entered by you is not present")
        return
    print("The substring is present at postition(not the index number) is",x)

def gp11rep():      #function to replace good with best in the given string and if good is not present in the string given then a message will be displayed
    s = input("Enter the string which you wish to be updated : ")
    if s.find('good')==-1 :                                                  #checking if the word good is not present in the string because if so then find would return -1
        print("The string that you entered does not have 'good' in it")
        return                                                                     #returning so the next statements in this particular function are not executed
    print("The updated string is :")
    print(s.replace('good','best'))                                     #replacing all the good in the statement with best using replace method

def gp11seperate():     #function to split the string into parts with split and partition functions
    a = input("Enter the string that needs to be split : ")
    b = input("Enter the delimited part or the string from which it has to be seperated : ")
    if a.find(b)==-1:                                                           #informing the user if the substring entered by them is not a part of the string as find returned -1
        print("The delimited part is not present in the string")
        return                                                                     #returning so next statements of the function are not executed
    print("The answer through split function is :", a.split(b)) #using split function to split the string a with the delimiter b
    print("The answer through partition function is :", a.partition(b))#using partition function to split the string a with the delimiter b

def gp11contit():       #function that accepts a string and prints its titilized version
    s = input("Enter the text you want to be converted into title form : ")
    print("The title form of the text entered by you is :")
    print(s.title())                                                              #titilizing the function title and printing it

def gp11loupp():        #function to accept a string and swap the cases of all its characters
    s = input("Enter the string in which you want the cases to be swaped : ")
    print("The answer with swapped cases is :")
    print(s.swapcase())                                                      #swapping the cases of all the characters of a string using swap function

def gp11invalid():      #a function to tell the user that he has entered an invalid value as a choice when it is called
    print("Invalid entry")

def gp11menu():       #a function that prints the menu to be given under the GP11 program everytime it is called       
    print("Enter the number next to operation you wish to perform")
    print("1 to look for a substring in the given string and returns its position.")
    print("2 to replace substring 'good' with 'best' in the given string.")
    print("3 to find all the substring in the string which are separated by delimited.")
    print("4 to convert the given text into title form.")
    print("5 to convert lowercase to uppercase and uppercase to lowercase in the given string.")
    print("6 to Exit")

def gp11():     #The function where all the supporting functions are being called as and when required based on the choices made by the user. This it the function that will be called if the user chooses GP11 from the main menu
    print('Your choice is GUIDELINE PROGRAM 11 where the functions based on your choices you will make from the future menu will be performed using appropriate string functions. This process will be repeated till the time you choose Exit option') 
    while True :                                                                #So that the loop does not terminate until and unless done from inside using break, return or any other appropriate means
        gp11menu()                                                              #Calling the function that will display the menu for the user each time
        choice = input('Enter you choice: ')                         #keeping the choice in string form as it will be easier to manage incase the user enters anything other than the required choices          
        if choice == '1' :                                                      #Calling the functions based on the choices made by the user each time
            gp11pos()
        elif choice == '2' :
            gp11rep()
        elif choice == '3' :
            gp11seperate()
        elif choice == '4' :
            gp11contit()
        elif choice == '5' :
            gp11loupp()
        elif choice == '6' :                                                  #if the user entere 6 then the main function will be terminated using the return statement to leave the function after a statement telling why
            print("GP12 has been terminated/exited as you entered 6")
            return
        else :
            gp11invalid()
        print()                                                                     #printing an empty line so that everytime the menu is printed again it can be distinguished based on the previous output


"""GUIDELINE PROGRAM 12
Define a class STUDENT to store his/her name, roll number and marks in three subjects and class variable to store maximum of average marks of the class. Use constructor/ destructor to
initialise/delete the values to data members and define following user defined function
members:
• Display the member's values with average mark.
• Display the maximum average Marks of the students."""

class STUDENT:      #class student with functions and class variables that will be called
    maxam=0                                                                     #initializing the maximum average marks, maxam at 0
    def __init__(self, name, roll, hindi, english, maths):   #initializing the values by defining the constructor
        self.name=name                                                       #using the self keyword to initialize and the values
        self.roll=roll
        self.marks=dict([('Hindi',hindi), ('English',english), ('Maths', maths)]) #creating a dictionary to store marks
    def __del__(self):                                                      #creating a destructor
        print('The destructor is called for ',self)
    def disbmem(self):                                                      #function to display the values member wise
        print(self.name, self.roll, self.marks['Hindi'], self.marks['English'],  self.marks['Maths'], sep='\t', end='\t') #printing the values for this student (tab used for proper distinction)        
        self.am = sum(self.marks.values())/len(self.marks.values()) #calculating average marks by dividing the sum of all values of marks by its len
        print(self.am)                                                          #printing the average marks of that object
        if type(self).maxam<self.am:                                    #updating the value of maximum average marks if it is less than the average marks we just saw
            type(self).maxam=self.am
#class ends

def gp12dismax():                                                           #function to display the maximum average marks (function out side the class) by accessing the class variable
    print('Maximum average marks out of all the students:', STUDENT.maxam)

def gp12(): #function in which the objects of the STUDENT are formed and deleted as well as all the other required functions are called to generate the output according to the question
    print('Your choice is GUIDELINE PROGRAM 12. Where a class STUDENT will be created with the given methods and the average marks of students along with their roll number, names and marks in each subject will be displayed als well as the maximum average marks out of all the students will be displayed') #informing the user about their choice
    n = input('Enter number of students: ')
    if checkwholenum(n):                                                   #checking if the user did not enter a whole number only and if so then the function is returned so it further statements are not executed
        print('Invalid number of students entered so GP12 will not be executed in this iteration')
        return
    if int(n)==0:                                                                 #if the number of students is 0 then no objects will be created and the function will be returned
        print('No students so no objects, table or maximum average')
        return
    l = []                                                                            #creating empty list to pass
    print('Enter values with correct datatypes in each case because if not then the moment a wrong datatype is entered GP12 will stop executing')
    for i in range(1, int(n)+1):                                             #for loop from 1 to n+1 as n+1 will be excluded and the loop is made to accept the details of the student
        name = input('Enter name of the Student%s: '%i)
        roll = input('Enter roll number of the Student%s: '%i)#No check for Roll Number as Roll Number can also have alphabets
        hindi = input('Enter the Hindi of the Student%s: '%i)
        english = input('Enter the English of the Student%s: '%i)
        maths = input('Enter the Maths of the Student%s: '%i)
        if checkwholenum(hindi) or checkwholenum(english) or checkwholenum(maths):  #checking the marks were not postive integers and returning so this execution of gp12 is terminated
            print('Since, marks were entered which were not positive integers the GP12 will be terminated and the other functions will not be performed')
            print('Destructors being called for the previous objects already been created')
            for i in l:                                                             #loop to call the destructor for each object in the list  that had already been created to end the list                                                                                                                                                                                           
                del i
            return                                                                 #return so futher lines of gp12() will not be performed
        l.append(STUDENT(name, roll, int(hindi), int(english), int(maths)))  #since the values are correct creating the the object for that student and appending it in list
    print('Name','Roll No.', ' Hindi', 'English', 'Maths', 'Average', sep='\t')  #printing the first line for the table (using tab for proper distinction) 
    for i in l:                                                                     #for loop in l for displaying the details of each student through the method of class 
        i.disbmem()
    gp12dismax()                                                              #displaying the maximum average marks
    for i in l:                                                                     #loop to call the destructor for each object in the list                                                                                                                                                                                            
        del i


"""GUIDELINE PROGRAM 13
Write a function that reads a text file and calculate the frequency of vowels.Use a variable of dictionary type to maintain the count."""

def gp13fileh():    #function that reads a text file and calculates the frequency of the vowels in that file and returns the counts stored in the form of a dictionary
    obj = open('GP13supportfile.txt','r+')                         #opening the file using r+ mode
    vl={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}                                #creating a dictionary with variable names as keys and initially has the count 0 for each
    x = obj.read()                                                              #reading the file using read function
    print(x)                                                                       #printing x to make sure that it contains a readable copy of the file
    for i in x:                                                                    #loop traversing through x character by character to calculate the frequency
        if i == 'a' or i == 'A':                                               #comparing each character stored in i and if it is a vowel then increasing the count in the value of that vowe's key
            vl['a']+=1
        if i == 'e' or i == 'E':
            vl['e']+=1
        if i == 'i' or i == 'I':
            vl['i']+=1
        if i == 'o' or i == '0':
            vl['o']+=1
        if i == 'u' or i == 'U':
            vl['u']+=1
    return vl                                                                     #returning the dictionary that contains the frequency of the vowels

def gp13():         #function called when the user choose GP13. It calls the function that reads a text file and calculates frequency of vowels in it ( A static program as the file is entered by the programmer so no user input)
    print('Your choice is GUIDELINE PROGRAM 13 in which a text file will be read and the frequency of the vowels in it will be displayed')  #informing the user about their choice
    d = gp13fileh()                                                            #d stores the returned by the function created according to the class that contains the frequency of the vowels
    print('The frequency of the vowels')
    print('"a" comes in the file', d['a'], 'many times')       #printing the values separetly for a clearer output
    print('"e" comes in the file', d['e'], 'many times')
    print('"i" comes in the file', d['i'], 'many times')
    print('"o" comes in the file', d['o'], 'many times')
    print('"u" comes in the file', d['u'], 'many times')


"""GUIDELINE PROGRAM 14
Write a Python function that prints a dictionary where the keys are numbers between 1 and 5 and values are cubes of the keys."""

def gp14cubes():        #function that perform the task of printing a dictionary where the keys are values from 1-5 and values are their cubes
    d = {}                                                                           #declaring an empty dictionary
    for i in range(1,6):                                                       #creating a for loop where i goes from 1 to 5 and we have 6 as last value is exculeded  
        d.update({i:(i**3)})                                                   #updating or adding a key value pair to the dictionary each time
    print('The dictinary having number from 1  to 5 as the keys and their cubes as their values :')
    print(d)                                                                       #printing the final dictionary

def gp14():                  #function that will call the function in which the dictionary is created and which will be called when user choose GP14 (static as no input is needed from the user)
    print('Your choice is GUIDELINE PROGRAM 14 in which a dictionary with number 1-5 their keys and their cubes their values will be created in a function')#informing the user about their choice
    gp14cubes()                                                                 #fucntion defined in the program being called


"""GUIDELINE PROGRAM 15
Consider a couple t1=(1,2,5,7,9,2,4,6,8,10). write a program to perform following functions :
(a) Print half the values of tuple in one line and other half in the next line.
(b) Print another tuple whose values are even numbers in the given tuple.
(c) Concatenate a tupal t2 = (11,13,15) with t1.
(d) Return maximum and minimum value from the tuple."""

def gp15createt1():      #function to create and return the static tuple written in the quesiton tuple 
    return (1,2,5,7,9,2,4,6,8,10)

def gp15displayhalf(t1):        #function to print halg of the values of the tuple in one line and other in next line
    n = (len(t1))//2                                                            #finding length of the tuple and halving it (floor division as we need integer value)
    print('Answer to part (a) is:')
    for i in range(n):                                                         #loop to print in first line till n(value at n will be excluded)
        print(t1[i], end='\t')                                               #ending with tab to separate the values for clear visibility
    print()                                                                         #printing a blank line after the loop so that next line prints on a new line
    for i in range(n,len(t1)):                                               #loop to print the second line from n to len(t1)
        print(t1[i], end='\t')
    print()                                                                         #printing a blank line after the loop so that the next line prints on a new line

def gp15eventuple(t1):      #a function creating and printing a new tuple with even values of old tuple
    t = ()                                                                           #creating a new empty tuple initially
    for i in t1:                                                                   #loop in t1 so that the values in t1 can be traversed to look for its even values
        if i%2==0:                                                               #if i is even then appending that value to the new tuple t                                                                                                                                                     
            t = t+(i,)
    print('The tuple with even elements of t1 is:')                                                                                                     
    print(t)                                                                        #printing the new tuple

def gp15concat(t1):      #concatenating two tuples (both are static tuples)
    t2 = (11, 13, 15)                                                            #creating the second static tuple as given in the question
    t1 = t1+t2                                                                     #concatinating them using the + operator
    print('The concatinated tuple is:')
    print(t1)                                                                      #printing t1 as the new concatinated tuple in the function(only inside the body of the function is it updated as it is not being returned and saved anywhere)

def gp15maxmin(t1):   #finding and returning the maximnum and minimun values from the t1 (first static tuple created for g15) and also the static tuple created in the function before this after concatinating the two
    return (max(t1), min(t1), max(t1+(11,13,15)), min(t1+(11,13,15) ))  #returning the values in a tuple so that it can returned at once (max and min values found using the inbuilt functions)

def gp15():         #function that calls all the supporting functions to execute GP15 task in order. This function will be called if user chooses GP15. All tuples in this GP are static so no user input taken
    print('Your choice is GUIDELINE PROGRAM 15 functions the following function will be performed in the given order on a tuple t1=(1,2,5,7,9,2,4,6,8,10) ') #informing the user about their choice
    print('(a) Print half the values of tuple in one line and other half in the next line.')
    print('(b) Print another tuple whose values are even numbers in the given tuple.')
    print('(c) Concatenate a tupal t2 = (11,13,15) with t1.')
    print('(d) Return maximum and minimum value from the tuple.')
    t1 = gp15createt1()                                                      #The tuple created in the first function saved as t1
    gp15displayhalf(t1)                                                      #the next 3 function are not returning anything so they need not be saved (Called in the order given in the quesiton) 
    gp15eventuple(t1)
    gp15concat(t1)
    mm = gp15maxmin(t1)                                                   #since maximum and minimum values are being returned as a tuple they need to be printed seperately so they are stored in a separate variable (mm contains the tuple with max value at 0 and 2 index and min value at 1 and 3index)
    print('maximum value of intial tuple t1:',mm[0])
    print('minimum value of initial tuple t1:', mm[1])
    print('maximum value of new tuple t1 (formed after concatinating with t2):',mm[2])
    print('minimum value of new tuple t1 (formed after concatinating with t2):', mm[3])


"""GUIDELINE PROGRAM 16
Write a menu driven program to do the following functions :
•Selection sort
•Insertion sort"""

def gp16menu():         #function to display the menu of GP 16 each time it is called
    print()                                                                         #empty lines before and after the menu for clear distinction
    print('Enter 1 for sorting a list in ascending order according to their ASCII values using selection sort')
    print('Enter 2 for sorting a list in ascending order according to their ASCII values using insertion sort')
    print('Enter 0 to exit')
    print()

def gp16selectionSort(l):       #creating a selection sort function on the list passed as the argument
    print('Unsorted List:',l)
    print('Peforming Selection Sort to sort it in ascending order according to the ASCII values:')
    for i in range(len(l)):                                                    #first function in range len(l) so last index is len(l)-1 is excluded to avoid error
        m = i                                                                        #assuming that the value at i is initially less than all the values after it in the list so putting that as the min index
        for j in range(i+1, len(l)) :                                        #running a loop on all the values in the list after the one at the current index 
            if l[j]<l[m]:   #since we are sorting in ascending order we are checking for values < l[m] and updating m, if we were sorting in descending order we would look for values > l[m] to update m
                m = j                                                                #if l[j] is less than l[m] then we will update m. That means m will be the index at which the minimum values in the sublist from i to len(l) is stored
        l[i], l[m] = l[m], l[i]                                                  #once the whole loop is traversed we will exchange value at l[i] and l[m]
        print('Pass -->',i+1,l)                                                #printing list after each iteration
    print('Sorted list in ascending order according the ASCII values is:',l, sep='\n')  #printing the sorted list

def gp16insertionSort(l):       #creating an insertion sort function on the list passed as the orgument
    print('Unsorted List:',l)
    print('Peforming Insertion Sort to sort it in ascending order according to the ASCII values:')
    for i in range(1, len(l)):                                                #funciton starting at 1 and ending at len(l)-1 (first element not accessed with i) because we will use i-1 and it migh cause index out of bound kind of error
        key = l[i]                                                                 #element at i is the key for this iterarion
        j = i - 1                                                                    #j is the index right before i
        while j >= 0 and key < l[j]:                                        # Compare key with each element on the left of it until an element smaller than it is found and for descending order, change key<l[j] to key>l[j].
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = key                                                            # Place key at after the element just smaller than it.
        print('Pass-->',i,l)                                                    #printing list after each iteration
    print('Sorted list in ascending order according the ASCII values is:',l, sep='\n') #printing the sorted list

def gp16(): #function that calls the sorting functions based on user's choices. This function will be called when the user chooses GP16
    print('Your choice is GUIDELINE PROGRAM 16 where you will be given a menu for sorting and you will make choices on what to do till the time you choose the exit options') #informing the user about their choice
    while True:                                                                 #so loop will end only when done so from inside
        gp16menu()                                                             #printing the menu
        choice = input('Enter your choice :')                       #accepting choice as string itself
        if choice == '1':
            l = createlist()                                                     #creating the list using the function defined at the beginning of the project
            if l==1:                                                                #checking if l was not created due to invalid n entered in the function.
                continue                                                          #if invalid list then continue to go to the next iteration without executing the next statements for this iteration
            gp16selectionSort(l)                                            #since correct list calling selection sort method
        elif choice == '2':
            l = createlist()                                                     #creating the list using the function defined at the beginning of the project
            if l==1:                                                                #checking if l was not created due to invalid n entered in the function.
                continue                                                          #if invalid list then continue to go to the next iteration without executing the next statements for this iteration
            gp16insertionSort(l)                                            #since correct list calling insertion sort method
        elif choice == '0':                                                   #if choice 0 returning the function after printing a statement so the control leaves the function gp16
            print('GP 16 terminated as you chose 0')
            return
        else:
            print('Choice not given')

        
"""GUIDELINE PROGRAM 17
Write a menu driven program to perform the following using functions :
•Linear search
• Binary search"""

def gp17menu():         #function that prints the menu of gp17 everytime it is called
    print()                                                                         #empty lines before and after the menu for clear distinction
    print('Enter 1 to search an element in a list entered by you using Linear Search')
    print('Enter 2 to search an element in a list entered by you using Binary Search')
    print('Enter 0 to exit')
    print() 

def gp17linearsearch(l): #function with the linear search algorithm on the list passed, where the element will be accepted in it. Everything will be in the default datatype of string so there is no issue in comparison
    s = input('Enter the character that you want to search: ') #accepting the element that need to be looked for
    f = 1                                                                            #putting flag in case the element is not found
    for i in range(len(l)):                                                   #for searaching we will have a for loop for the length of len(l) so that we can count when the element was found 
        if l[i]==s:
            print('The element found at index number:',i)
            f = 0
            break                                                                  #breaking so that if the element is found then it need not iterate again
        print('The element not found at index number:',i)
    if f :                                                                            #if the value of i is equal to len(l) then the element was not present in the list
        print('The element was not found')

def gp17checksort(l):   #checking if the user entered a sorted list and return true or false based on it. f will be returned 1 if not sorted, 0 if sorted
    f = 0                                                                            #initially we are assuming that the user entered a sorted list                                                                                                                                                                    
    for i in range(len(l)-1):                                                 #excluding the last index from loop to avoid out of bound exception
        if l[i]>l[i+1]:
            f = 1
            break                                                                  #if even 1 previous value is greater than the next value it will give false
    return f

def gp17binarysearch(l):    #Function with binary search algorithm on the list passed, where the element will be accepted in it. Everything will be in the default datatype of string so there is no issue
    el = input('Enter the element to be searched: ')          #accepting the element (keeping it as string)
    low = 0                                                                        #putting low and high values initially as the very extremes of the values of the indexes
    high = len(l)-1
    while low <= high:                                                        #loop till high is greater than low
        print('Low is',low,'and High is',high)                      #printing the flow
        mid = low +(high-low)//2                                         #calculating the middle index using floor so its a int value not float and high-low because it could be later as well
        if l[mid]==el:
            print('The element found at index number',mid)
            return                                                                 #ending the function here itself as the element is found
        elif l[mid]<el:                                                           #if element is greater than mid value, in the next iteration it will look in the second half
            low = mid+1
        else :                                                                       #if element is less than mid value, in the next iteration it will look in the first half
            high = mid-1
    print('Element is not found in the list')                       #if no value is returned even after the loop and the loop its looked through completely it means element not in the list

def gp17():         #function that calls the soearchin functions based on user's choices. This function will be called when the user chooses GP16
    print('Your choice is GUIDELINE PROGRAM 17 where you will be given a menu for searching and you will make choices on what to do till the time you choose the exit options')     #informing the user about their choice
    while True:                                                                 #so loop will end only when done so from inside
        gp17menu()                                                             #printing the menu
        choice = input('Enter your choice :')                       #accepting choice as string itself
        if choice == '1':
            l = createlist()                                                     #creating the list using the function defined at the beginning of the project
            if l==1:                                                                #checking if l was not created due to invalid n entered in the function.
                continue                                                          #if invalid list then continue to go to the next iteration without executing the next statements for this iteration
            gp17linearsearch(l)                                             #since correct list calling linear search method
        elif choice == '2':
            print('Binary search only works on sorted list so please enter a list sorted in ascending order in accordance to the ASCII values of the elements')
            l = createlist()                                                     #creating the list using the function defined at the beginning of the project
            if l==1:                                                                #checking if l was not created due to invalid n entered in the function.
                continue                                                          #if invalid list then continue to go to the next iteration without executing the next statements for this iteration
            if gp17checksort(l):
                print('The list entered by you is not sorted in ascending order in accordance to the ASCII values of the elements')
                continue                                                          #if invalid list then continue to go to the next iteration without executing the next statements for this iteration
            gp17binarysearch(l)                                            #since correct list calling insertion binary search method
        elif choice == '0':                                                    #if choice 0 returning the function after printing a statement so the control leaves the function gp16
            print('GP 17 terminated as you chose 0')
            return
        else:
            print('Choice not given')


"""GUIDELINE PROGRAM 18
Write a program to implement a class for finding area and perimeter of a rectangular playground. Write Constructor, destructor and functions for calculating area and perimeter."""

class Playground:   #creating a class Playground
    def __init__(self, l, b):                                              #constructor for initializing the values
        self.length=l                                                            #initializing values
        self.breadth=b

    def __del__(self):                                                      #destructor for the class
        print('The destructor is called for',self)

    def area(self):                                                            #function to calculate and return the area and since values have already been initialized in constructor we do not need to pass them in arguments
        return self.length * self.breadth

    def perimeter(self):                                                    #function to calculate and return the perimeter of the area and no arguments for the same reason as area function
        return 2 * (self.length + self.breadth)

def gp18(): #function in which the object of the class will be created and its functions will be called. This function will be called if the user chooses GP18
    print('Your choice is GUIDELINE PROGRAM 18 in which a class will be created with constructor/destructor and functions to find the area and perimeter of rectangle') #informing the user about their choice
    x = input('Enter the length of the rectangle: ')
    y = input('Enter the breadth of the rectangle: ')
    if checkfloat(x) or checkfloat(y):                                #checking if the values are not float or int as sides cannot have alphabets or other symbols
        print('Invalid Entry')
        return
    x = float(x)                                                                 #converting values to float as we know they can be converted and will not give an error due to previous condition
    y = float(y)
    if x<0 or y<0:                                                              #only checking if the values are negative
        print('Invalid entries. Lengths and breadhts can only be positive values')
        return                                                                     #returning so next statements of the class cannot be executed
    ob = Playground(x,y)                                                    #creating an object of the class Rectangle with x, y as its parameters
    print('Area of the rectangle is', ob.area())                  #Calling the area  and rectangle functions with the object and printing them in directly so they need not be saved
    print('Perimeter of the rectangle is', ob.perimeter())
    del ob                                                                         #calling the deconstructor/destructor


"""GUIDELINE PROGRAM 19
Write a program to perform the following functionality using csv files.
• Create a csv files for maintaining student records containing name and total marks obtained.
• Read the file created above to display the details of every third student."""

def gp19createcsvfile():            #defining function to create the csv file since we are not checking for the datatyep of marks even if the user enters something other than a number the program would work
    records = [['Name', 'Total marks']]                           #creating a list which will later be converted to csv file
    n = input('Enter the number of students (Enter is a positive integer number or gp19 will not be executed further): ') #seeing the number of students that the record will have
    if checkwholenum(n):                                                  #checking if the number n can be possible
        print('Invalid Entry of number of students and so file not created. This means further functions cannot be performed either')
        return 1                                                                   #returning 1 so when called we can know that the file was not created
    if int(n)<1:                                                                    #to see if the file would be empty
        print('Since 0 students no list will be formed so nothing else can be done ')
        return 1                                                                   #returning 1 for the same reason
    print('The name name and total marks of the students one by one (the marks here can be in any form, the program will not stop working because of it')       #creating the nested list for n+1 rows with the first row being the heading
    for i in range(int(n)):
        x=[]
        x.append(input('Enter the name of student: '))
        x.append(input('Enter the total marks of the student: '))
        records.append(x)                                                   #writing the data in the csv file
    with open('myfile.csv','w',newline='') as file:              #creating an object for it
        csvobj=csv.writer(file, delimiter='\t')
        csvobj.writerows(records)
        print('myfile.csv is created with the student details')
    return 0                                                                      #so when called we know that the file was created call the rest of the functions

def gp19display():              #function that displays the details of the student from the csv files
    print('students read from myfile.csv')
    print('Details of every student to see if it was read')
    with open('myfile.csv','r',newline='') as file:              #opening csv file with r for reading
        csvobj = csv.reader(file, delimiter='\t')                 #creating an object of the file to use
        for row in csvobj:
            print(row)
        print()                                                                     #printing plain line so next print is from a new line

def gp19display3rd():       #function to display the details of every third student
    print('Details of every third student')
    with open('myfile.csv','r', newline='') as mainf:
        l = list(csv.reader(mainf, delimiter='\t'))                 #converting the file back to a list to print the details of every third student
        for i in range(len(l)):                                                #i is the row number
            if i%3==0:
                print(l[i])

def gp19():     #fucntion that calls all the functions requried for GP19 and will be called if user chooses 19 from the main menu
    print('Your choice is GUIDELINE PROGRAM 19 in which a csv file holding names and marks of students is being maintained and the details of every 3rd students is being displayed')   #informing the user about their choice
    x = gp19createcsvfile()                                               #calling the create function and storing the return value to so it can be checked if it was created or not
    if x==1:                                                                            #if x = 1 it will mean True that means the file was not created so returning the function to not call display functions
        return
    gp19display()                                                              #calling the two display funcitons for all and only every 3rd student
    gp19display3rd()


"""GUIDELINE PROGRAM 20
Perform the following functions using list :
•Find whether all elements in list are numbers or not.
•If numeric list then count number of odd values in it.
•If string list then display the largest string in this list.
•If all elements are string then count numeric string and string with alphabets only"""

def gp20inputlist():    #a function that accepts an input in the form of a list and checks if the input is valid or not
    #assuming that the user follows the rules for entering a string as mentioned in the print statements
    print('Enter a list in using the rules given below:',end='')
    print( 'If entering a string enclose the element in "" and enclose all the elements in [] seperated by ", " example ["a", 5, True,"5"] where the whole thing is a list, "a" and "5" are strings, True is boolean and 5 is int value')
    l = input()
    try:                                                                             #eval function in try block so if user does not follow rules and an error might occur it can be handled
        l = eval(l)
    except :
        print('Invalid Entry: Rules given were not followed so the functions in gp20 cannot be perfomed in this iteration of main menu')
        return 0                                                                  #if NameError occurs, we would return 0 so when calling we know that the list was not formed
    else:
        if type(l)!= list:                                                        #checking if teh user entered a list only. If not, return 0 after a print statement
            print('Invalid Entry: Not a list')
            return 0                                                                            
        return l                                                                   #else we will return l which would now be evaluated from string to list along with all its elements

def gp20typecheck(l, datatype):#function that checks if all the elements in the list l are of the datataype passed
    f=1                                                                              #f is the check variable which will become false if even one element is not of the datatype required else will return true (initially it is considered to be true)
    for i in l:
        if type(i) != datatype :                                             #if type(i) is not equal to the datatype entered then f = 0
            f=0
    return f

def gp20countodd(l):    #function counting the number of odd elements in the numerical list passed
    c=0                                                                              #c stores the count of odd numbers and will be returned later
    for i in l:                                                                      #i in l so i will be each element in l one by one
        if i%2 != 0 :                                                              #if remainder when i is divided by 2 is not zero then i is odd so we increment c
            c=c+1
    return c                                                                       #count returned once the whole list is checked

def gp20countnumeric(l):    #function counting the number of numeric strings in the string list l passed as a parameter
    c=0                                                                             #c stores the number of numeric strings
    for i in l:                                                                     #i in l so i will be each element in l one by one
        if i.isnumeric():                                                       #if i is numberic string then c is incremented by 1
            c=c+1
    return c                                                                       #count returned once the whole list is checked

def gp20countalpha(l):        #function counting the number of alphabetical strings in the string list l passed as a parameter
    c=0                                                                              #c stores the number of alphabetical strings
    for i in l:                                                                     #i in l so i will be each element in l one by one
        if i.isalpha():                                                            #if i is alphabetical string then c is incremented by 1
            c=c+1
    return c                                                                       #count returned once the whole list is checked

def gp20():     #funciton which will call all the functions as and when required and will be called when user chooses 20
    print('Your choice is GUIDELINE PROGRAM 20 in which a list is to be accepted from the user and the following functions have to be performed') #informing the user about their choice
    print('•Find whether all elements in list are numbers or not.')
    print('•If numeric list then count number of odd values in it.')
    print('•If string list then display the largest string in this list.')
    print('•If all elements are string then count numeric string and string with alphabets only')
    l=gp20inputlist()                                                          #calling the input function and storing the returned value in inputlist
    if l == 0:                                                                      #if l = 0 then user did not give a proper input so rest of the funcitons of gp20 cannot be so returning and exiting the funciton
        return
    if gp20typecheck(l,int):                                               #checking if its a numerical string
        print('The list is a numerical list')
        print('The number of odd number elements in the list are', gp20countodd(l)) #if numeric string then we have to count the number of odd elements in the string
    elif gp20typecheck(l,str):                                           #if not numeric then we have to check if its a list only with strings
        print('The list only has strings')
        print('The largest string in the list by ASCII value is :',  max(l))    #if all are strings then we have to check for the largest string in it (using inbuilt functions for this)
        print('The largest string in the list by length is :', max(l,key=len))   #for the length wise out of two equal lenght of  strings it will choose the first one (using inbuilt funcitons for this)
        print('There are',gp20countalpha(l),'alphabetical strings in the list')     #if string then when need to count the number of alpha and num elements
        print('There are',gp20countnumeric(l),'numeric strings in the list')
    else:                                                                            #All the elements in the list are not of the same datatype so we tell the user that
        print('The list is neither completely numerical nor string')


"""GUIDELINE PROGRAM 21
Write a program that accepts two things and perform the following using sets.
• Convert each string into separate set.
•Identify and display the common characters between the two sets.
•Identify and display the distinct characters between the two sets."""

def gp21toset(l):      #function to convert the strings (in the list) passed in a strings to sets
    x = []                                                                          #x is the new list that will be passed which will have strings stored as sets
    for i in l:
        x.append(set(i))                                                       #converting the strings to set and adding them to the list x
    return x                                                                      #returning the list containing sets of those strings

def gp21common(l):    #function to indentify and display common characters stored in two different sets in a list using the intersection function for this purpose
    if (l[0]).isdisjoint(l[1]):                                                # checking if there is no intersection. If so then no value will be printed and a message will be displayed instead
        print('There are no common values between the two')
        return                                                                     #returning so next lines of the funciton cannot be executed if no intersection
    x = (l[0]).intersection(l[1])                                           #finding intersection using inbuilt function and saving in x                     
    print('The common characters in the sets of the given string are')
    for i in x:                                                                    #printing the elements of x one by one, separated by tab for proper distinction
        print(i, end='\t')
    print()                                                                         #so next statement is printed in a new line

def gp21distinct(l):    #function to indentify and display all distinct characters stored in two different sets in a list and using the sumemetric_difference function for this
    x = (l[0]).symmetric_difference(l[1])                          #using in built function to get a set of all the different distinct characters between the two sets
    if len(x)==0:                                                                #checking if x is an empty set, if so then no distinct characters so printing a message
        print('There are no distinct characters in them')
        return                                                                     #returning so next lines of the funciton cannot be executed if no distinct characters
    print('The distince elements in the sets of the given string are') #else printing the distinct characters one by one (elements of x), using tab for distinction
    for i in x:
        print(i, end='\t')
    print()                                                                         #so next statement is printed in a new line

def gp21():         #function that calls all supporting functions of gp21 as and when required and if user chooses 21 in main menu this function will be called
    print('Your choice is GUIDELINE PROGRAM 21 in which two strings accepted from the user are converted to sets and then their common and distinct characters are identified and displayed')              #informing the user about their choice
    print('Enter two strings')
    l = [input(), input()]                                                      #accepting two strings and appending them to an empty list l
    l = gp21toset(l)                                                            #converting the elements of the list using the function defined earlier
    gp21common(l)                                                             #printing the common characters of the two using function defined above
    gp21distinct(l)                                                             #printing the distinct characters of the two using funciton defiend above


"""The main() function is the one in which the user will be given the choice on which program they want to execute after they presenting them with the menu.
The choices will all be accepted and compared as strings it self so that in case user enters something wrong, an error is not generated.
The process of giving the menu to the user, accepting their choice, comparing their choice and then executing the program they have chosen will go on till the user does not choose the exit option."""

def main(): #function where all the Guideline Progrmas will be called based on the users choice
    print('Vaasvi Agarwal - Roll Number 2020/459 - PS 1 - Python Lab Final Project - A menu driven program of all the Guideline Programs in the Syllabus')  #printing my details
    while True:                                                                 #while loop which will be exited only from the inside using break or return statements when user makes that choice
        menu()                                                                     #printing the menu with all the Guideline programs (First function defined in the project at line no 10). It will be printed in every iteration
        choice = input('Enter you choice : ')                        #accepting the choice of program made by the user (will remain in string and be compared as a string
        print()                                                                     #extra line for distinction
        if choice == '1':                                                       #if choice is 1 calling gp1() defined on line 107
            gp1()
           
        elif choice == '2':                                                    #if choice is 2 calling gp2() defined on line 173
            gp2()
            
        elif choice == '3':                                                    #if choice is 3 calling gp3() defined on line 186
            gp3()
            
        elif choice == '4':                                                    #if choice is 4 calling gp1() defined on line 221
            gp4()
            
        elif choice == '5':                                                    #if choice is 5 calling gp1() defined on line 271
            gp5()
            
        elif choice == '6':                                                    #if choice is 6 calling gp1() defined on line 307
            gp6()
            
        elif choice == '7':                                                    #if choice is 7 calling gp1() defined on line 357
            gp7()
            
        elif choice == '8':                                                    #if choice is 8 calling gp1() defined on line 386
            gp8()
            
        elif choice == '9':                                                    #if choice is 9 calling gp1() defined on line 408
            gp9()
            
        elif choice == '10':                                                  #if choice is 10 calling gp1() defined on line 433
            gp10()
            
        elif choice == '11':                                                  #if choice is 11 calling gp1() defined on line 506
            gp11()
            
        elif choice == '12':                                                  #if choice is 12 calling gp1() defined on line 555
            gp12()
            
        elif choice == '13':                                                  #if choice is 13 calling gp1() defined on line 609
            gp13()
            
        elif choice == '14':                                                  #if choice is 14 calling gp1() defined on line 630
            gp14()
            
        elif choice == '15':                                                  #if choice is 15 calling gp1() defined on line 672
            gp15()
            
        elif choice == '16':                                                  #if choice is 16 calling gp1() defined on line 726
            gp16()
            
        elif choice == '17':                                                  #if choice is 17 calling gp1() defined on line 796
            gp17()
            
        elif choice == '18':                                                  #if choice is 18 calling gp1() defined on line 838
            gp18()
            
        elif choice == '19':                                                  #if choice is 19 calling gp1() defined on line 896
            gp19()
            
        elif choice == '20':                                                 #if choice is 20 calling gp1() defined on line 956
            gp20()
            
        elif choice == '21':                                                  #if choice is 21 calling gp1() defined on line 1010
            gp21()
             
        elif choice == '0':                                                    #if choice is 0 then loop will be terminated after given the reason in a statement
            print('The Program is terminated as you chose the EXIT option 0. Thank you - Vaasvi Agarwal')
            return                                                                 #return so that the control leaves the main function and the progrma is terminated

        else:                                                                        #if user enters anything that is not given in the choice a message will be displayed
            print('Choice not given')
        print()                                                                     #extra line for distinction


"""Checking if the control is in the correct module and then calling the main function for the execution of the project"""

if __name__ == "__main__":
    main()                                                                          #calling the main function
            

