# Glossary

Every technical word used in this course, in plain language, with the
lesson that introduces it. If a lesson uses a word you do not recognise,
look it up here.

There are 169 terms. They are listed alphabetically.

| Term | What it means | First taught in |
|---|---|---|
| `+= 1` | A shortcut for "add one to this variable". count += 1 means count = count + 1. | Lesson 9 |
| `.append()` | A list method that adds one new element to the end. | Lesson 7 |
| `.center()` | A string method that pads text with spaces so it sits in the middle of a given width. | Lesson 47 |
| `.get()` | Looks a key up but returns None instead of crashing when it is missing. | Lesson 42 |
| `.items()` | A method giving back both together, ideal for looping. | Lesson 15 |
| `.keys()` | A method giving back all the labels. | Lesson 15 |
| `.lower()` | A string method that gives back a quiet copy, all in small letters. | Lesson 5 |
| `.read()` | Gives you the whole file as one long string. | Lesson 26 |
| `.readlines()` | Gives you a list, with one string per line. | Lesson 26 |
| `.remove()` | Takes the first matching item out of a list. | Lesson 33 |
| `.strip()` | Removes spaces and the invisible newline character from the ends of a string. | Lesson 26 |
| `.upper()` | A string method that gives back a SHOUTY copy of the text, in capitals. | Lesson 5 |
| `.values()` | A method giving back all the stored values. | Lesson 15 |
| `.write()` | Puts text into the open file. | Lesson 25 |
| `:.1f` | Show this number with one digit after the point. | Lesson 30 |
| `:<10` | Pad this value with spaces to ten characters wide, lined up to the left. | Lesson 30 |
| `=` | The assignment operator. It does NOT mean "equals" like in maths. It means "put the value on the right into the name on the left." | Lesson 2 |
| `==` | The comparison operator meaning "is the same as". One = stores a value; two == asks a question. | Lesson 6 |
| `\n` | Newline. Where you put it, the text jumps down to the next line. | Lesson 3 |
| `\t` | Tab. Adds a wide gap, useful for lining up columns. | Lesson 3 |
| `__init__` | A special method that runs automatically whenever you build a new object. It sets the starting values. | Lesson 17 |
| `afford` | Whether the hero has enough gold for the price. | Lesson 41 |
| `amount` | How much health a Potion restores. | Lesson 23 |
| `and` | Joins two conditions. The whole thing is only True when BOTH sides are True. | Lesson 8 |
| `ANSI escape code` | A short secret string that tells the terminal to change color. They all begin with \033[ which is the escape character followed by a square bracket. | Lesson 46 |
| `argument` | The actual value you hand over when you call it. | Lesson 10 |
| `attack(hero, monster)` | The function you will write. It takes both objects so it can read one and change the other. | Lesson 38 |
| `attack_power` | How hard this monster hits. | Lesson 37 |
| `attacker` | The fighter doing the hitting. It has attack_power. | Lesson 39 |
| `attribute` | A piece of information stored on an object, reached with a dot: goblin.name | Lesson 17 |
| `banner` | A title framed by decorative lines. | Lesson 47 |
| `base class` | The general class other classes build on. Here, Item. | Lesson 22 |
| `body` | The indented lines underneath def. This is the code that runs each time you call the function. | Lesson 11 |
| `bonus` | The extra attack a Weapon adds. | Lesson 23 |
| `boolean` | A value that is either True or False. Nothing else. | Lesson 8 |
| `border` | A decorative line, usually made by repeating one character, that separates parts of the screen. | Lesson 3 |
| `calculate_damage` | The exact name of the function you will write in this lesson. Your test looks for this name. | Lesson 39 |
| `call` | To make a function run: show_status("Musab", 100, 50) | Lesson 10 |
| `cap` | To stop a number going above a limit. A hero on 95 health drinking a 30-point potion should end on 100, not 125. | Lesson 36 |
| `chance` | A probability between 0.0 and 1.0. 0.5 means a fifty-fifty coin flip. | Lesson 40 |
| `child class` | The new class that inherits. Also called a subclass. Here that is Dog. | Lesson 19 |
| `class` | A blueprint describing what a kind of thing knows and can do. A class is not a thing itself; it is the plan. | Lesson 17 |
| `class attribute` | A value written directly in the class body, outside any method. Every object shares it. | Lesson 21 |
| `class_item` | The name you will give your shared attribute in this lesson. | Lesson 21 |
| `Color` | The class you will write to hold those codes. | Lesson 46 |
| `colorize()` | The function you will write to wrap text in a color. | Lesson 46 |
| `comparison` | A question that gives back a boolean. < means "less than", > means "greater than", == means "the same as". | Lesson 8 |
| `concatenate` | The proper word for joining strings together to make one longer string. | Lesson 5 |
| `condition` | The true-or-false question an if statement asks. | Lesson 6 |
| `constant` | A value that never changes. Constants are written in UPPER_CASE, like RED and RESET. | Lesson 46 |
| `credits` | The exact name of the function you will write. Real games list who made them at the end. | Lesson 50 |
| `current` | The variable holding the hero's location at this moment. This lesson uses the name current. | Lesson 43 |
| `def` | The keyword that defines a function. | Lesson 10 |
| `default` | A value a parameter falls back to when no argument is given. You write it with = in the def line. | Lesson 12 |
| `defender` | The fighter being hit. It has defense. | Lesson 39 |
| `defense` | How much damage this fighter shrugs off. | Lesson 39 |
| `define` | To create a function using the def keyword. Defining does not run it; it only teaches Python the recipe. | Lesson 11 |
| `description` | A short piece of text saying what the item is. | Lesson 34 |
| `dictionary` | A collection that stores pairs of label and value, written with curly brackets: {"health": 100}. | Lesson 15 |
| `docstring` | A short string just under def that says what the function does. | Lesson 10 |
| `DRY` | A rule real programmers follow: Don't Repeat Yourself. If you are copying code, write a function instead. | Lesson 14 |
| `element` | One single item inside a list. | Lesson 7 |
| `enumerate()` | A built-in that walks a list and hands you both the position number and the element at the same time. | Lesson 7 |
| `equipped` | The weapon a hero is currently holding. It may be None if they have nothing. | Lesson 38 |
| `escape sequence` | Two characters starting with a backslash that mean something special inside a string. | Lesson 3 |
| `evaluate` | What Python does to an expression: it works out the answer before storing or printing it. | Lesson 4 |
| `except` | Catches the problem and runs your rescue code instead of crashing. | Lesson 24 |
| `exception` | An error that happens while the program is running, such as trying to turn "banana" into a number. | Lesson 24 |
| `exits` | The directions you can travel from a place, and where each one leads. | Lesson 42 |
| `expression` | A piece of code that works out to a single value, like hero_attack - monster_defense. | Lesson 4 |
| `f-string` | A string with an f in front of it. Inside it you can put a variable in curly brackets {} and Python swaps in the value for you. | Lesson 2 |
| `file` | A place on disk where information is kept permanently. | Lesson 25 |
| `FileNotFoundError` | The exception Python raises when the file is not there. | Lesson 26 |
| `flag` | A True or False value recording whether something has happened. Here it records whether a quest is finished. | Lesson 48 |
| `flee` | The exact name of the function you will write. | Lesson 40 |
| `floor` | A lowest allowed value. Here the floor is 1: however strong the armour, a hit always does at least 1. | Lesson 39 |
| `for` | Repeats once for each item in a collection. | Lesson 9 |
| `format spec` | Extra instructions after a colon inside the brackets, controlling width or decimal places. | Lesson 30 |
| `function` | A named piece of code that does one job. You create it with def and use it by writing its name with brackets. | Lesson 10 |
| `game loop` | The repeating heart of a game: show the situation, take an action, update the state, repeat. | Lesson 43 |
| `gold_reward` | How much gold the hero wins for defeating it. | Lesson 37 |
| `graceful` | Handling a problem without crashing. A brand new player has no save file, and that is not an error. | Lesson 45 |
| `heal_amount` | How much health a Potion restores. | Lesson 35 |
| `hero` | The variable holding your Hero object. The test looks for this exact name. | Lesson 49 |
| `if` | A keyword that runs some code only when something is true. | Lesson 6 |
| `immutable` | Cannot be changed after it is made. Tuples are immutable; lists are not. | Lesson 18 |
| `import` | The keyword that brings a module into your program. | Lesson 27 |
| `in` | Asks whether a key exists in a dictionary. Always check before looking something up. | Lesson 41 |
| `index` | The position of an element. Python counts from 0, so the first element is at index 0, not 1. | Lesson 7 |
| `inheritance` | When one class receives the abilities of another, instead of copying the code. | Lesson 19 |
| `input()` | A built-in instruction that stops and waits for the player to type something and press Enter. Whatever they typed comes back as a string. | Lesson 6 |
| `instance attribute` | A value set on self inside __init__. Each object gets its own copy. | Lesson 21 |
| `int()` | Turns text into a whole number, when it can. | Lesson 24 |
| `integer` | A whole number with no decimal point, like 100 or 50. Programmers say "int" for short. | Lesson 2 |
| `integration` | Joining separate parts into one working program. | Lesson 49 |
| `inventory` | The list of things a hero is carrying. | Lesson 33 |
| `is-a` | The test for whether inheritance is right. A Weapon is-a Item, so Weapon(Item) makes sense. | Lesson 22 |
| `is_alive()` | The method you will write. Methods that answer a question are usually named starting with is_ or has_. | Lesson 32 |
| `item_key` | The name used to look an item up in the shop, such as "sword" or "potion". | Lesson 41 |
| `iterate` | The proper word for going through a collection one item at a time. | Lesson 9 |
| `JSON` | A standard text format for storing structured data. Nearly every program in the world understands it. | Lesson 27 |
| `json.dump()` | Writes a Python dictionary into an open file. | Lesson 27 |
| `json.load()` | Reads it back out again as a real dictionary. | Lesson 27 |
| `key` | The label you look something up by, like "health". | Lesson 15 |
| `list` | A variable that holds many values in order, written with square brackets: ["sword", "shield"]. | Lesson 7 |
| `load_game()` | The function you will write. It reads the save file and gives the data back. | Lesson 45 |
| `loop` | Code that runs more than once. | Lesson 9 |
| `loop variable` | The name between for and in. Each time round, Python puts the next item into it. | Lesson 13 |
| `max()` | A built-in that gives the larger of two numbers. max(x, 0) is the neat way to stop a value going negative. | Lesson 37 |
| `max_health` | The most health this hero can ever have. Current health goes up and down; max_health does not. | Lesson 32 |
| `method` | An instruction that belongs to a value and is written after a dot, like monster_name.upper(). | Lesson 5 |
| `min()` | A built-in that gives the smaller of two numbers. It is the neat way to stop healing past maximum. | Lesson 36 |
| `mode "r"` | Read mode. Opens an existing file to look at it. | Lesson 26 |
| `mode "w"` | Write mode. Creates the file, or empties it first if it already exists. | Lesson 25 |
| `module` | A ready-made bundle of code you can borrow. | Lesson 27 |
| `mutate` | To change an object's state, for example lowering its health when it is hit. | Lesson 20 |
| `nested` | A dictionary inside another dictionary. Your exits live nested inside each place. | Lesson 42 |
| `None` | What a function gives back when it has no return line. It means "nothing here". | Lesson 16 |
| `object` | An actual thing built from the blueprint. Also called an instance. | Lesson 17 |
| `objectives` | A list of the quests in your game. This lesson uses that exact name. | Lesson 48 |
| `open()` | Opens a file so you can use it. You say the filename and the mode. | Lesson 25 |
| `operator` | A symbol that does something to values. + adds, - subtracts, * multiplies, / divides. | Lesson 4 |
| `optional` | A parameter with a default. The caller may supply it or skip it. | Lesson 12 |
| `or` | Joins two conditions. True when EITHER side is True. | Lesson 8 |
| `override` | When a child class replaces a method it inherited with its own version. | Lesson 19 |
| `parameter` | A name in the function's brackets that stands for information the function needs. | Lesson 10 |
| `per-object` | Each hero needs their OWN list. Two heroes must never share one bag. | Lesson 33 |
| `placeholder` | The {} part inside an f-string. | Lesson 30 |
| `price` | The name this lesson uses for how much an item costs. | Lesson 23 |
| `print()` | A built-in instruction that shows something on the screen. The round brackets () hold the thing you want to show. | Lesson 1 |
| `print_header()` | The function you will write to display a framed title. | Lesson 49 |
| `probability` | How likely something is. Comparing a random number against your chance is how you roll for it. | Lesson 40 |
| `program` | A list of instructions for the computer, written in order from top to bottom. | Lesson 1 |
| `prompt` | The message you show inside input() so the player knows what to type. | Lesson 6 |
| `random` | A module of functions that produce unpredictable results. | Lesson 28 |
| `random.randint(1, 6)` | Gives a whole number from 1 to 6. Unlike range(), both ends are included. | Lesson 28 |
| `random.random()` | Gives a decimal from 0.0 up to just below 1.0. | Lesson 40 |
| `range(3)` | A built-in that counts for you: 0, then 1, then 2. It stops before the number you give it. | Lesson 13 |
| `required` | A parameter with no default. It must always be given. | Lesson 12 |
| `RESET` | The code that turns the color back to normal. Without it, everything printed afterwards stays colored. | Lesson 46 |
| `return` | Sends a value back to whoever called the function. | Lesson 10 |
| `reuse` | Using the same function again instead of writing new copies of the same code. | Lesson 14 |
| `run` | To make the computer actually do your instructions. | Lesson 1 |
| `save_game()` | The function you will write. It takes the hero and their location and writes them to disk. | Lesson 44 |
| `savegame.json` | The file your game saves into. | Lesson 44 |
| `self` | The word a class uses to mean "this particular object". It is always the first parameter. | Lesson 17 |
| `separator` | Another line below the title, dividing it from what comes next. | Lesson 47 |
| `serialise` | To turn objects into plain data (numbers, strings, lists, dictionaries) that a file can hold. | Lesson 44 |
| `ship` | What programmers say when a project is finished and handed to real people. | Lesson 50 |
| `shop` | A dictionary of prices, where each key is an item name and each value is what it costs. | Lesson 41 |
| `simulate` | To model something in code, like rolling dice or fighting several rounds. | Lesson 28 |
| `state` | The current values stored on an object, such as how much health a goblin has left right now. | Lesson 20 |
| `string` | Text in a program. You wrap text in quote marks so Python knows it is words and not code, like "Hello". | Lesson 1 |
| `subclass` | The more specific class. Here, Weapon is a subclass of Item, because every weapon IS an item. | Lesson 22 |
| `super()` | A built-in that means "the parent class". You use it to call the parent's version of a method. | Lesson 23 |
| `super().__init__(...)` | Runs the parent's setup code from inside the child's own __init__. | Lesson 23 |
| `suspense` | The effect you get by pausing between messages, which makes a game feel alive. | Lesson 29 |
| `time` | A module for working with time. | Lesson 29 |
| `try` | Marks code that might go wrong. | Lesson 24 |
| `tuple` | A collection written with round brackets: ("Sword", 25). Like a list, but frozen. | Lesson 18 |
| `unarmed` | A hero with no weapon. They still deal 1 damage. | Lesson 38 |
| `unpacking` | Pulling a tuple apart into separate variables in one line: name, price = weapon | Lesson 18 |
| `update` | To replace the old value with the new one, as in current = move(world, current, "north") | Lesson 43 |
| `value` | The information stored under that key, like 100. | Lesson 15 |
| `ValueError` | The specific exception Python raises when a value is the wrong sort of thing. int("banana") raises it. | Lesson 24 |
| `variable` | A name that holds a value, like a labelled box. You put something in the box now and open it later. | Lesson 2 |
| `while` | Repeats for as long as a condition stays True. | Lesson 9 |
| `with` | A safety net. It closes the file for you, even if something goes wrong. | Lesson 25 |
| `world` | A dictionary where each key is a place name and each value describes that place. | Lesson 42 |

## Style rules real programmers follow

These habits are introduced one lesson at a time and used for the rest of
the course.

| Rule | Why | Taught in |
|---|---|---|
| `snake_case` for variables and functions, saying what they hold | `hero_health` reads clearly; `hh` does not | Lesson 2 |
| Comments explain *why*, not *what* | The code already says what it does | Lesson 3 |
| Every function gets a docstring, and does one job | Makes functions reusable and understandable | Lesson 10 |
| Prefer `return` over printing inside a function | A returned value can be reused anywhere | Lesson 16 |
| `PascalCase` for class names | Instantly distinguishes `Hero` the class from `hero` the object | Lesson 17 |
| Catch a specific exception, never a bare `except:` | A bare except hides real bugs | Lesson 24 |
| Use `with open(...) as f:` | Closes the file for you, even if something breaks | Lesson 25 |
| Constants in `UPPER_CASE` | Signals a value that never changes | Lesson 46 |
| Don't Repeat Yourself (DRY) | If you are copying code, write a function instead | Lessons 14, 44 |
