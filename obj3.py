import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/V/Desktop/cleaned_covid_data.csv')

corr_matrix = df[['Cases - Weekly', 'Deaths - Weekly', 'Tests - Weekly']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Correlation Matrix: Weekly Cases, Deaths, Tests')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.show()

print("Correlation Matrix:")
print(corr_matrix)
