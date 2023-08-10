from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, new_pokemon: Pokemon):
        for pokemon in self.pokemons:
            if new_pokemon.name == pokemon.name:
                return "This pokemon is already caught"
        self.pokemons.append(new_pokemon)
        return f"Caught {new_pokemon.name} with health {new_pokemon.health}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = (f"Pokemon Trainer {self.name}\n"
                  f"Pokemon count {len(self.pokemons)}")
        for pokemon in self.pokemons:
            result += '\n- ' + pokemon.pokemon_details()
        return result
