"""

*Program To Calculate Simple Interest And Compound Interest*
Created By :- Suraj Sharma
Date :- 28.06.2021

"""

import os #A system file and functions related module

from termcolor import colored #importing termcolor Module to make programm more Beautiful

import pyfiglet #Pyfiglet Module Used For Ascii_art Creation.

#Ascii_Art Used To Show A Good Desgine For My Programm.

os.system('clear') #clear's the screen

ascii_art = pyfiglet.figlet_format("          SI > > > CI")

#Printing Banner or Ascii_art
print(colored(ascii_art, "magenta"))


#Printing About Tool And Its Creator.
print(colored("\n\n\t>> SI and CI Calculator By Suraj Sharma <<\n", "yellow"))

#Defining A Function...
def find_Simple_Interest():
	
	 #Printing Line For Decoration And Used Termcolor Module To Color The Output
	print(colored("\n\n"+"="*59, "yellow"))
	
	# For Principal As Input
	Principal = float(input("\n\nEnter Principal Amount : "))
	#For Rate as Input 
	Rate = float(input("\n\nEnter Rate of Interest : "))
	
	#For Time as Input
	Time = int(input("\n\nEnter Time : "))
	
	#For Calculation of SI
	Simple_Interest = (Principal*Rate*Time)/100
	
	#For Printing The Calculation of SI
	print(f"\n\nSimple Interest Is : ₹ {Simple_Interest}\n")#Use of f-"string"
	
	#Printing Line For Decoration And Used Termcolor Module To Color The Output
	print(colored("\n"+"="*59, "yellow"))
	
	print()#for one line space
	
#Function To Calculate C.I.
def Compound_Interest():
	
	#Printing Line For Decoration And Used Termcolor Module To Color The Output
	print(colored("\n\n"+"="*59, "yellow"))
	
	
	#Input for taking Principal Amount
	Principal = float(input("\n\nEnter Principal amount : "))
	
	#Input for taking Rate of  Interest
	Rate = float(input("\n\nEnter rate of Interest : "))
	
	#input for taking number of times the interest is compounded per year 
	N = int(input("\n\nEnter no of time interest compounded per year : "))
	
	
	#Calculation of Compund Interest.
	CI = Principal*(1+Rate/100)**N
	
	#Showing Final Answer as a Output
	print(f"\n\nCompound Interest is : ₹ {CI}")
	
	#Printing Line For Decoration And Used Termcolor Module To Color The Output
	print(colored("\n\n"+"="*59, "yellow"))
	print() #For giving a one line space
		
if __name__ == '__main__':
		
		def choose():
			
			choice = input("\n\nChoose (SI) or (CI) : ").lower()#Taking Input as all Lower Words.
	
						
			#Use of if, else statements.
			
			if(choice == "si"):
			#Calling The Simple Interest Fuction
				find_Simple_Interest()
				
			elif(choice == "ci"):
				#Calling The CI function
				Compound_Interest()
				
			else:
				print(colored("\nInvalid Input !", "red")) #Else statement To check for A invalid Input By User.
			

			choose() #Use of Recursion
choose() 
		
"""

Recursion Call's A function itself And Work's Like a Loop

"""		
		
		
#=========== Thankyou ===========#

