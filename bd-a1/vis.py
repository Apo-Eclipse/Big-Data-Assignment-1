import matplotlib.pyplot as plt
import seaborn as sns

def visualize(df):
    sns.histplot(df['price'], bins=7, kde=False)
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title('Histogram of Prices')
    plt.savefig('vis.png')