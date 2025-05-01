# Assignment 1
---
## Assignment 1: Design Your Own Class! 🏗️
## Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
## Add attributes and methods to bring the class to life!
## Use constructors to initialize each object with unique values.
## Add an inheritance layer to explore polymorphism or encapsulation.
---

This project demonstrates core Object-Oriented Programming (OOP) concepts in Python — specifically inheritance, polymorphism, and abstraction — by modeling different types of content: books, movies, and music.

## 🧠 Concepts Covered

- **Classes & Objects**
- **Constructors (`__init__`)**
- **Inheritance**
- **Polymorphism**
- **Abstract Base Classes (ABC)**
- **Method Overriding**

### `Content` (Abstract Base Class)
A generic class representing any form of content. It cannot be instantiated directly and requires subclasses to implement the `get_info()` method.

```python
from abc import ABC, abstractmethod

class Content(ABC):
    def __init__(self, title, genre, release_year):
        self.title = title
        self.genre = genre
        self.release_year = release_year

    @abstractmethod
    def get_info(self):
        pass

```

### Subclasses
- Book — adds author
- Movie — adds director
- Music — adds artist
**Each subclass overrides the get_info() method to return a formatted string containing its specific information.**


```
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925)
movie = Movie("Inception", "Christopher Nolan", "Sci-Fi", 2010)
music = Music("Bohemian Rhapsody", "Queen", "Rock", 1975)

contents = [book, movie, music]

for content in contents:
    print(content.get_info())

```

``` output
The Great Gatsby by F. Scott Fitzgerald (1925) - Genre: Fiction
Inception directed by Christopher Nolan (2010) - Genre: Sci-Fi
Bohemian Rhapsody by Queen (1975) - Genre: Rock

```


# Assignment 2

---
## Activity 2: Polymorphism Challenge! 🎭

## Create a program that includes animals or vehicles with the same action (like move()). 
## However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
---

## 🧠 Concepts Covered

- **Abstract Base Classes (ABC)**
- **Abstract Methods**
- **Polymorphism**
- **Inheritance**
- **Error Handling (e.g., NotImplementedError)**

### `Animal` (Abstract Base Class)
Defines a contract for all animal types. Any subclass must implement the `move()` method, or it will raise a `NotImplementedError`.

```python
class Animal(ABC):
    @abstractmethod
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

```
## Subclasses and Their Behaviors
- Dog: Implements move() as "Running"
- Snake: Implements move() as "Slithering"
- Bird: Implements move() as "Flying"
**Fish: Does not implement move() to demonstrate error enforcement**

```
dog = Dog()
snake = Snake()
bird = Bird()

animals = [dog, snake, bird]

for animal in animals:
    print(f"{animal.__class__.__name__} is {animal.move()}")

```
```
Dog is Running
Snake is Slithering
Bird is Flying

```
---
**Note: Attempting to instantiate or call move() on Fish will raise an error since it does not implement the required method.**

---