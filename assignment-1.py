# Assignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.


# Class representing a Content (Book, Movie, etc.)

from abc import ABC, abstractmethod
class Content (ABC):
    def __init__(self, title, genre, release_year): # Constructor to initialize the content
        self.title = title
        self.genre = genre
        self.release_year = release_year

    @abstractmethod
    def get_info(self): # Abstract method to be implemented by subclasses
        pass

    
class Book(Content):
    def __init__(self, title, author, genre, release_year):
        super().__init__(title, genre, release_year) # Call the parent constructor
        self.author = author

    def get_info(self):
        return f"{self.title} by {self.author} ({self.release_year}) - Genre: {self.genre}"
    
class Movie(Content):
    def __init__(self, title, director, genre, release_year): 
        super().__init__(title, genre, release_year) # Call the parent constructor
        self.director = director

    def get_info(self):
        return f"{self.title} directed by {self.director} ({self.release_year}) - Genre: {self.genre}"
    
class Music(Content):
    def __init__(self, title, artist, genre, release_year):
        super().__init__(title, genre, release_year) # Call the parent constructor
        self.artist = artist

    def get_info(self):
        return f"{self.title} by {self.artist} ({self.release_year}) - Genre: {self.genre}"

# Example usage
if __name__ == "__main__":
    # Create instances of each class
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925)
    movie = Movie("Inception", "Christopher Nolan", "Sci-Fi", 2010)
    music = Music("Bohemian Rhapsody", "Queen", "Rock", 1975)

    # Initialize a list of contents
    contents = [book, movie, music]

    # Iterate through the list and print information about each content
    for content in contents:
        print(content.get_info())



# Explanation:
# - The `Content` class is an abstract base class that defines a constructor to initialize common attributes (title, genre, release_year) and an abstract method `get_info()`.
# - The `Book`, `Movie`, and `Music` classes inherit from the `Content` class and implement the `get_info()` method to provide specific information about the content.
# - The `super().__init__()` calls the constructor of the parent class to initialize common attributes.

# - Each subclass has its own constructor that initializes specific attributes (like author, director, artist).
# - The `get_info` method is overridden in each subclass to provide specific information about the content. This demonstrates polymorphism.
# - The example usage creates instances of each class and prints their information using the `get_info` method.