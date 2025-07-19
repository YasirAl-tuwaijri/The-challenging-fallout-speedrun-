import random

choices1 = ["Yes man ", "legion", "House", " NCR (on very easy mode because they take a lot of time comparing to the others)",]
draw1 = random.choice(choices1)
print("First random:", draw1)

# Randomizng the companion choice (they should be with you until the ending unless they lefft you beacuse your ending choices)
choices2 = [" Arcade", " Ed-E", " Rex", " Cass", " Boone", " Lily", " Raul", " Veronica"]
draw2 = random.choice(choices2)
print("Second random:", draw2)
# Randomizng the challenge while speed running
choices3 = [" No gambling", " Killing a deathclaw without loading a save", " doing enclave side quest", " doing BoS side quest"]
draw3 = random.choice(choices3)
print("third random:", draw3)
