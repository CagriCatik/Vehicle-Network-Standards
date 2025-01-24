import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Failure Mode': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Old RPN': [592, 576, 729, 810, 680, 380, 596, 700, 812, 504],
    'New RPN': [160, 225, 378, 108, 81, 168, 126, 105, 160, 200]
}

df = pd.DataFrame(data)

# Number of variables
categories = list(df['Failure Mode'])
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variables)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()

# The radar chart is a circle, so we need to "complete the loop", and append the start to the end.
angles += angles[:1]

# Values
old_rpn = df['Old RPN'].tolist()
old_rpn += old_rpn[:1]

new_rpn = df['New RPN'].tolist()
new_rpn += new_rpn[:1]

# Plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.fill(angles, old_rpn, color='red', alpha=0.25)
ax.fill(angles, new_rpn, color='blue', alpha=0.25)

ax.plot(angles, old_rpn, color='red', linewidth=2, label='Old RPN')
ax.plot(angles, new_rpn, color='blue', linewidth=2, label='New RPN')

# Labels for each point
plt.xticks(angles[:-1], categories)

# Title and legend
plt.title('Failure Modes (Risk Priority Number) Comparison', size=20, color='black', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.show()
