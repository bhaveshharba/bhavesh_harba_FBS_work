# 3. Convert distant given in feet and inches into meter and centimeter.

feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_inches = feet * 12 + inches
total_cm = total_inches * 2.54 

print(f"{feet} FT and {inches} Inch is \n{total_inches} Inch or {total_cm}Centimeters")
