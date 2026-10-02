import json
import requests


def dish_fetch(num):
    response = requests.get(f"https://api-colombia.com/api/v1/TypicalDish/{num}")
    dish = json.loads(response.content)
    return dish


def main():
    print("Hello learners!")

    print("\nMENÚ DE PLATOS TÍPICOS DE COLOMBIA ")
    print("1. Bandeja Paisa")
    print("2. Sancocho Antioqueño")
    print("3. Ajiaco Santafereño")
    print("4. Sancocho de Gallina")
    print("5. Lechona Tolimense")

    
    opcion = int(input("\nElige el número de un plato (1-68): "))

  
    if 1 <= opcion <= 68:
        plato = dish_fetch(opcion)
        print("\n INFORMACIÓN DEL PLATO ")
        print("Nombre:", plato.get("name"))
        print("Descripción:", plato.get("description"))
        print("Ingredientes:", plato.get("ingredients"))
    else:
        print("Opción no válida. Ingresa un número entre 1 y 68.")


if __name__ == "__main__":
    main()
