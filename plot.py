import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

ticks = [['Density', 'Green spaces', 'Public Transport', 'Traffic', 'Security', 'Sunshine Hours'], 
         ['Air Pollution', 'Noise Pollution', 'Light Pollution'], 
         ['Unemployment', 'Debt per Capita', 'Social Security', 'Family Purchase Power'], 
         ['Mental Health', 'Physical Health', 'Gender Equality', 'Race Equality']]
top10 = [[3.028, 2.015, 3.145, 4.016, 2.231, 7.318], 
         [3.028, 7.178, 7.592], 
         [4.533, 3.389, 2.837, 1.996], 
         [1.652, 4.935, 3.006, 3.166]]
seoul = [[9.4, 7.22, 3.9, 4.2, 3.9, 4.81], 
         [5.86, 9.21, 9.09], 
         [3.48, 1.3, 9.34, 9.03], 
         [9.7, 1.7, 8.61, 10]]


fig, axes = plt.subplots(nrows=1, ncols=4, sharey=True, figsize=(12, 6), gridspec_kw={'width_ratios':[4, 1, 2.5, 2.5]})

width = 0.3

for i in range(4):
    if i !=0:
        axes[i].tick_params(axis='y', which='both', left=False)
    ind = np.arange(len(top10[i]))
    axes[i].grid(which='major',  axis='y', linestyle='--')
    axes[i].tick_params(axis='x', rotation=70)
    axes[i].set_xticks(ind)
    axes[i].set_xticklabels(ticks[i])
    axes[i].bar(ind-width/2, top10[i], width)
    axes[i].bar(ind+width/2, seoul[i], width)

plt.subplots_adjust(wspace=0)
plt.show()
    