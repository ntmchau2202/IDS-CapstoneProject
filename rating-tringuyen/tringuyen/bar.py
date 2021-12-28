import pandas as pd
import matplotlib.pyplot as plt

raw_data = pd.read_excel("../raw_restaurant_categorized.xlsx")

df = raw_data


df['new_rate'] = (round((df['rating']) * 2) / 2)  # round rating to the NEREAST 0.5, create new column called "new_rate"
# 0.7 round down to 0.5,
# 0,8 round up to next number
# new_rate = df['new_rate']
# new_rate_count = df['new_rate'].nunique()  # show number of unique value in column "new_rate"
# new_rate_uni = df['new_rate'].unique()  # show those unique values in column "new_rate"
# new_rate_uni = np.sort(new_rate_uni)  # SORT with NUMPY
# print(new_rate_count)
# print(new_rate_uni)

f, ax = plt.subplots(figsize=(10, 8))  # set the size that you'd like (width, height)
df['new_rate'].groupby(df['new_rate']).count().plot(kind='bar', color='pink', align="center", width=0.9)  # plot bar chart
#  width=0.9 to increase bar size

plt.xticks(rotation=0)  # dont want to rotate x ticks because it's stupid
plt.xlabel("RATING")
plt.ylabel("COUNT", rotation=0)  # dont want to rotate y lable because it's stupid
plt.show()