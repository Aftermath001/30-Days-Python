# You are building a program to help a user decide what to wear based on the current weather conditions. 
# Write a Python program that prompts the user to enter the current temperature in Fahrenheit and whether it is currently raining or not 
# (as a boolean value), and then suggests an appropriate outfit based on the following criteria:

# If the temperature is less than 50 degrees Fahrenheit, suggest wearing a coat, hat, scarf, and gloves. 
# If the temperature is between 50 and 70 degrees Fahrenheit and it is not raining, suggest wearing a sweater or light jacket. 
# If the temperature is between 50 and 70 degrees Fahrenheit and it is raining, suggest wearing a rain jacket and boots. 
# If the temperature is above 70 degrees Fahrenheit and it is not raining, suggest wearing a t-shirt and shorts. 
# If the temperature is above 70 degrees Fahrenheit and it is raining, suggest wearing a light jacket and rain boots.


def weather():
    joto = float(input("Enter Degree: "))
    rain = input("is it raining? (type True or False): ")
    if joto < 50:
        print("wear coat, hat, scarf and gloves ")
    elif joto >= 50 and joto <= 70 and rain != True:
        print("wear a sweater or light jacket")
    elif joto >= 50 and joto <= 70 and rain == True:
         print("wear a rain jacket and boots")
    elif joto > 70 and rain != True:
        print("wear tshirt and short")
    elif joto > 70 and rain == True:
        print("wear light jacket and boots")
weather()