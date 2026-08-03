"""
Lesson 19: Inheritance - Building On Another Class
===================================================

WHAT YOU'LL LEARN
  How to make a new class that automatically gets everything an
  existing class has, then adds its own twist.

NEW WORDS
  inheritance  When one class receives the abilities of another,
               instead of copying the code.
  parent class The original class being built on. Also called the
               base class. Here that is Animal.
  child class  The new class that inherits. Also called a subclass.
               Here that is Dog.
  override     When a child class replaces a method it inherited with
               its own version.

HOW IT WORKS
  class Animal:
      def __init__(self, name):
          self.name = name

      def speak(self):
          return "..."

  To build on it, put the parent's name in brackets after the child:

      class Dog(Animal):
          def speak(self):
              return "Woof!"

  Dog never defines __init__, yet Dog("Buddy") still works, because
  it inherited __init__ from Animal. It does define its own speak,
  which overrides the quiet one it inherited.

      dog = Dog("Buddy")
      print(dog.name)      ->  Buddy    (inherited)
      print(dog.speak())   ->  Woof!    (overridden)

  Inheritance is how you avoid writing the same code twice.

YOUR TASK
  Step 1: Create a class named Animal whose __init__ takes self and
          name, and stores self.name.
  Step 2: Create a class named Dog that inherits from Animal by
          writing class Dog(Animal), and give it a speak method that
          returns a dog sound.
  Step 3: Create a Dog, then print its name and what it says.

EXAMPLE
  This example is about vehicles, so you still write your own Animal
  and Dog.

      class Vehicle:
          def __init__(self, name):
              self.name = name

      class Bike(Vehicle):
          def wheels(self):
              return 2

      bmx = Bike("BMX")
      print(bmx.name)
      print(bmx.wheels())

WHEN IT WORKS YOU'LL SEE
  Buddy says Woof!

IF YOU GET STUCK
  NameError: Animal is  -> define the parent class above the child
  not defined              class in the file.
  AttributeError: no    -> check the method name is spelled the same
  attribute speak          in the class and where you call it.
  TypeError on Dog(...) -> the parent's __init__ decides what
                           arguments Dog needs.

CHECK YOUR WORK
  python run_lesson.py 19
"""

# TODO: Write your code for Lesson 19 below this line.
