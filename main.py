import swapi

def get_film_details(film_id):
    api = swapi.Swapi()
    film = api.get_film(film_id)
    characters = [api.get_person(character_id) for character_id in film.characters]
    vehicles = [api.get_vehicle(vehicle_id) for vehicle_id in film.vehicles]
    starships = [api.get_starship(starship_id) for starship_id in film.starships]
    species = [api.get_species(species_id) for species_id in film.species]

    print(f"Фільм: {film.title}")
    print("Персонажі:")
    for idx, character in enumerate(characters, 1):
        print(f"  {idx}. {character.name} з планети {character.homeworld.name}")
    print("Транспортні засоби:")
    for idx, vehicle in enumerate(vehicles, 1):
        print(f"  {idx}. {vehicle.name}")
    print("Космічні кораблі:")
    for idx, starship in enumerate(starships, 1):
        print(f"  {idx}. {starship.name}")
    print("Види істот:")
    for idx, specie in enumerate(species, 1):
        print(f"  {idx}. {specie.name}")


if __name__ == "__main__":
    film_id = input("Введіть ідентифікатор фільму: ")
    get_film_details(film_gitid)