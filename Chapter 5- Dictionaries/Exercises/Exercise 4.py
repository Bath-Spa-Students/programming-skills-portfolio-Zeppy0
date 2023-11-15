rivers = {
    "Nile": "Egypt", "Ganges": "India", "yangtze": "china"
}

for river, country in rivers.items(): 
    print(f"The {river.capitalize()} runs through {country.capitalize()}.")
