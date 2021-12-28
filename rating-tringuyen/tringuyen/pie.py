import pandas as pd
import matplotlib.pyplot as plt

raw_data = pd.read_excel("../raw_restaurant_categorized.xlsx")

df = raw_data
df['new_rate'] = (round((df['rating']) * 2) / 2)  # round rating to the NEREAST 0.5, create new column called "new_rate"
df['avg_price'] = (df['endrange'] + df['startrange']) / 2  # find the average price
df['avg_price'] = df['avg_price'] / 1000  # price 1 instead of 1000 for short

lables = {'nhà hàng': 'Nhà hàng', 'cafe': 'Cafe', 'quán cơm văn phòng': 'Văn phòng', 'trà sữa': 'Trà sữa',
          'ăn vặt, ăn vặt vỉa hè': 'Ăn vặt', 'quán cơm bình dân, cơm mang đi': 'Bình dân', 'đồ ăn nhanh': 'Ăn nhanh',
          'đồ ăn nhật bản, nhà hàng nhật bản': 'Nhật Bản', 'đồ ăn hàn quốc, nhà hàng hàn quốc': 'Hàn Quốc',
          'bánh ngọt, bánh sinh nhật': 'Bánh', 'cơm, phở': 'Cơm phở', 'pizza': 'Pizza', 'nhà hàng chay': 'Chay',
          'đồ ăn sáng, đồ ăn sáng vỉa hè': 'Vỉa hè'}
df = df.rename(columns=lables)
districts = ['quận long biên', 'quận hoàn kiếm', 'quận đống đa', 'quận cầu giấy',
             'quận ba đình', 'quận bắc từ liêm', 'quận nam từ liêm', 'quận tây hồ',
             'quận hoàng mai', 'quận thanh xuân', 'quận hai bà trưng', 'quận hà đông']
colors = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
          'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
          'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
i = 0
fig, ax = plt.subplots(3, 4, figsize=(15, 8))

for x in range(0, 3):
    for y in range(0, 4):
        df_tmp = df.loc[(df['new_rate'] >= 7.5) & (df['location'] == districts[i])]
        df_tmp = df_tmp.iloc[:, 10:24]
        df_tmp = df_tmp.count().reset_index(name='count').sort_values(['count'], ascending=False)
        df_tmp = df_tmp.iloc[:8, :]

        theme = plt.get_cmap(colors[i])
        theme_sets = [theme(1. * i / len(df_tmp["count"]))
                      for i in range(len(df_tmp["count"]))]
        theme_sets = theme_sets[::-1]
        ax[x, y].set_prop_cycle("color", theme_sets)
        ax[x, y].pie(df_tmp["count"], labels=df_tmp["index"], autopct='%1.1f', shadow=True,
                     explode=[0.1, 0, 0, 0, 0, 0, 0, 0])

        ax[x, y].set_title(districts[i], size=15, style='italic', weight='bold')
        i += 1

fig.tight_layout(pad=1)
plt.show()
