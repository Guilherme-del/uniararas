import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
data = pd.read_csv('dataset.csv')

# Tratar valores ausentes
imputer = SimpleImputer(strategy='most_frequent')
data_imputed = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

# Converter atributos categóricos em numéricos
data_encoded = pd.get_dummies(data_imputed)

# Separar features e target
X = data_encoded.drop(['ADM-DECS_A', 'ADM-DECS_I', 'ADM-DECS_S'], axis=1)
y = data_encoded[['ADM-DECS_A', 'ADM-DECS_I', 'ADM-DECS_S']].apply(lambda row: ''.join(row.astype(str)), axis=1)

# Dividir dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Função para treinar e avaliar modelo
def train_and_evaluate(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return classification_report(y_test, y_pred, output_dict=True, zero_division=1)

# KNeighbors
print("KNeighbors:")
knn_reports = []
for n_neighbors in [3, 5, 7]:
    print(f"Number of Neighbors: {n_neighbors}")
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn_report = train_and_evaluate(knn, X_train, X_test, y_train, y_test)
    knn_reports.append(knn_report)
    
# Decision Tree
print("\nDecision Tree:")
tree_reports = []
for max_depth in [None, 3, 5]:
    print(f"Max Depth: {max_depth}")
    tree = DecisionTreeClassifier(max_depth=max_depth, class_weight='balanced')
    tree_report = train_and_evaluate(tree, X_train, X_test, y_train, y_test)
    tree_reports.append(tree_report)

# Random Forest
print("\nRandom Forest:")
forest_reports = []
for n_estimators in [50, 100, 150]:
    print(f"Number of Estimators: {n_estimators}")
    forest = RandomForestClassifier(n_estimators=n_estimators, class_weight='balanced')
    forest_report = train_and_evaluate(forest, X_train, X_test, y_train, y_test)
    forest_reports.append(forest_report)

# Função para calcular métricas médias
def calculate_average_metrics(reports):
    metrics = ['precision', 'recall', 'f1-score']
    class_metrics = {}
    
    for metric in metrics:
        class_metrics[metric] = {}
    
    for report in reports:
        for class_name, values in report.items():
            if class_name.isdigit():  # Ignorar classes não numéricas, como 'accuracy' e 'macro avg'
                for metric in metrics:
                    if metric != 'support':  # Ignorar a métrica 'support'
                        if class_name not in class_metrics[metric]:
                            class_metrics[metric][class_name] = []
                        class_metrics[metric][class_name].append(values[metric])
    
    # Calcular métricas médias para cada classe
    average_metrics = {}
    for metric, values in class_metrics.items():
        average_metrics[metric] = {class_name: sum(scores) / len(scores) for class_name, scores in values.items()}
    
    return average_metrics

# Calcular métricas médias para cada algoritmo
average_metrics_knn = calculate_average_metrics(knn_reports)
average_metrics_tree = calculate_average_metrics(tree_reports)
average_metrics_forest = calculate_average_metrics(forest_reports)

# Função para plotar os resultados
def plot_results(average_metrics, title):
    df = pd.DataFrame(average_metrics)
    df = df.T.reset_index().rename(columns={'index': 'Class'})
    df = pd.melt(df, id_vars='Class', var_name='Metric', value_name='Value')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Class', y='Value', hue='Metric', data=df)
    plt.title(title)
    plt.xlabel('Class')
    plt.ylabel('Value')
    plt.legend(title='Metric')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plotar os resultados para K Neighbors
print("K Nearest Neighbors:")
plot_results(average_metrics_knn, 'K Nearest Neighbors')

# Plotar os resultados para Decision Tree
print("\nDecision Tree:")
plot_results(average_metrics_tree, 'Decision Tree')

# Plotar os resultados para Random Forest
print("\nRandom Forest:")
plot_results(average_metrics_forest, 'Random Forest')
