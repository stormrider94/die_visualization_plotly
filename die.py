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

die = Die()

# make some rolls and store the results in a list. 
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


# let's analyze the results 
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)

# Visualize the results 
x_values = list(range(1,die.num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',xaxis=x_axis_config,yaxis=y_axis_config)

offline.plot({'data': data,'layout': my_layout},filename='d6_1.html')