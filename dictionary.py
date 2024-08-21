country = {"Nigeria": "Abuja", "USA": "Washington DC", "United Kingdom": "London"}
capital = country.keys()  # returns the display of all the keys in the dictionary
print(capital)

value = country.get("USA")  # displays the value for a specified key
value_2 = country.get("france")  # displays none since key doesn't exist in dictionary
print(value)
print(value_2)

country["italy"] = "rome"  # adds or updates the dictionary with an element
print(country)