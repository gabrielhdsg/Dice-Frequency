from die import Die
import pygal

#Create a eight-sided die
sides = 8
die_1 = Die(sides)
die_2 = Die(sides)

#Roll the die and store its values
results = []
rolls = 100000
for num in range(rolls):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analizing the result
frequencies=[]
max_result = sides * 2
for value in range(2,max_result+1):
    frequecy = results.count(value)
    frequencies.append(frequecy)

#Visualize the results
hist = pygal.Bar()

#Histogram configurations
hist.title = "Results of rolling two dice " + str(rolls) + " times"
hist.x_labels = list(range(2,max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('Die 1 + Die 2', frequencies)
hist.render_to_file('die_visual.svg')
