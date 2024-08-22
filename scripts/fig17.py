''' Required packages. Use python3 -m pip install xxx for all the packages. '''
import pandas as pd
import numpy as np
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
import easypyplot
import math

csv_path = './results/fig17.csv'
with open('./results/pimpam_time.txt', 'r') as f:
    times = f.readlines()
    pimpam_time = []
    for i in range(6):
        pimpam_time.append(times[i*5])
        pimpam_time.append(times[i*5+1])
    pimpam_time = [float(x.strip()) for x in pimpam_time]
    pimpam_time = [math.log10(x*1e6) for x in pimpam_time]

with open('./scripts/khuzdul_time.txt', 'r') as f:
    khuzdul_time = f.readlines()
    khuzdul_time = [float(x.strip()) for x in khuzdul_time]
    khuzdul_time = [math.log10(x*1e6) for x in khuzdul_time]

dataset_list = ['WV', 'PP', 'AP', 'YT', 'PT', 'LJ']
with open(csv_path, 'w') as f:
    f.write('Name,Khuzudal,MyMiner\n')
    for graph in dataset_list:
        for pattern in ['CLIQUE3', 'CLIQUE4']:
            f.write(graph + '-' + pattern + ',')
            f.write(','.join([str(x) for x in [khuzdul_time.pop(0), pimpam_time.pop(0)]]) + '\n')

''' Plot knobs. Change only if you want to resize the graph, etc. '''
fig_bar_width = 7
fig_dims = (3.6, 1.6)
fig_label_fontsize = 9
ft = fm.FontProperties('Times New Roman')
ft.set_size(fig_label_fontsize)

# plt.rcParams['text.usetex'] = True #Let TeX do the typsetting

''' [TODO] Figure properties. Specify the csv file and corresponding columns. '''
csv_hd = pd.read_csv(csv_path, sep=',')

fig_title = 'Execution Time (μs)' # TODO: figure title, shown as y-axis label
fig_name = 'fig17' # TODO: figure name, used as pdf name

dataset_list = ['WV', 'PP', 'AP', 'YT', 'PT', 'LJ']

workload_list = csv_hd["Name"].to_list()
scheme_list = ['Khuzudal', 'MyMiner'] # TODO: list of all schemes in the breakdown. Each column corresponds with one scheme
patternd_dict = {'CLIQUE3':'C3',
                 'CLIQUE4':'C4',
                 'CLIQUE5':'C5',
                 "CYCLE4":'R4',
                 'HOUSE5':'H5',
                 'TRI_TRI6':"T6"}
workload_dict = {item: patternd_dict[(item.split("-"))[1]] for item in workload_list} # Change the mapping if you want a different figure label text instead of the csv column name
print(workload_dict)
scheme_dict = {item: item for item in scheme_list}
scheme_dict['MyMiner'] = 'PimPam'
# scheme_dict['GPU'] = 'Pangolin'

fig_ylim = (0, 9) # TODO: y-axis range. Align with your data
fig_yticks = list(np.arange(fig_ylim[0], fig_ylim[1], 2))


fig_bar_colors = ['#f99b7d', '#a6d0d0'] # TODO: choose enough colors for schemes
all_colors = [easypyplot.color.COLOR_SET[i] for i in range(len(easypyplot.color.COLOR_SET))]
print(all_colors)
assert len(fig_bar_colors) == len(scheme_dict)

print("Expect {} groups and {} entries within each group".format(len(workload_dict), len(scheme_dict)))

''' Load data from file. '''
# TODO assert workload_name
# TODO assert scheme_name
fig_xlabels = []
fig_xticks = []
fig_data_2darr = []
xtick = -4.5
for idx, row in csv_hd.iterrows():
    workload_fullname = row[0]
    if any(workload in workload_fullname for workload in workload_list):
        row_value = []
        for col in scheme_list:
            # print(col)
            if any(scheme in col for scheme in scheme_dict):
                row_value.append(row[col])
        fig_data_2darr.append(row_value)
        fig_xlabels.append(workload_dict[workload_fullname])
        xtick += 11
        fig_xticks.append(xtick)
assert len(fig_data_2darr) == len(fig_xlabels) == len(fig_xticks)

print(fig_data_2darr)

''' Ploting script '''
pp, fig = easypyplot.pdf.plot_setup(fig_name, fig_dims)
# ax = fig.gca() # Only used with no subplot mode
fig_ax = fig.add_subplot(1, 1, 1) # Knob: plot the first subgraph of a 1x1 grid, i.e., no subplot mode
easypyplot.format.turn_off_box(fig_ax)

