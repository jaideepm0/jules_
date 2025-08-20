import matplotlib.pyplot as plt

def analysis():
    # Quarterly retention data
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    retention_rates = [66.51, 74.55, 71.04, 78.98]

    # Calculate the average retention rate
    average_retention = sum(retention_rates) / len(retention_rates)
    print(f"Average quarterly retention rate: {average_retention:.2f}%")

    # Industry benchmark
    industry_benchmark = 85

    # --- Visualization 1: Quarterly Retention Trend ---
    plt.figure(figsize=(10, 6))
    plt.plot(quarters, retention_rates, marker='o', linestyle='-', color='b')
    plt.title('Quarterly Retention Rate Trend')
    plt.xlabel('Quarter')
    plt.ylabel('Retention Rate (%)')
    plt.grid(True)
    plt.ylim(60, 90)
    # Save the plot
    plt.savefig('retention_trend.png')
    plt.close()

    # --- Visualization 2: Benchmark Comparison ---
    plt.figure(figsize=(8, 6))
    labels = ['Our Average Retention', 'Industry Benchmark']
    values = [average_retention, industry_benchmark]
    colors = ['skyblue', 'lightgreen']

    bars = plt.bar(labels, values, color=colors)
    plt.ylabel('Retention Rate (%)')
    plt.title('Average Retention Rate vs. Industry Benchmark')
    plt.ylim(0, 100)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}%', va='bottom', ha='center')

    # Save the plot
    plt.savefig('benchmark_comparison.png')
    plt.close()

if __name__ == '__main__':
    analysis()
