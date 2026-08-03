"""Lesson 9: Loops
===============
Step 1: Use while loop to count 1 to 5
Step 2: Use for loop over inventory items
Step 3: Simulate combat rounds while health > 0
Step 4: Test your code
  Run: python run_lesson.py 9
"""
count = 1
while count <= 5:
    print(count)
    count += 1
inventory = ["Health Potion", "Iron Sword"]
for item in inventory:
    print(item)
health = 50
rounds = 0
while health > 0:
    health -= 10
    rounds += 1
    if health <= 0:
        break
print(f"Combat ended after {rounds} rounds")
