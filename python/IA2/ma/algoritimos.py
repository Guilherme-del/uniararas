import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
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
  report = classification_report(y_test, y_pred, output_dict=True, zero_division=1)
  return report

# K Nearest Neighbors
print("K Nearest Neighbors:")
knn_reports = []
for n_neighbors in [1, 3, 5]:
    print(f"Number of Neighbors: {n_neighbors}")
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn_report = train_and_evaluate(knn, X_train, X_test, y_train, y_test)
    print(knn_report)  # Print the classification report
    if knn_report and knn_report != {}:  # Check if the report is non-empty
        knn_reports.append(knn_report)
    
# Decision Tree
print("\nDecision Tree:")
tree_reports = []
for max_depth in [1, 3, 5]:
    print(f"Max Depth: {max_depth}")
    tree = DecisionTreeClassifier(max_depth=max_depth, class_weight='balanced')
    tree_report = train_and_evaluate(tree, X_train, X_test, y_train, y_test)
    print(tree_report)  # Print the classification report
    if tree_report and tree_report != {}:  # Check if the report is non-empty
        tree_reports.append(tree_report)

# Random Forest
print("\nRandom Forest:")
forest_reports = []
for n_estimators in [50, 100, 150]:
    print(f"Number of Estimators: {n_estimators}")
    forest = RandomForestClassifier(n_estimators=n_estimators, class_weight='balanced')
    forest_report = train_and_evaluate(forest, X_train, X_test, y_train, y_test)
    print(forest_report)  # Print the classification report
    if forest_report and forest_report != {}:  # Check if the report is non-empty
        forest_reports.append(forest_report)

# Função para calcular métricas médias
def calculate_average_metrics(reports):
    metrics = ['precision', 'recall', 'f1-score']
    class_metrics = {metric: {} for metric in metrics}
    print("relatorios: ", reports)
    
    for report in reports:
        for class_name, values in report.items():
            if class_name not in ['accuracy', 'macro avg', 'weighted avg']:
                for metric in metrics:
                    if metric in values:
                        # Split the class name into individual labels
                        class_names = class_name.split('_')
                        for name in class_names:
                            if name not in class_metrics[metric]:
                                class_metrics[metric][name] = []
                            class_metrics[metric][name].append(values[metric])
    
    average_metrics = {}
    for metric, values in class_metrics.items():
        if any(values):  # Check if any values are present in the dictionary
            average_metrics[metric] = {class_name: sum(scores) / len(scores) for class_name, scores in values.items()}
        else:
            average_metrics[metric] = {}
    return average_metrics

# Calcular métricas médias para cada algoritmo
average_metrics_knn = calculate_average_metrics(knn_reports)
average_metrics_tree = calculate_average_metrics(tree_reports)
average_metrics_forest = calculate_average_metrics(forest_reports)

# Função para plotar os resultados
def plot_results(average_metrics, title):
    if not average_metrics:
        print("No data to plot.")
        return
    
    # Create a figure and axis object
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Define colors for different metrics
    colors = {'precision': 'blue', 'recall': 'orange', 'f1-score': 'green'}
    
    # Define the width of each bar
    bar_width = 0.2
    
    # Define the positions of bars on the x-axis
    positions = range(len(next(iter(average_metrics.values()))))
    
    # Plot bars for each metric
    for i, (metric, values) in enumerate(average_metrics.items()):
        ax.bar([p + i * bar_width for p in positions], values.values(), bar_width, label=metric, color=colors[metric])
    
    # Set x-axis labels and tick positions
    ax.set_xticks([p + 1.5 * bar_width for p in positions])
    ax.set_xticklabels(average_metrics[next(iter(average_metrics))].keys())  # Use keys of the first metric
    
    # Set labels and title
    ax.set_xlabel('Class')
    ax.set_ylabel('Value')
    ax.set_title(title)
    
    # Add legend
    ax.legend(title='Metric')
    
    # Show plot
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
