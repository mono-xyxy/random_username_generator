import random

adjectives =[
    "cool", "fast", "happy", "smart", "silent",
    "brave", "wild", "bright", "shadow", "frozen"
]

nouns=[
    "tiger", "eagle", "ninja", "coder", "dragon",
    "warrior", "hunter", "lion", "phoenix", "wolf"
]

print("Random Username Generator")

count=int(input("How many usernames do you want? "))

print("\nGenerated usernames: ")

for _ in range(count):
    username = random.choice(adjectives)+random.choice(nouns)+str(random.randint(1,999))
    print(username)