class Creature:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} ({self.species})"

    def __repr__(self):
        return f"Creature('{self.name}', '{self.species}')"

    def __eq__(self, other):
        if isinstance(other, Creature):
            return self.name == other.name and self.species == other.species
        return False

    def __ne__(self, other):
        if isinstance(other, Creature):
            return not self.__eq__(other)
        return False

    def __lt__(self, other):
        if isinstance(other, Creature):
            return (self.species, self.name) < (other.species, other.name)
        return False

    def __gt__(self, other):
        if isinstance(other, Creature):
            return (self.species, self.name) > (other.species, other.name)
        return False

    def __le__(self, other):
        if isinstance(other, Creature):
            return (self.species, self.name) <= (other.species, other.name)
        return False

    def __ge__(self, other):
        if isinstance(other, Creature):
            return (self.species, self.name) >= (other.species, other.name)
        return False


class Mammal(Creature):
    def __init__(self, name, species, years):
        super().__init__(name, species)
        self.years = years

    def __str__(self):
        return f"{super().__str__()}, {self.years} years"

    def __repr__(self):
        return f"Mammal('{self.name}', '{self.species}', {self.years})"

    def __eq__(self, other):
        if isinstance(other, Mammal):
            return super().__eq__(other) and self.years == other.years
        return False

    def __ne__(self, other):
        if isinstance(other, Mammal):
            return super().__ne__(other) and not self.__eq__(other)
        return False

    def __lt__(self, other):
        if isinstance(other, Mammal):
            return super().__lt__(other) and self.years < other.years
        return False

    def __gt__(self, other):
        if isinstance(other, Mammal):
            return super().__gt__(other) and self.years > other.years
        return False

    def __le__(self, other):
        if isinstance(other, Mammal):
            return super().__le__(other) and self.years <= other.years
        return False

    def __ge__(self, other):
        if isinstance(other, Mammal):
            return super().__ge__(other) and self.years >= other.years
        return False


class DomesticAnimal(Mammal):
    def __init__(self, name, species, years, breed):
        super().__init__(name, species, years)
        self.breed = breed

    def __str__(self):
        return f"{super().__str__()}, {self.breed} breed"

    def __repr__(self):
        return f"DomesticAnimal('{self.name}', '{self.species}', {self.years}, '{self.breed}')"


creature1 = Creature("Lion", "Mammal")
creature2 = Creature("Giraffe", "Mammal")
mammal1 = Mammal("Giraffe", "Mammal", 5)
domestic_animal1 = DomesticAnimal("Fluffy", "Cat", 3, "Siamese")
domestic_animal2 = DomesticAnimal("Bella", "Cat", 2, "Maine Coon")

print(str(creature1))
print(str(mammal1))
print(str(domestic_animal1))
print(repr(creature1))
print(repr(mammal1))
print(repr(domestic_animal1))
print(domestic_animal1 == domestic_animal2)
print(domestic_animal1 != domestic_animal2)
print(domestic_animal1 > mammal1)
print(domestic_animal1 < creature1)
