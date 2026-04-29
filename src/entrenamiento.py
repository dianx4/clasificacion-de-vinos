import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import joblib

def main():
    df = pd.read_csv("../WineQT.csv")

    X = df.drop("quality", axis=1)
    y = df["quality"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    modelos = {
        "RandomForest": RandomForestClassifier(),
        "LogisticRegression": LogisticRegression(max_iter=1000)
    }

    mejor_modelo = None
    mejor_score = 0

    for nombre, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        pred = modelo.predict(X_test)

        acc = accuracy_score(y_test, pred)
        print(f"{nombre} Accuracy:", acc)

        if acc > mejor_score:
            mejor_score = acc
            mejor_modelo = modelo

    joblib.dump(mejor_modelo, "modelo.pkl")
    print("Modelo guardado")

if __name__ == "__main__":
    main()