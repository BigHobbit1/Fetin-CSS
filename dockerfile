# Use a imagem oficial do Jenkins LTS
FROM jenkins/jenkins:lts

# Instala dependências necessárias, incluindo Python, pip, e bibliotecas para análise de dados
USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev libpq-dev && \
    pip3 install --upgrade pip

# Instala as bibliotecas necessárias para o projeto: pandas, numpy, pytest
RUN pip3 install pandas numpy pytest

# Cria um diretório para o projeto dentro do container
WORKDIR /home/jenkins/workspace

# Copia o código-fonte do projeto e o arquivo CSV para dentro do container
COPY . .

# Expondo a porta do Jenkins para acesso externo
EXPOSE 8080

# Configura o comando de inicialização do Jenkins
ENTRYPOINT ["jenkins-slave"]

RUN apt-get clean

User jenkins