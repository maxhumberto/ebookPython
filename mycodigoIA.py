import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carregar o conjunto de dados Iris
iris_data = pd.read_csv('iris.csv')

# Separar os recursos (features) e os rótulos (labels)
X = iris_data.drop('species', axis=1)
y = iris_data['species']

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo de classificação SVM (Máquina de Vetores de Suporte)
model = SVC(kernel='linear')

# Treinar o modelo com os dados de treino
model.fit(X_train, y_train)

# Realizar previsões com o conjunto de teste
predictions = model.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print("Precisão do modelo:", accuracy)
