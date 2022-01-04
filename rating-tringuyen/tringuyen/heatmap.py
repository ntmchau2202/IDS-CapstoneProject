import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raw_data = pd.read_excel("../raw_restaurant_categorized.xlsx")

df = raw_data

df['new_rate'] = (round((df['rating']) * 2) / 2)  # round rating to the NEREAST 0.5, create new column called "new_rate"

df['avg_price'] = (df['endrange'] + df['startrange']) / 2  # find the average price
df['avg_price'] = df['avg_price'] / 1000  # price 1 instead of 1000 for short

# Plot heatmap "Number of each rating(avg) vs Location" of specific dish
fig, axs = plt.subplots(2, 2, figsize=(15, 8))

pizza_tight_price = df.loc[(df['pizza'] == 'x') & (50 <= df['avg_price']) & (df['avg_price'] <= 150)]
location_vs_rate_pizza = pizza_tight_price.groupby('location').new_rate.value_counts().unstack().fillna(0)
sns.heatmap(location_vs_rate_pizza, cmap='Reds', ax=axs[0, 0])

nhahang_tight_price = df.loc[(df['nhà hàng'] == 'x') & (0 <= df['avg_price']) & (df['avg_price'] <= 500)]
location_vs_rate_nhahang = nhahang_tight_price.groupby('location').new_rate.value_counts().unstack().fillna(0)
sns.heatmap(location_vs_rate_nhahang, cmap='Purples', ax=axs[0, 1])

trasua_tight_price = df.loc[(df['trà sữa'] == 'x') & (0 <= df['avg_price']) & (df['avg_price'] <= 75)]
location_vs_rate_trasua = trasua_tight_price.groupby('location').new_rate.value_counts().unstack().fillna(0)
sns.heatmap(location_vs_rate_trasua, cmap='Blues', ax=axs[1, 0])

vanphong_tight_price = df.loc[(df['quán cơm văn phòng'] == 'x') & (0 <= df['avg_price']) & (df['avg_price'] <= 100)]
location_vs_rate_vanphong = vanphong_tight_price.groupby('location').new_rate.value_counts().unstack().fillna(0)
sns.heatmap(location_vs_rate_vanphong, cmap='Oranges', ax=axs[1, 1])

axs[0, 0].set_ylabel('')
axs[0, 0].set_xlabel('')
axs[0, 0].tick_params('x', labelrotation=45)
axs[0, 0].set_title('Pizza (50k-150k)', weight='bold')
axs[0, 1].set_ylabel('')
axs[0, 1].set_xlabel('')
axs[0, 1].tick_params('x', labelrotation=45)
axs[0, 1].set_title('Nhà hàng (max 500k)', weight='bold')
axs[1, 0].set_ylabel('')
axs[1, 0].set_xlabel('')
axs[1, 0].tick_params('x', labelrotation=45)
axs[1, 0].set_title('Trà sữa (max 75k)', weight='bold')
axs[1, 1].set_ylabel('')
axs[1, 1].set_xlabel('')
axs[1, 1].tick_params('x', labelrotation=45)
axs[1, 1].set_title('Cơm văn phòng (max 100k)', weight='bold')
fig.tight_layout(pad=1)
plt.show()