fig_h = easypyplot.barchart.draw(
    fig_ax, fig_data_2darr,
    width=fig_bar_width,
    breakdown=False,
    group_names=fig_xlabels,
    xticks=fig_xticks,
    xticklabelfontsize=fig_label_fontsize,
    # xticklabelrotation=25, # Knob: rotated x tick labels
    colors=fig_bar_colors)

print(fig_xticks)
''' x axis '''
# fig_ax.xaxis.set_tick_params(pad=0) # Knob: distance between x tick label and x-axis
fig_ax.set_xlim([fig_ax.get_xticks()[0] - 6.5, fig_ax.get_xticks()[-1] + 6.5])
fig_ax.set_xticks(fig_xticks)
fig_ax.set_xticklabels(fig_xlabels, fontsize=fig_label_fontsize, fontproperties=ft)
fig_ax.xaxis.set_ticks_position('none') # Knob: uncomment for visible x ticks
# ax.tick_params(direction='in') # Knob: [in, out, inout]

next_ticks = []
print(len(fig_xticks))
for i in range(0,6):
    next_ticks.append((fig_xticks[i*2] + fig_xticks[(i+1)*2-1])/2+0.02)
print(next_ticks)
fig_ax.set_xticks(next_ticks, minor=True)
# fig_ax.set_xticks([28.1, 83, 138, 193, 248, 303], minor=True)
fig_ax.set_xticklabels(dataset_list, fontsize=fig_label_fontsize, fontproperties=ft, minor=True)

fig_ax.tick_params(axis='x', which='major', pad=0)
fig_ax.tick_params(axis='x', which='minor', pad=10)
# fig_ax.grid(which='minor', axis='x', linestyle='--')


line_ticks = []
for i in range(0,5):
    line_ticks.append((fig_xticks[(i+1)*2-1] + fig_xticks[(i+1)*2])/2+0.02)
for tick in line_ticks:
    fig_ax.axvline(tick, color='k', linestyle='--', linewidth=0.4, ymin=-0.35, ymax=0 ,clip_on=False)

# for tick in next_ticks:
#     fig_ax.axhline(0, color='k', linestyle='--', linewidth=0.5, xmin=tick / 13, xmax=(tick + 2) / 13, clip_on=False)

''' y axis '''
fig_ax.yaxis.set_tick_params(pad=0) # Knob: distance between y tick label and y-axis
# easypyplot.format.set_axis_to_percent(fig_ax.yaxis) # Uncomment for y axis tick label in xx% formatwer limits as per your requirement

# Apply the formatter to the y-axis

fig_ax.yaxis.grid(True)
fig_ax.set_ylim(fig_ylim)
fig_ax.set_yticks(fig_yticks)
print(fig_yticks)
# fig_yticks_label = ["{:.0f}".format(item) for item in fig_yticks] # Change for customized y tick label text
fig_yticks_label = ["$10^{:.0f}$".format(item) for item in fig_yticks] # Change for customized y tick label text
fig_yticks_label[0] ='0'
# fig_yticks_label = [item for item in fig_yticks] # Change for customized y tick label text
fig_ax.set_yticklabels(fig_yticks_label, fontsize=fig_label_fontsize, fontproperties=ft)
fig_ax.set_ylabel(fig_title, multialignment='center', fontproperties=ft)

''' values on top of each bar '''
# for group_id in range(len(workload_dict)):
#     for entry_id in range(len(scheme_dict)):
#         bar_value = fig_data_2darr[group_id][entry_id]
#         bar_x = fig_ax.get_xticks()[group_id] + fig_bar_width / len(scheme_dict) * (entry_id - len(scheme_dict) / 2)
#         bar_text = str('{:.2f}'.format(bar_value))
#         fig_ax.text(bar_x, bar_value + 0.1, bar_text, ha='left', va='top',
#                 fontsize=fig_label_fontsize,
#                 # rotation=90,
#                 fontproperties=ft,
#                 )

''' legend '''
legend = [scheme_dict[item] for item in scheme_dict]
print(legend)
fig.legend(fig_h, legend, loc='upper center', frameon=False, prop=ft,
        bbox_to_anchor=(0.5, 1.05),
        ncol=3,
        columnspacing=1.5, # padding between columns
        labelspacing=0, # padding between rows
        )

''' last resize '''
plt.yticks(fontproperties='Times New Roman', size=9)
plt.tight_layout()
easypyplot.format.resize_ax_box(fig_ax, hratio=0.8)
# plt.show()

''' Save figures'''
fig.savefig('./reproduce/'+fig_name+'.pdf', format="pdf", bbox_inches = 'tight')
# easypyplot.pdf.plot_teardown(pp) # BUG: it sometimes generates wierd chopped pdf figures
# fig.savefig(fig_name+'.svg', format="svg", bbox_inches = 'tight', transparent=False) # svg format

