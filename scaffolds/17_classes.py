"""
Lesson 17: Classes - Designing Your Own Kind Of Thing
======================================================

WHAT YOU'LL LEARN
  How to invent a brand new kind of thing, like a Monster, and then
  make as many of them as your game needs.

NEW WORDS
  class        A blueprint describing what a kind of thing knows and
               can do. A class is not a thing itself; it is the plan.
  object       An actual thing built from the blueprint. Also called
               an instance.
  __init__     A special method that runs automatically whenever you
               build a new object. It sets the starting values.
  self         The word a class uses to mean "this particular
               object". It is always the first parameter.
  attribute    A piece of information stored on an object, reached
               with a dot: goblin.name

HOW IT WORKS
  class Monster:
      def __init__(self, name, hp):
          self.name = name
          self.hp = hp

  The class is the plan. Nothing exists yet. To build a real monster:

      goblin = Monster("Goblin", 30)

  Python runs __init__ with self set to the new object, so self.name
  becomes "Goblin" and self.hp becomes 30. Now you can read them back
  with a dot:

      print(goblin.name)
      print(goblin.hp)

  Build a second one and it is completely separate:

      dragon = Monster("Dragon", 200)

YOUR TASK
  Step 1: Create a class named Monster with an __init__ method taking
          self, name and hp, and store both on self.
  Step 2: Create an object named goblin by calling Monster("Goblin",
          30).
  Step 3: Print goblin.name and print goblin.hp.

EXAMPLE
  This example is about a book, so you still write your own Monster.

      class Book:
          def __init__(self, title, pages):
              self.title = title
              self.pages = pages

      atlas = Book("World Atlas", 120)
      print(atlas.title)
      print(atlas.pages)

WHEN IT WORKS YOU'LL SEE
  Goblin
  30

IF YOU GET STUCK
  TypeError: takes 2   -> you forgot self as the first parameter of
  positional arguments    __init__.
  AttributeError       -> you wrote name = name instead of
                          self.name = name, so nothing was stored.
  Nothing happens      -> defining a class does not create an object.
                          You must call Monster(...) to build one.

STYLE
  Class names use PascalCase: every word starts with a capital and
  there are no underscores, like Monster or HealthPotion. Functions
  and variables stay in snake_case. This instantly tells a reader
  which is which.

CHECK YOUR WORK
  python run_lesson.py 17
"""

# TODO: Write your code for Lesson 17 below this line.
