from weather import get_weather


def main():
    print("=== Väderprogram ===")

    while True:
        city = input("Skriv stad (eller quit): ")

        if city.lower() == "quit":
            print("Programmet avslutas.")
            break

        weather = get_weather(city)

        if weather:
            print(f"\nStad: {weather['city']}")
            print(f"Temperatur: {weather['temperature']}°C")
            print(f"Väder: {weather['description']}\n")
        else:
            print("Kunde inte hämta väderdata.\n")


main()