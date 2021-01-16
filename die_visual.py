from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die 

# create two D6 dice
die_1 = Die()
die_2 = Die()
n_rolls = 50_000

# make some rolls, and store results in list

# with for loop
# results = []
# for roll_num in range(n_rolls):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# with list comprehension
results = [die_1.roll() + die_2.roll() for roll_num in range(n_rolls)]

# analyze the results

# with for loop
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# with list comprehension
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

print(frequencies)

# visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling two D6 dice {n_rolls} times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
