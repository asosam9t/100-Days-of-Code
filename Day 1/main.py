#This program is intended to generate a band name based on two values provided by the user; their city and pet name.

#1. Create a greeting for your program.

print("Hello there, Welcome to the BAND NAME GENERATOR SOFTWARE\n")

#2. Ask the user for the city that they grew up in.

city = input("Please enter the name of the city you grow up in\n")

#3. Ask the user for the name of a pet.

pet_name = input("Please enter the name of your pet\n")

#4. Combine the name of their city and pet and show them their band name.

band_name = city + " " + pet_name 

#5. Make sure the input cursor shows on a new line:

print ('Your Band Name could be ' + '"'+band_name+'"')
