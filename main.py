from die import Die

#Create a eight-sided die
die_1 = Die(8)

#Roll the dice and store its values
results = []
for num in range(1000):
    results.append(die_1.roll())

#Analizing the result
frequencies=[]
for value in range(1,die_1.sides):
    unique_frequecy = results.count(value)
    frequencies.append(unique_frequecy)

print(frequencies)