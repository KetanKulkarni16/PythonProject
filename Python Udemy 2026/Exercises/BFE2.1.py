#Fix the bug

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
print(countries)


#Solution: Just indent last print statement in to the loop.
countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)