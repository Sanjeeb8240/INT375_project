import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/V/Desktop/cleaned_covid_data.csv")
df['Week Start'] = pd.to_datetime(df['Week Start'])

weekly_data = df.groupby('Week Start')[['Cases - Weekly', 'Deaths - Weekly', 'Tests - Weekly']].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Week Start', y='Cases - Weekly', data=weekly_data, label='Cases', marker='o')
sns.lineplot(x='Week Start', y='Deaths - Weekly', data=weekly_data, label='Deaths', marker='s')
sns.lineplot(x='Week Start', y='Tests - Weekly', data=weekly_data, label='Tests', marker='^')
plt.title('Weekly COVID-19 Trends Across All ZIP Codes')
plt.xlabel('Week Start Date')
plt.ylabel('Count (Normalized)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('weekly_trends_line.png')
plt.show()

plt.figure(figsize=(12, 6))
plt.stackplot(weekly_data['Week Start'], weekly_data['Cases - Weekly'], weekly_data['Deaths - Weekly'], weekly_data['Tests - Weekly'],
              labels=['Cases', 'Deaths', 'Tests'], alpha=0.5)
plt.title('Weekly COVID-19 Trends (Stacked Area)')
plt.xlabel('Week Start Date')
plt.ylabel('Count (Normalized)')
plt.legend(loc='upper left')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('weekly_trends_area.png')
plt.show()
