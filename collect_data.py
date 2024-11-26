import pandas as pd
import numpy as np

# Exemplo de criação de um DataFrame com pandas
data = {
    'coluna_1': np.random.randint(0, 100, 10),
    'coluna_2': np.random.random(10),
}

df = pd.DataFrame(data)

# Salvar os dados processados em um arquivo CSV
df.to_csv('dados_coletados.csv', index=False)

print("Dados coletados e salvos com sucesso!")
