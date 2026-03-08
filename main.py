import requests


def main():
    print("=== Pokédex CLI — Pokémon Information Explorer ===")

    while True:
        name = input("\nEnter Pokémon name (or 'q' to quit): ").lower().strip()

        if name == "q":
            print("Goodbye Trainer!")
            break

        data = get_pokemon_data(name)

        if data:
            display_pokemon(data)
            save_option(data)
        else:
            print("Pokémon not found. Please try again.")


def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        return response.json()

    except requests.RequestException:
        print("Network error. Please check your internet connection.")
        return None

def display_pokemon(data):

    name = data["name"].title()
    height = data["height"]
    weight = data["weight"]
    base_exp = data["base_experience"]

    types = [t["type"]["name"] for t in data["types"]]
    abilities = [a["ability"]["name"] for a in data["abilities"]]

    print("\n----- Pokémon Info -----")
    print(f"Name: {name}")
    print(f"Type: {', '.join(types)}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"Base Experience: {base_exp}")

    print("\nAbilities:")
    for ability in abilities:
        print(f"- {ability}")

    print("\nStats:")
    for stat in data["stats"]:
        stat_name = stat["stat"]["name"]
        stat_value = stat["base_stat"]
        print(f"{stat_name.title()}: {stat_value}")


def save_option(data):

    choice = input("\nSave this Pokémon to pokedex.txt? (y/n): ").lower()

    if choice == "y":

        name = data["name"].title()
        types = [t["type"]["name"] for t in data["types"]]

        with open("pokedex.txt", "a") as file:
            file.write(f"{name} | Type: {', '.join(types)}\n")

        print("Pokémon saved successfully!")


if __name__ == "__main__":
    main()

    