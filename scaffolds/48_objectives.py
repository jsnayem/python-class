"""
Lesson 48: Objectives - A Quest Checklist
==========================================

WHAT YOU'LL LEARN
  How to store a list of quests with a done-or-not flag, and print
  them as a tidy checklist.

NEW WORDS
  objectives   A list of the quests in your game. This lesson uses
               that exact name.
  tuple        A small fixed group of values in round brackets. Each
               objective is a tuple of (description, done).
  flag         A True or False value recording whether something has
               happened. Here it records whether a quest is finished.
  unpacking    Splitting a tuple into separate names inside a loop:
               for text, done in objectives

HOW IT WORKS
  objectives = [
      ("Find the sword", True),
      ("Defeat the dragon", False),
  ]

  Each entry pairs the quest text with a flag. A tuple is right here
  because those two values belong together and should not drift
  apart. You need at least one True and one False so the checklist
  has something to show in both states.

      def show_objectives(objectives):
          for text, done in objectives:
              mark = "[x]" if done else "[ ]"
              print(f"{mark} {text}")

  The loop unpacks each tuple into text and done. The mark line
  chooses between two symbols, so finished and unfinished quests look
  clearly different at a glance.

YOUR TASK
  Step 1: Create a list named objectives holding tuples of
          (description, done). Include at least one finished quest
          and one unfinished one.
  Step 2: Define a function named show_objectives that takes
          objectives and prints every quest.
  Step 3: Mark finished and unfinished quests differently, for
          example with [x] and [ ], then call show_objectives.

EXAMPLE
  This example is a chore chart, so you still write your own quest
  list.

      chores = [("Tidy room", True), ("Walk dog", False)]

      def show_chores(chores):
          for text, done in chores:
              print(("[x] " if done else "[ ] ") + text)

      show_chores(chores)

WHEN IT WORKS YOU'LL SEE
  [x] Find the sword
  [ ] Defeat the dragon

IF YOU GET STUCK
  ValueError: too many  -> each objective must be a tuple of exactly
  values to unpack         two things.
  Everything looks the  -> your mark must differ for True and False.
  same
  The test wants both   -> include at least one True and one False
  states                   objective in the list.

CHECK YOUR WORK
  python run_lesson.py 48
"""

# TODO: Write your code for Lesson 48 below this line.
