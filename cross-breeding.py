import tkinter as tk
from tkinter import messagebox
import random

# Genetic inheritance simulation
class Animal:
    def __init__(self, species, trait1, trait2):
        self.species = species
        self.trait1 = trait1
        self.trait2 = trait2

    def crossbreed(self, other):
        # Simulate genetic inheritance of traits
        child_trait1 = self._inherit_trait(self.trait1, other.trait1)
        child_trait2 = self._inherit_trait(self.trait2, other.trait2)
        
        # Return a new Animal as a child
        return Animal(self.species, child_trait1, child_trait2)

    def _inherit_trait(self, trait1, trait2):
        # Inheritance logic: random combination of parent traits (simplified)
        return random.choice([trait1, trait2])

    def get_traits(self):
        return f"Trait 1: {self.trait1}, Trait 2: {self.trait2}"

# GUI class
class GeneticBreedingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Genetic Breeding Simulation")
        self.root.geometry("500x500")
        self.root.config(bg='yellow')

        self.species_label = tk.Label(self.root, text="Enter Animal Species", bg="yellow")
        self.species_label.pack()

        self.species_entry = tk.Entry(self.root)
        self.species_entry.pack()

        self.trait1_label = tk.Label(self.root, text="Enter Trait 1 (Dominant or Recessive)", bg="yellow")
        self.trait1_label.pack()

        self.trait1_entry = tk.Entry(self.root)
        self.trait1_entry.pack()

        self.trait2_label = tk.Label(self.root, text="Enter Trait 2 (Dominant or Recessive)", bg="yellow")
        self.trait2_label.pack()

        self.trait2_entry = tk.Entry(self.root)
        self.trait2_entry.pack()

        self.breed_button = tk.Button(self.root, text="Breed Animals", command=self.simulate_breeding)
        self.breed_button.pack()

        self.results_label = tk.Label(self.root, text="", bg="yellow")
        self.results_label.pack()

    def simulate_breeding(self):
        species = self.species_entry.get()
        trait1 = self.trait1_entry.get()
        trait2 = self.trait2_entry.get()

        if not species or not trait1 or not trait2:
            messagebox.showerror("Input Error", "Please fill all the fields.")
            return

        # Create two animals for crossbreeding
        animal1 = Animal(species, trait1, trait2)
        animal2 = Animal(species, trait1, trait2)

        # Crossbreed them
        offspring = animal1.crossbreed(animal2)
        self.display_results(offspring)

    def display_results(self, offspring):
        self.results_label.config(text=f"Offspring Traits:\n{offspring.get_traits()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GeneticBreedingApp(root)
    root.mainloop()
