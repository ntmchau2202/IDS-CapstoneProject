import pandas as pd
import matplotlib.pyplot as plt

raw_data = pd.read_excel("../raw_restaurant_categorized.xlsx")

df = raw_data


df['new_rate'] = (round((df['rating']) * 2) / 2)  # round rating to the NEREAST 0.5, create new column called "new_rate"


df['avg_price'] = (df['endrange'] + df['startrange']) / 2  # find the average price
df['avg_price'] = df['avg_price'] / 1000  # price 1 instead of 1000 for short


# # GET only data of each dish
# df1 = df.loc[df['cơm, phở'] == 'x']
# df2 = df.loc[df['pizza'] == 'x']
# df3 = df.loc[df['ăn vặt, ăn vặt vỉa hè'] == 'x']
# df4 = df.loc[df['đồ ăn sáng, đồ ăn sáng vỉa hè'] == 'x']
# df5 = df.loc[df['quán cơm văn phòng'] == 'x']
# df6 = df.loc[df['quán cơm bình dân, cơm mang đi'] == 'x']
# df7 = df.loc[df['đồ ăn nhanh'] == 'x']
# df8 = df.loc[df['đồ ăn hàn quốc, nhà hàng hàn quốc'] == 'x']
# df9 = df.loc[df['đồ ăn nhật bản, nhà hàng nhật bản'] == 'x']
# df10 = df.loc[df['nhà hàng'] == 'x']
# df11 = df.loc[df['nhà hàng chay'] == 'x']
# df12 = df.loc[df['trà sữa'] == 'x']
# df13 = df.loc[df['bánh ngọt, bánh sinh nhật'] == 'x']
# df14 = df.loc[df['cafe'] == 'x']

# Remove outliers of each dish
df1 = df.loc[(df['cơm, phở'] == 'x') & (df['avg_price'] <= 200)]
df2 = df.loc[(df['pizza'] == 'x') & (df['avg_price'] <= 350)]
df3 = df.loc[(df['ăn vặt, ăn vặt vỉa hè'] == 'x') & (df['avg_price'] <= 400)]
df4 = df.loc[(df['đồ ăn sáng, đồ ăn sáng vỉa hè'] == 'x') & (df['avg_price'] <= 300)]
df5 = df.loc[(df['quán cơm văn phòng'] == 'x') & (df['avg_price'] <= 400)]
df6 = df.loc[(df['quán cơm bình dân, cơm mang đi'] == 'x') & (df['avg_price'] <= 300)]
df7 = df.loc[(df['đồ ăn nhanh'] == 'x') & (df['avg_price'] <= 150)]
df8 = df.loc[df['đồ ăn hàn quốc, nhà hàng hàn quốc'] == 'x']
df9 = df.loc[(df['đồ ăn nhật bản, nhà hàng nhật bản'] == 'x') & (df['avg_price'] <= 400)]
df10 = df.loc[(df['nhà hàng'] == 'x') & (df['avg_price'] <= 800)]
df11 = df.loc[(df['nhà hàng chay'] == 'x') & (df['avg_price'] <= 300)]
df12 = df.loc[df['trà sữa'] == 'x']
df13 = df.loc[(df['bánh ngọt, bánh sinh nhật'] == 'x') & (df['avg_price'] <= 300)]
df14 = df.loc[(df['cafe'] == 'x') & (df['avg_price'] <= 600)]

# OVERALL Rating vs Price
# fig, ax = plt.subplots()
# ax.ticklabel_format(useOffset=False, style='plain')
# plt.scatter(df['avg_price'], df['rating'])
# plt.show()
# exit(0)

# Plot all 14 dishes - "Rating vs price"
fig, axs = plt.subplots(4, 4, figsize=(15, 9))
axs[0, 0].scatter(df1['avg_price'], df1['rating'], c='#454d66')
axs[0, 0].set_title('Cơm phở', weight='bold')
axs[0, 1].scatter(df2['avg_price'], df2['rating'], c='#309975')
axs[0, 1].set_title('Pizza', weight='bold')
axs[0, 2].scatter(df3['avg_price'], df3['rating'], c='#58b368')
axs[0, 2].set_title('Ăn vặt', weight='bold')
axs[0, 3].scatter(df4['avg_price'], df4['rating'], c='#dad873')
axs[0, 3].set_title('Ăn sáng', weight='bold')
axs[1, 0].scatter(df5['avg_price'], df5['rating'], c='#e0f0ea')
axs[1, 0].set_title('Cơm văn phòng', weight='bold')
axs[1, 1].scatter(df6['avg_price'], df6['rating'], c='#95adbe')
axs[1, 1].set_title('Cơm bình dân', weight='bold')
axs[1, 2].scatter(df7['avg_price'], df7['rating'], c='#574f7d')
axs[1, 2].set_title('Ăn nhanh', weight='bold')
axs[1, 3].scatter(df8['avg_price'], df8['rating'], c='#503a65')
axs[1, 3].set_title('Hàn Quốc', weight='bold')
axs[2, 0].scatter(df9['avg_price'], df9['rating'], c='#e74645')
axs[2, 0].set_title('Nhật Bản', weight='bold')
axs[2, 1].scatter(df10['avg_price'], df10['rating'], c='#fb7756')
axs[2, 1].set_title('Nhà hàng', weight='bold')
axs[2, 2].scatter(df11['avg_price'], df11['rating'], c='#facd60')
axs[2, 2].set_title('Chay', weight='bold')
axs[2, 3].scatter(df12['avg_price'], df12['rating'], c='#fdfa66')
axs[2, 3].set_title('Trà sữa', weight='bold')
axs[3, 0].scatter(df13['avg_price'], df13['rating'], c='#8f3b76')
axs[3, 0].set_title('Bánh ngọt', weight='bold')
axs[3, 1].scatter(df14['avg_price'], df14['rating'], c='#c7417b')
axs[3, 1].set_title('Cafe', weight='bold')
fig.delaxes(axs[3][2])
fig.delaxes(axs[3][3])
fig.tight_layout(pad=1)

plt.show()
