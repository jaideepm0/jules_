import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
retention_rates = [66.51, 74.55, 71.04, 78.98]
average_retention = np.mean(retention_rates)
industry_target = 85

# --- Trend Visualization ---
plt.figure(figsize=(10, 5))
plt.plot(quarters, retention_rates, marker='o', linestyle='-', color='b')
plt.title('Quarterly Customer Retention Rate (2024)')
plt.xlabel('Quarter')
plt.ylabel('Retention Rate (%)')
plt.ylim(60, 90)
plt.grid(True)
for i, rate in enumerate(retention_rates):
    plt.text(i, rate + 1, f'{rate:.2f}', ha='center')
plt.savefig('trend.png')
plt.close()

# --- Benchmark Comparison Visualization ---
plt.figure(figsize=(8, 6))
labels = ['Average Retention', 'Industry Target']
values = [average_retention, industry_target]
colors = ['skyblue', 'lightgreen']
bars = plt.bar(labels, values, color=colors)
plt.ylabel('Retention Rate (%)')
plt.title('Average Retention Rate vs. Industry Target')
plt.ylim(0, 100)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval:.2f}', ha='center')
plt.savefig('benchmark.png')
plt.close()

print("Data analysis and visualization complete.")
print(f"Average Retention Rate: {average_retention:.2f}")
