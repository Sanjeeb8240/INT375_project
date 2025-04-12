import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/V/Desktop/cleaned_covid_data.csv')

plt.figure(figsize=(8, 6))
sns.boxplot(y='Case Rate - Weekly', data=df, color='lightblue')
plt.title('Boxplot of Weekly Case Rates Across ZIP Codes')
plt.ylabel('Case Rate (Normalized)')
plt.tight_layout()
plt.savefig('case_rate_boxplot.png')
plt.show()

Q1 = df['Case Rate - Weekly'].quantile(0.25)
Q3 = df['Case Rate - Weekly'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Case Rate - Weekly'] < Q1 - 1.5 * IQR) | (df['Case Rate - Weekly'] > Q3 + 1.5 * IQR)]
print("Outliers in Case Rates:")
print(outliers[['ZIP Code', 'Week Start', 'Case Rate - Weekly']])
