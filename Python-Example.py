import random

# Our list of bars
bars = ["Lion's Head Tavern",
        "The Hamilton",
        "1020 Bar",
        "Amsterdam Tavern",
        "The Heights",
        "The Dead Poet",
        "Prohibition"]

# Our list of friends
people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Alexander Hamilton",
          "Samule L. Jackson",
          "A 4 Apollo"]

random_bar = random.choice(bars)
random_person = random.choice(people)
random_person_one = random.choice(people)

print(f"How about you go to {random_bar} with {random_person} and {random_person_one}?")
