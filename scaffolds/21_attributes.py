"""
Lesson 21: Class Attributes - Shared By Everyone
=================================================

WHAT YOU'LL LEARN
  The difference between information that belongs to one object and
  information shared by every object of that class.

NEW WORDS
  instance attribute  A value set on self inside __init__. Each
                      object gets its own copy.
  class attribute     A value written directly in the class body,
                      outside any method. Every object shares it.
  class_item          The name you will give your shared attribute in
                      this lesson.

HOW IT WORKS
  class Hero:
      class_item = "Adventurer's Badge"

      def __init__(self, name):
          self.name = name

  class_item sits in the class body, so it belongs to the class
  itself. name is set on self, so it belongs to one hero.

      a = Hero("Musab")
      b = Hero("Zoe")
      print(a.name, b.name)          -> different for each hero
      print(a.class_item)            -> Adventurer's Badge
      print(Hero.class_item)         -> the same badge

  You can reach a class attribute through any object or through the
  class name. Use one when the value is genuinely the same for all
  of them, like a badge every hero carries.

YOUR TASK
  Step 1: Create a class named Hero with a class attribute named
          class_item, and an __init__ that stores self.name.
  Step 2: Create a hero, then print the class_item through the object
          and through the Hero class itself, to show they match.

EXAMPLE
  This example is about pupils in a school, so you still write your
  own Hero.

      class Pupil:
          school = "Riverside Primary"

          def __init__(self, name):
              self.name = name

      p = Pupil("Sam")
      print(p.name)
      print(p.school)
      print(Pupil.school)

WHEN IT WORKS YOU'LL SEE
  Musab carries the Adventurer's Badge
  Every hero carries the Adventurer's Badge

IF YOU GET STUCK
  AttributeError        -> the class attribute must be indented
                           inside the class, but not inside __init__.
  Each hero has a       -> you put it on self. Move it out of
  different one            __init__ into the class body.

CHECK YOUR WORK
  python run_lesson.py 21
"""

# TODO: Write your code for Lesson 21 below this line.
