import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/V/Desktop/cleaned_covid_data.csv')

zip_data = df.groupby('ZIP Code')[['Cases - Weekly', 'Deaths - Weekly', 'Tests - Weekly']].sum().reset_index()

top_cases = zip_data.nlargest(10, 'Cases - Weekly')
plt.figure(figsize=(10, 6))
sns.barplot(x='Cases - Weekly', y='ZIP Code', hue='ZIP Code', data=top_cases, palette='viridis', legend=False)
plt.title('Top 10 ZIP Codes by Total Weekly Cases')
plt.xlabel('Total Cases (Normalized)')
plt.ylabel('ZIP Code')
plt.tight_layout()
plt.savefig('zip_cases_barplot.png')
plt.show()

top_deaths = zip_data.nlargest(10, 'Deaths - Weekly')
plt.figure(figsize=(10, 6))
sns.barplot(x='Deaths - Weekly', y='ZIP Code', hue='ZIP Code', data=top_deaths, palette='magma', legend=False)
plt.title('Top 10 ZIP Codes by Total Weekly Deaths')
plt.xlabel('Total Deaths (Normalized)')
plt.ylabel('ZIP Code')
plt.tight_layout()
plt.savefig('zip_deaths_barplot.png')
plt.show()

top_tests = zip_data.nlargest(10, 'Tests - Weekly')
plt.figure(figsize=(10, 6))
sns.barplot(x='Tests - Weekly', y='ZIP Code', hue='ZIP Code', data=top_tests, palette='plasma', legend=False)
plt.title('Top 10 ZIP Codes by Total Weekly Tests')
plt.xlabel('Total Tests (Normalized)')
plt.ylabel('ZIP Code')
plt.tight_layout()
plt.savefig('zip_tests_barplot.png')
plt.show()

pivot_data = zip_data.set_index('ZIP Code')[['Cases - Weekly', 'Deaths - Weekly', 'Tests - Weekly']]
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_data, cmap='Reds', annot=True, fmt='.2f')
plt.title('ZIP Code Severity Heatmap (Cases, Deaths, Tests)')
plt.tight_layout()
plt.savefig('zip_heatmap.png')
plt.show()
