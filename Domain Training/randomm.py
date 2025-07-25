import random  
colors = ['red', 'blue', 'green', 'yellow']
print("Random color:", random.choice(colors))

random.shuffle(colors)

print("Random sample of 2 colors:", random.sample(colors,2))