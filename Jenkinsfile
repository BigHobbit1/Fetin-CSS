pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    // Instala as dependências do Python
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Executa os testes com pytest
                    sh 'pytest test_script.py'
                }
            }
        }
    }

    post {
        always {
            // Sempre gera o relatório de testes
            junit '**/test-*.xml'
        }
    }
}
