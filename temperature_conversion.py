print("""Choose The Conversion Type:
1.Celsius to Fahrenheit
2.Fahrenheit to Celsius""")
user = input("Enter your choice (1 OR 2):\n")
if user in ["1", "2"]:
   temperature = input("Enter The Temperature in Celsius: \n")
   float_temperature = float(temperature)

   if user == "1":
       f = (float_temperature * 9/5) + 32
       print("The Temperature in Fahrenheit is :\n", f)
   elif user == "2":
       c = (float_temperature - 32) * 5/9
       print("The Temperature in Celsius is :\n", c)

if user not in ["1", "2"]:
    print("Invalid choice, Please run the program again and choose 1 or 2")
  
