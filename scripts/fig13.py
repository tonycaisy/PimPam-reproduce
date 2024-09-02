import matplotlib.pyplot as plt
import re
import numpy as np
from collect_data import collect_data
import matplotlib.pyplot as plt

# regular expression for matching number
num_re = re.compile(r"\d+")

if True:
    # Read data from file
    deg, o_deg, ans, cycle, dpu_cycle = collect_data("./results/accuracy_C4.txt")
    deg = np.array(deg)
    o_deg = np.array(o_deg)
    ids = np.array(range(1, len(deg)+1))

    # Plot data as log-log plot
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(o_deg*o_deg*o_deg+100, cycle, s=1, label="cycle")
    plt.yticks(fontproperties='Times New Roman', size=20)
    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.xlabel("Predicted execution cycles", fontsize=30, fontproperties='Times New Roman')
    plt.ylabel("Execution cycles", fontsize=30, fontproperties='Times New Roman')
    plt.xlim(0, 80000000)
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.xaxis.get_offset_text().set_position(xy=(1.1,2.0))
    ax.xaxis.get_offset_text().set_fontsize(20)
    ax.xaxis.get_offset_text().set_fontname('Times New Roman')
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontname('Times New Roman')

    # plot log-linear plot
    plt.subplot(1, 2, 2)
    plt.plot(range(len(dpu_cycle)), dpu_cycle, "o", markersize=1, label="cycle")
    plt.yticks(fontproperties='Times New Roman', size=20)
    plt.xticks([10000,20000,30000,40000],fontproperties='Times New Roman', size=20)
    plt.xlabel("DPU hardware thread ID", fontsize=30, fontproperties='Times New Roman')
    plt.ylabel("Execution cycles", fontsize=30, fontproperties='Times New Roman')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontname('Times New Roman')

    plt.tight_layout()
    print("clique4-predict.png")
    plt.savefig("./reproduce/fig13-1.png",format="png",bbox_inches = 'tight',dpi=1000)

# -------------------------------------------------------------------------------------------

# Read data from file
deg, o_deg, ans, cycle, dpu_cycle = collect_data("./results/accuracy_R4.txt")
deg = np.array(deg)
o_deg = np.array(o_deg)
ids = np.array(range(1, len(deg)+1))

# Plot data as log-log plot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(o_deg*o_deg+100, cycle, s=1, label="cycle")
plt.yticks(fontproperties='Times New Roman', size=20)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.xticks([40000,80000,120000,160000,200000],fontproperties='Times New Roman', size=20)
plt.xlabel("Predicted execution cycles", fontsize=30, fontproperties='Times New Roman')
plt.ylabel("Execution cycles", fontsize=30, fontproperties='Times New Roman')
plt.xlim(0, 200000)
#plt.legend()
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
print(ax.xaxis.get_offset_text().get_position())
# ax.xaxis.offset_text_position = "top"
print(type(ax.xaxis.get_offset_text()))
print(ax.xaxis.get_offset_text())
ax.xaxis.get_offset_text().set_position(xy=(1.1,2.0))
# ax.xaxis.get_offset_text().set_y(2.0)
ax.xaxis.get_offset_text().set_fontsize(20)
ax.xaxis.get_offset_text().set_fontname('Times New Roman')
ax.yaxis.get_offset_text().set_fontsize(20)
ax.yaxis.get_offset_text().set_fontname('Times New Roman')

# plot log-linear plot
plt.subplot(1, 2, 2)
plt.plot(range(len(dpu_cycle)), dpu_cycle, "o", markersize=1, label="cycle")
plt.yticks(fontproperties='Times New Roman', size=20)
plt.xticks([10000,20000,30000,40000], fontproperties='Times New Roman', size=20)
plt.xlabel("DPU hardware thread ID", fontsize=30, fontproperties='Times New Roman')
plt.ylabel("Execution cycles", fontsize=30, fontproperties='Times New Roman')
#plt.legend()
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.yaxis.get_offset_text().set_fontsize(20)
ax.yaxis.get_offset_text().set_fontname('Times New Roman')

plt.tight_layout()
print("cycle4-predict.png")
plt.savefig("./reproduce/fig13-2.png",format="png",bbox_inches = 'tight',dpi=1000)

# -------------------------------------------------------------------------------------------

if True:
    # Read data from file
    deg, o_deg, ans, cycle, dpu_cycle = collect_data("./results/accuracy_T6.txt")
    deg = np.array(deg)
    o_deg = np.array(o_deg)
    ids = np.array(range(1, len(deg)+1))

    # Plot data as log-log plot
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.scatter(o_deg*o_deg*deg+100, cycle, s=1, label="cycle")
    plt.yticks(fontproperties='Times New Roman', size=20)
    plt.xticks(fontproperties='Times New Roman', size=20)
    plt.xlabel("Predicted execution cycles", fontsize=30, fontproperties='Times New Roman')
    plt.ylabel("Execution cycles", fontsize=30, fontproperties='Times New Roman')
    plt.xlim(0, 80000000)
    #plt.legend()
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.xaxis.get_offset_text().set_position(xy=(1.1,2.0))
    ax.xaxis.get_offset_text().set_fontsize(20)
    ax.xaxis.get_offset_text().set_fontname('Times New Roman')
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontname('Times New Roman')

    # plot log-linear plot
    plt.subplot(1, 2, 2)
    plt.plot(range(len(dpu_cycle)), dpu_cycle, "o", markersize=1, label="cycle")
    plt.yticks(fontproperties='Times New Roman', size=20)
    plt.xticks([10000,20000,30000,40000],fontproperties='Times New Roman', size=20)
    plt.xlabel("DPU hardware thread ID", fontsize=30, fontproperties='Times New Roman')
    plt.ylabel("Execution cycles", fontsize=30, fontproperties='Times New Roman')
    #plt.legend()
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontname('Times New Roman')

    plt.tight_layout()
    print("tri_tri6-predict.png")
    plt.savefig("./reproduce/fig13-3.png",format="png",bbox_inches = 'tight',dpi=1000)
