# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod  # Abstract method to be implemented by subclasses
    def move(self): 
        raise NotImplementedError("Subclasses must implement this method")
    

class Dog(Animal):
    def move(self):
        return "Running"  # Dog's way of moving
    
class Snake(Animal):
    def move(self):
        return "Slithering"  # Snake's way of moving
    
class Bird(Animal):
    def move(self):
        return "Flying"  # Bird's way of moving
    
class Fish(Animal):
    # Fish doesn't implement move() method, so it will raise an error if called directly
    pass  # Fish doesn't have a specific move method, but it can be added later if needed



# Example usage
if __name__ == "__main__":
    # Create instances of each animal
    dog = Dog()
    snake = Snake()
    bird = Bird()

    

    
    # Initialize a list of animals
    animals = [dog, snake, bird]
    
    # Iterate through the list and print the way each animal moves
    for animal in animals:
        print(f"{animal.__class__.__name__} is {animal.move()}")
    
    # Uncommenting the following line will raise an error since Fish doesn't implement move()
    # fish = Fish()
    # print(fish.move())  # This will raise NotImplementedError


# Explanation:
# - The `Animal` class is an abstract base class that defines an abstract method `move()`. It cannot be instantiated directly.
# - The `Dog`, `Snake`, and `Bird` classes inherit from the `Animal` class and implement the `move()` method in their own way.
# - The `Fish` class is defined but does not implement the `move()` method, demonstrating that it can be left unimplemented if needed.
# - The example usage creates instances of each animal and prints the way they move using the `move()` method.
# - The program demonstrates polymorphism by allowing different classes to define the same method (`move()`) in their own way.
# - If you try to call the `move()` method on an instance of the `Fish` class, it will raise a `NotImplementedError`, indicating that the method is not implemented.