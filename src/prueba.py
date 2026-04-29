import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix, classification_report

def main():
    df = pd.read_csv("../WineQT.csv")

    X = df.drop("quality", axis=1)
    y = df["quality"]

    modelo = joblib.load("modelo.pkl")

    pred = modelo.predict(X)

    print("Matriz de confusión:")
    print(confusion_matrix(y, pred))

    print("\nReporte:")
    print(classification_report(y, pred))

if __name__ == "__main__":
    main()