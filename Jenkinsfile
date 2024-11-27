pipeline {
    agent any

    environment {
        EMAIL_RECIPIENT = "${env.USU_EMAIL}"  // MY_EMAIL é uma variável de ambiente definida no Jenkins ou no sistema
    }


    stages {
        stage('Install dependencies') {
            steps {
                script {
                    // Instala as dependências do Python
                    sh 'pip3 install -r requirements.txt --break-system-packages'
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
            // Enviar o e-mail após a execução do pipeline
            emailext(
                to: "${EMAIL_RECIPIENT}",
                subject: "Pipeline Jenkins - Status da execução",
                body: "O pipeline foi executado. Verifique os logs do Jenkins."
            )
        }

        success {
            echo 'Pipeline executado com sucesso!'
        }

        failure {
            echo 'Houve um erro na execução do pipeline!'
        }
    }
}
