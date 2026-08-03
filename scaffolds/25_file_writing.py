r"""
Lesson 25: File Writing - Saving Something Forever
===================================================

WHAT YOU'LL LEARN
  How to write information into a file on the computer, so it is
  still there after your program closes.

NEW WORDS
  file         A place on disk where information is kept permanently.
  open()       Opens a file so you can use it. You say the filename
               and the mode.
  mode "w"     Write mode. Creates the file, or empties it first if
               it already exists.
  .write()     Puts text into the open file.
  with         A safety net. It closes the file for you, even if
               something goes wrong.

HOW IT WORKS
  with open("save.txt", "w") as f:
      f.write("Musab\n")
      f.write("120\n")

  Read it as: "open save.txt for writing, call it f, and inside this
  indented block write these lines." When the block ends, Python
  closes the file automatically.

  The \n at the end of each write starts a new line in the file.
  Without it everything runs together on one line.

  .write() only accepts strings. To save a number, wrap it in str()
  or build the text with an f-string.

YOUR TASK
  Step 1: Create two variables named player_name and player_gold.
  Step 2: Use with open("save.txt", "w") to write both values into
          the file save.txt, each on its own line.

EXAMPLE
  This example saves a high score, so you still write your own player
  details.

      score = 900
      with open("highscore.txt", "w") as f:
          f.write("Ada\n")
          f.write(f"{score}\n")

WHEN IT WORKS YOU'LL SEE
  Nothing appears on screen, but a file named save.txt now exists
  containing:

      Musab
      120

IF YOU GET STUCK
  TypeError: write()   -> you passed a number. Use str(number) or an
  argument must be str    f-string.
  Everything on one    -> add \n at the end of each line you write.
  line
  File is empty        -> writing happens inside the with block. Check
                          your indentation.

STYLE
  Always use with open(...) as f. It closes the file for you, so you
  can never forget and leave a file half-written.

CHECK YOUR WORK
  python run_lesson.py 25
"""

# TODO: Write your code for Lesson 25 below this line.
