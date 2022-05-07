import matplotlib.pyplot as plt
import numpy as np
# Part 1
'''
import csv

x = []
y = []

with open('example.TXT', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='Loaded from file!')
'''

x, y = np.loadtxt('samplefile.txt', delimiter=',', unpack=True)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(x, y)

bbox_props = dict(boxstyle='larrow', fc='w', ec='k', lw=1)
ax1.annotate(str(y[-1]), (x[-1], y[-1]),
             xytext=(x[-1]+0.5, y[-1]), bbox=bbox_props)

# # Annotation example with arrow
# ax1.annotate('Big News!', (x[5], y[5]),
#              xytext=(0.8, 0.9), textcoords='axes fraction',
#              arrowprops=dict(color='grey'))
# # Font dict example
# font_dict = {
#             'family': 'serif',
#             'color': 'darkred',
#             'size': 15}
# # Hard coded text
# ax1.text(4, 4, 'Text example', fontdict=font_dict)
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.90, top=0.90, wspace=0.2, hspace=0)
plt.show()
