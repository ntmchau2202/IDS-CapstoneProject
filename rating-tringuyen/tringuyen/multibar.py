import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

raw_data = pd.read_excel("../raw_restaurant_categorized.xlsx")

df = raw_data

df['new_rate'] = (round((df['rating']) * 2) / 2)  # round rating to the NEREAST 0.5, create new column called "new_rate"

df['avg_price'] = (df['endrange'] + df['startrange']) / 2  # find the average price
df['avg_price'] = df['avg_price'] / 1000  # price 1 instead of 1000 for short

mon_phu = ['trà sữa', 'cafe', 'bánh ngọt, bánh sinh nhật', 'pizza']
nha_hang = ['nhà hàng', 'đồ ăn nhật bản, nhà hàng nhật bản', 'đồ ăn hàn quốc, nhà hàng hàn quốc', 'nhà hàng chay']
com = ['quán cơm văn phòng', 'quán cơm bình dân, cơm mang đi', 'cơm, phở']
fast = ['ăn vặt, ăn vặt vỉa hè', 'đồ ăn nhanh', 'đồ ăn sáng, đồ ăn sáng vỉa hè']

mon_phu_lable = ['Trà sữa', 'Cafe', 'Bánh', 'Pizza']
nha_hang_lable = ['Nhà hàng', 'Nhật Bản', 'Hàn Quốc', 'Chay']
com_lable = ['Cơm văn phòng', 'Cơm bình dân', 'Cơm phở']
fast_lable = ['Ăn vặt', 'Ăn nhanh', 'Ăn sáng, vỉa hè']

mon_phu_axis = np.arange(len(mon_phu_lable))
nha_hang_axis = np.arange(len(nha_hang_lable))
com_axis = np.arange(len(com_lable))
fast_axis = np.arange(len(fast_lable))

avg_rate_mon_phu = list(map(lambda x: df.loc[(df[x] == 'x')]['rating'].mean(), mon_phu))
# above equals to : avg_rate_1 = [df.loc[(df['trà sữa'] == 'x')]['rating'].mean(), df.loc[(df['cafe'] == 'x')][
# 'rating'].mean(), df.loc[(df['pizza'] == 'x')]['rating'].mean(), df.loc[(df['bánh ngọt, bánh sinh nhật'] == 'x')][
# 'rating'].mean()]
min_mon_phu = list(map(lambda x: df.loc[(df[x] == 'x')]['startrange'].mean() / 1000, mon_phu))
max_mon_phu = list(map(lambda x: df.loc[(df[x] == 'x')]['endrange'].mean() / 1000, mon_phu))

avg_rate_nha_hang = list(map(lambda x: df.loc[(df[x] == 'x')]['rating'].mean(), nha_hang))
min_nha_hang = list(map(lambda x: df.loc[(df[x] == 'x')]['startrange'].mean() / 1000, nha_hang))
max_nha_hang = list(map(lambda x: df.loc[(df[x] == 'x')]['endrange'].mean() / 1000, nha_hang))

avg_rate_com = list(map(lambda x: df.loc[(df[x] == 'x')]['rating'].mean(), com))
min_com = list(map(lambda x: df.loc[(df[x] == 'x')]['startrange'].mean() / 1000, com))
max_com = list(map(lambda x: df.loc[(df[x] == 'x')]['endrange'].mean() / 1000, com))

avg_fast = list(map(lambda x: df.loc[(df[x] == 'x')]['rating'].mean(), fast))
min_fast = list(map(lambda x: df.loc[(df[x] == 'x')]['startrange'].mean() / 1000, fast))
max_fast = list(map(lambda x: df.loc[(df[x] == 'x')]['endrange'].mean() / 1000, fast))

fig, ax = plt.subplots(2, 2, figsize=(15, 8))

ax[0, 0].set_xticks(mon_phu_axis, mon_phu_lable, fontsize=18)
ax[0, 0].set_ylabel('Avg rating', fontsize=18, color='#543c52', weight='bold')
ax[0, 0].yaxis.set_tick_params(labelsize=15, labelcolor='#543c52')

