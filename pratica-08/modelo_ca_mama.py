# Importação das bibliotecas do projeto
from sklearn.datasets import load_breast_cancer  # Dataset de CA de mama
from sklearn.ensemble import RandomForestClassifier  # Algoritmo do Random Forest

# Métricas do projeto
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

# Função para dividir o conjunto de dados
from sklearn.model_selection import train_test_split

# Carregar o dataset do CA de mama
data = load_breast_cancer()

# ---
# 569 amostras
# característica: 30 de imagens
# rótulos: 0 para valores de tumor maligno e 1 para valores de tumores benignos

# O dataset tem características (data.data) e rótulos (data.target).
# data.data: matriz de 30 características para cada amostra
# data.target: vetores 0 (maligno), 1 (benigno) para cada amostra

# Dividir os dados para treinamento e teste, sendo que 70% será para treinamento e 30% para teste

# X_train e X_test: características para treinar, testar
# y_train e y_test: rótulos para treinar, testar

# random_state=42: garantir a reprodutibilidade dos resultados
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

# Inicializar o modelo Random Forest
model = RandomForestClassifier(random_state=42)

# Treinar o modelo
model.fit(X_train, y_train)

# Previsão de classe (0 ou 1)
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:,1]  # Probabilidade de ser da classe positiva (1)

# Cálculo das Métricas
precision = precision_score(y_test, y_pred)      # Precisão: TP / (TP + FP)
recall = recall_score(y_test, y_pred)            # Sensibilidade: TP / (TP + FN)
f1 = f1_score(y_test, y_pred)                    # Média F1: 2 * (precisão * sensibilidade) / (precisão + sensibilidade)
auc = roc_auc_score(y_test, y_pred_proba)        # Área sob a curva ROC

# Exibição dos resultados
print(f"\nA métrica Precisão é: {precision:.2f}, significa que temos poucos falsos positivos.")
print(f"\nA métrica Sensibilidade é: {recall:.2f}, significa que temos poucos falsos negativos")
print(f"\nA métrica F1 Score é: {f1:.2f}, significa um equilíbrio entre as métricas precision (precisão) e recall (sensibilidade) ")
print(f"\nA métrica da AUC/ROC (área sob a curva ROC) é: {auc:.2f}, significa boa capacidade de distinguir as classes distintas.")
