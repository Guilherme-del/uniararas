import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

class ModelTrainer:
    def __init__(self, train_path, test_path):
        # Caminho dos arquivos
        self.train_path = train_path
        self.test_path = test_path

        # Carregar dados de treino e teste
        self.train_data = pd.read_csv(train_path)
        self.test_data = pd.read_csv(test_path)
        self.X_train = self.train_data.drop(columns=['game_state', 'game_state_encoded', 'id'])
        self.y_train = self.train_data['game_state_encoded']
        
        # Normalizar os dados
        self.scaler = StandardScaler()
        self.X_train = self.scaler.fit_transform(self.X_train)
        
        # Separar dados de treino e validação
        self.X_train_split, self.X_val_split, self.y_train_split, self.y_val_split = train_test_split(
            self.X_train, self.y_train, test_size=0.1, random_state=33, stratify=self.y_train)
        
        # Aplicar SMOTE para balancear as classes
        self.smote = SMOTE(random_state=33, k_neighbors=1)
        self.X_train_split, self.y_train_split = self.smote.fit_resample(self.X_train_split, self.y_train_split)
        
        # Definir os modelos e os grids de parâmetros
        self.param_grid_gb = {
            'n_estimators': [50,100],
            'learning_rate': [0.001,0.01,0.1],
            'max_depth': [1,3,5,7]
        }
        self.param_grid_rf = {
            'n_estimators': [50,100],
            'max_depth': [1,3,5,7],
            'criterion': ['entropy', 'log_loss','gini']
        }
        self.models = {
            'GradientBoosting': (GradientBoostingClassifier(random_state=42), self.param_grid_gb),
            'RandomForest': (RandomForestClassifier(random_state=42), self.param_grid_rf)
        }
        self.best_score = 0
        self.best_model = None
        self.best_params = None

    def train_and_evaluate(self):
        # Realizar cross-validation e grid search
        cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
        for model_name, (model, param_grid) in self.models.items():
            grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=cv, scoring='f1_weighted', n_jobs=-1, verbose=2)
            grid_search.fit(self.X_train_split, self.y_train_split)
            if grid_search.best_score_ > self.best_score:
                self.best_score = grid_search.best_score_
                self.best_model = grid_search.best_estimator_
                self.best_params = grid_search.best_params_

        # Avaliar o melhor modelo nos dados de validação
        y_val_pred_best = self.best_model.predict(self.X_val_split)
        f1_best = f1_score(self.y_val_split, y_val_pred_best, average='weighted')
        precision_best = precision_score(self.y_val_split, y_val_pred_best, average='weighted')
        recall_best = recall_score(self.y_val_split, y_val_pred_best, average='weighted')
        confusion_best = confusion_matrix(self.y_val_split, y_val_pred_best)
        class_report = classification_report(self.y_val_split, y_val_pred_best)

        print(f'Melhores hiperparâmetros: {self.best_params}')
        print(f'Melhor F1 Score: {f1_best}')
        print(f'Melhor Precisão: {precision_best}')
        print(f'Melhor Recall: {recall_best}')
        print(f'Confusion Matrix:\n {confusion_best}')
        print(f'Classification Report:\n {class_report}')

    def make_predictions(self):
        # Fazer predições no conjunto de teste
        X_test = self.test_data.drop(columns=['id'])
        X_test = self.scaler.transform(X_test)
        self.test_data['target'] = self.best_model.predict(X_test)
        
        # Salvar submissão
        submission = self.test_data[['id', 'target']]
        submission.columns = ['id', 'target']
        submission.to_csv('submissao.csv', index=False)

if __name__ == "__main__":
    trainer = ModelTrainer(train_path='./treino.csv', test_path='./teste.csv')
    trainer.train_and_evaluate()
    trainer.make_predictions()
