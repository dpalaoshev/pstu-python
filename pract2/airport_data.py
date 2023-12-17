import json

def get_iata_code(airport_data, airport_name):
    for code, names in airport_data.items():
        if airport_name.lower() == names["english_name"].lower() or airport_name.lower() == names["russian_name"].lower():
            return code

if __name__ == "__main__":
    with open('airport_data.json', 'r', encoding='utf-8') as file:
        airport_data = json.load(file)

    airport_name = 'Buariki'
    iata_code = get_iata_code(airport_data, airport_name)
    print(f"IATA код: {iata_code}")

    airport_name = 'Асау'
    iata_code = get_iata_code(airport_data, airport_name)
    print(f"IATA код: {iata_code}")
