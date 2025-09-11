country={'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21}
user_command=""
while user_command !="PRINT":
    user_command = input("Pls enter the next or print: ").upper()
    if user_command=="PRINT":
        break
    country_name = input("Enter the name of the country").upper()
    population=int(input("Enter the population"))
    country[country_name]=population
print(country)
import json
s=input("Enter the file directory to save as: ")
r=json.dumps(country)
with open(f"c://data//{s}.txt","w") as f:
    f.write(r)



