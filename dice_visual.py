from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline



class Die:
    """A class representing a single die"""
    def __init__(self,num_sides=6):
        """Assume a six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1,self.num_sides)

die_1 = Die()
die_2 = Die(10)

# make some rolls and store the results in a list. 
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# let's analyze the results 
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2,max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)

# Visualize the results 
x_values = list(range(2,max_results+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title': 'Result','dtick':1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 dice 50000 times',xaxis=x_axis_config,yaxis=y_axis_config)

offline.plot({'data': data,'layout': my_layout},filename='d6_d10.html')