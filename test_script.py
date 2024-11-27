import pytest
import pandas as pd
import numpy as np

# Carregando o arquivo CSV para realizar testes
df = pd.read_csv('data.csv')

# Teste 1: Verificar se o DataFrame foi carregado corretamente
def test_dataframe_load():
    assert df.shape[0] > 0  # Verifica se o DataFrame não está vazio

# Teste 2: Verificar se a coluna 'idade' existe
def test_column_exists():
    assert 'idade' in df.columns

# Teste 3: Verificar se a soma da coluna 'idade' está correta

# Teste 4: Verificar a média da coluna 'salario'

# Teste 5: Verificar se existe algum valor NaN na coluna 'salario'
def test_column_nan():
    assert df['salario'].isnull().sum() == 0  # Verifica se não há valores faltantes

# Teste 6: Verificar se a coluna 'idade' é do tipo inteiro
def test_column_type():
    assert pd.api.types.is_integer_dtype(df['idade'])

# Teste 7: Verificar a mediana da coluna 'salario'  # Exemplo de valor esperado

# Teste 8: Verificar se há valores negativos na coluna 'salario'
def test_column_negative_values():
    assert (df['salario'] < 0).sum() == 0  # Verifica se não há salários negativos

# Teste 9: Verificar a quantidade de linhas únicas em uma coluna # Verifica se há mais de 3 departamentos únicos

# Teste 10: Verificar se a soma total de um cálculo feito com numpy está correta