ax00b = ax[0, 0].twinx()  # instantiate a second axes that shares the same x-axis
ax00b.set_ylabel('Start/End range', color='#f19088', fontsize=18, weight='bold')
ax00b.yaxis.set_tick_params(labelsize=15, labelcolor='#f19088')

ax[0, 0].bar(mon_phu_axis - 0.2, avg_rate_mon_phu, 0.2, label='Avg rating', color='#543c52')
ax00b.bar(mon_phu_axis, min_mon_phu, 0.2, label='Stare range', color='#f55951')
ax00b.bar(mon_phu_axis + 0.2, max_mon_phu, 0.2, label='End range', color='#edd2cb')

ax[0, 1].set_xticks(nha_hang_axis, nha_hang_lable, fontsize=18)
ax[0, 1].set_ylabel('Avg rating', fontsize=18, color='#543c52', weight='bold')
ax[0, 1].yaxis.set_tick_params(labelsize=15, labelcolor='#543c52')

ax01b = ax[0, 1].twinx()  # instantiate a second axes that shares the same x-axis
ax01b.set_ylabel('Start/End range', color='#f19088', fontsize=18, weight='bold')
ax01b.yaxis.set_tick_params(labelsize=15, labelcolor='#f19088')

ax[0, 1].bar(nha_hang_axis - 0.2, avg_rate_nha_hang, 0.2, label='Avg rating', color='#543c52')
ax01b.bar(nha_hang_axis, min_nha_hang, 0.2, label='Stare range', color='#f55951')
ax01b.bar(nha_hang_axis + 0.2, max_nha_hang, 0.2, label='End range', color='#edd2cb')

ax[1, 0].set_xticks(fast_axis, fast_lable, fontsize=18)
ax[1, 0].set_ylabel('Avg rating', fontsize=18, color='#543c52', weight='bold')
ax[1, 0].yaxis.set_tick_params(labelsize=15, labelcolor='#543c52')

ax10b = ax[1, 0].twinx()  # instantiate a second axes that shares the same x-axis
ax10b.set_ylabel('Start/End range', color='#f19088', fontsize=18, weight='bold')
ax10b.yaxis.set_tick_params(labelsize=15, labelcolor='#f19088')

ax[1, 0].bar(fast_axis - 0.2, avg_fast, 0.2, label='Avg rating', color='#543c52')
ax10b.bar(fast_axis, min_fast, 0.2, label='Stare range', color='#f55951')
ax10b.bar(fast_axis + 0.2, max_fast, 0.2, label='End range', color='#edd2cb')

ax[1, 1].set_xticks(com_axis, com_lable, fontsize=16)
ax[1, 1].set_ylabel('Avg rating', fontsize=18, color='#543c52', weight='bold')
ax[1, 1].yaxis.set_tick_params(labelsize=15, labelcolor='#543c52')

ax11b = ax[1, 1].twinx()  # instantiate a second axes that shares the same x-axis
ax11b.set_ylabel('Start/End range', color='#f19088', fontsize=18, weight='bold')
ax11b.yaxis.set_tick_params(labelsize=15, labelcolor='#f19088')

ax[1, 1].bar(com_axis - 0.2, avg_rate_com, 0.2, label='Avg rating', color='#543c52')
ax11b.bar(com_axis, min_com, 0.2, label='Stare range', color='#f55951')
ax11b.bar(com_axis + 0.2, max_com, 0.2, label='End range', color='#edd2cb')

avg_patch = mpatches.Patch(color='#543c52', label='Avg rating')
start_patch = mpatches.Patch(color='#f55951', label='Start range')
end_patch = mpatches.Patch(color='#edd2cb', label='End range')

plt.legend(handles=[avg_patch, start_patch, end_patch], bbox_to_anchor=(1.5, 1.2))
fig.tight_layout(pad=1)  # otherwise the right y-label is slightly clipped

plt.show()
