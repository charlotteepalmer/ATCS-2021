# Charlotte Palmer
# AT CS Block B
# 12/2/21

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# cleaning data - combining the two csv files
pd.set_option("display.max_columns", None)
df1 = pd.read_csv("olympicData1.csv")
df2 = pd.read_csv("olympicData2.csv")
print(df1.info())
print(df2.info())

df3 = pd.merge(df1, df2, how="inner", left_on="Country", right_on="Country")
print(df3)

# bar chart for total medals per country in 2020
# x = countries, y = total medals
# color coded by GDP
ax = sns.barplot(x="Country", y="Total 2020", hue="GDP", data=df3, dodge=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()

# bar chart for total medals per country in 2020
# x = countries, y = total medals
# color coded by type of government
ax = sns.barplot(x="Country", y="Total 2020", hue="Type of government", data=df3, dodge=False)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()

# bar chart for gold medals per country in 2020
# x = countries, y = gold medals
# color coded by GDP
ax = sns.barplot(x="Country", y="Gold 2020", hue="GDP", data=df3, dodge=False, order=df3.sort_values('Gold 2020',ascending = False).Country)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()

# bar chart for gold medals per country in 2020
# x = countries, y = gold medals
# color coded by type of government
ax = sns.barplot(x="Country", y="Gold 2020", hue="Type of government", data=df3, dodge=False, order=df3.sort_values('Gold 2020',ascending = False).Country)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()

# bar chart for total medals per country in 2016
# x = countries, y = total medals
# color coded by GDP
ax = sns.barplot(x="Country", y="Total 2016", hue="GDP", data=df3, dodge=False, order=df3.sort_values('Total 2016',ascending = False).Country)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()

# bar chart for total medals per country in 2016
# x = countries, y = total medals
# color coded by type of government
ax = sns.barplot(x="Country", y="Total 2016", hue="Type of government", data=df3, dodge=False, order=df3.sort_values('Total 2016',ascending = False).Country)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()

# bar chart for gold medals per country in 2016
# x = countries, y = gold medals
# color coded by GDP
ax = sns.barplot(x="Country", y="Gold 2016", hue="GDP", data=df3, dodge=False, order=df3.sort_values('Gold 2016',ascending = False).Country)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()

# bar chart for gold medals per country in 2016
# x = countries, y = gold medals
# color coded by type of government
ax = sns.barplot(x="Country", y="Gold 2016", hue="Type of government", data=df3, dodge=False, order=df3.sort_values('Gold 2016',ascending = False).Country)
ax.set_xticklabels(ax.get_xticklabels(),rotation = 90)
plt.gcf().subplots_adjust(bottom=0.25)
plt.show()