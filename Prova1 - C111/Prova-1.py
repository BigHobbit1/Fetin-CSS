import numpy as np

arr = np.loadtxt('brands.csv',delimiter=';',dtype=str,encoding='utf-8')

# Questão 1
Empresas = arr[1:,0]
Microsoft = np.char.find(Empresas,'Microsoft')>=0
Faturamento2021 = arr[1:,10].astype(float)
Faturamento2022 = arr[1:,9].astype(float)
print('O faturamento da empresa de 2021 para 2022 foi de :',Faturamento2022[Microsoft]-Faturamento2021[Microsoft],'$')

#Questão 2
MarcasComA = np.char.find(Empresas,'A')==0
print('As Empresas que começam com a letra "a" são: ',Empresas[MarcasComA])
print('Organizando as empresas em ordem alfabetica: ',np.sort(Empresas[MarcasComA]))

#Questão 3
Pais = arr[1:,3]
Eua = np.char.find(Pais,'United States')>=0
print('A porcentagem de empresas deste dataset que são dos EUA e de: ',(np.count_nonzero(Eua)/np.count_nonzero(Pais))*100,'%')

#Questão 4
Slicing = arr[1:,0:3]
cond1 = Slicing[0:,2].astype(float)>2000
cond2 = Slicing[0:,0]
print('As empresas fundadas depois do ano 2000 são: ',cond2[cond1])

#Questão 5
Fundacoes = arr[1:,2]
Anos,NEmpresas = np.unique(Fundacoes,return_counts=True)
print('O ano que houve um maior numero de abertura de empresas foi o ano de: ',Anos[np.argmax(NEmpresas)])
