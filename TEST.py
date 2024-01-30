import numpy as np
import matplotlib.pyplot as plt

data = [[ 66386, 174296,  75131, 577908,  32015],
        [ 58230, 381139,  78045,  99308, 160454],
        [ 89135,  80552, 152558, 497981, 603535],
        [ 78415,  81858, 150656, 193263,  69638],
        [139361, 331509, 343164, 781380,  52269]]
columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]

cell_text = [['%.1f' % (x / 1000.0) for x in row] for row in data]

fig, ax = plt.subplots()

# Turn off the axis
ax.axis('off')

# Add a table
the_table = ax.table(cellText=cell_text,
                      rowLabels=rows,
                      colLabels=columns,
                      loc='center')

# Set the title and label of the x-axis to empty strings
ax.set_title('')
ax.set_xlabel('')

plt.show()