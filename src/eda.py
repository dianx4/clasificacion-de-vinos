import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def main():
    df = pd.read_csv("../WineQT.csv")

    print(df.head())
    print("\nInfo:")
    print(df.info())

    print("\nNulos:")
    print(df.isnull().sum())

    print("\nDescripción:")
    print(df.describe())

    # Histogramas
    df.hist(figsize=(12,10))
    plt.show()

    # Correlación
    plt.figure(figsize=(10,8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.show()

    # Boxplots
    for col in df.columns[:-1]:
        sns.boxplot(y=df[col])
        plt.title(col)
        plt.show()

if __name__ == "__main__":
    main()