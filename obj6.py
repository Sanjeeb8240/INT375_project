import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/V/Desktop/cleaned_covid_data.csv')

print("Summary Statistics:")
print(df[['Cases - Weekly', 'Deaths - Weekly', 'Tests - Weekly', 'Case Rate - Weekly']].describe())

plt.figure(figsize=(8, 6))
sns.histplot(df['Cases - Weekly'], bins=30, kde=True, color='blue')
plt.title('Distribution of Weekly Cases')
plt.xlabel('Cases (Normalized)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('cases_histogram.png')
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Tests - Weekly', y='Cases - Weekly', data=df, hue='Deaths - Weekly', size='Deaths - Weekly', palette='coolwarm')
plt.title('Weekly Cases vs Tests (Colored by Deaths)')
plt.xlabel('Tests (Normalized)')
plt.ylabel('Cases (Normalized)')
plt.tight_layout()
plt.savefig('cases_vs_tests_scatter.png')
plt.show()

plt.figure(figsize=(8, 6))
sns.kdeplot(df['Case Rate - Weekly'], fill=True, color='green')
plt.title('Density Plot of Weekly Case Rates')
plt.xlabel('Case Rate (Normalized)')
plt.ylabel('Density')
plt.tight_layout()
plt.savefig('case_rate_density.png')
plt.show()
