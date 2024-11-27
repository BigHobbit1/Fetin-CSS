pipeline {
    agent any

    environment {
        // Define a variável de ambiente com o e-mail de destino
        MY_EMAIL = 'vitorpestalozi1@gmail.com'  // Substitua pelo seu e-mail
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
    
    post {
        always {
            // Chama o script para enviar o e-mail com a execução do pipeline
            script {
                def pipelineStatus = currentBuild.result ?: 'SUCCESS'  // Verifica o status da execução
                def emailBody = "Pipeline executado. Status: ${pipelineStatus}.\n\nVerifique os logs do Jenkins para mais detalhes."
                sh 'chmod +x send_email.sh'
                
                // Chama o script para enviar o e-mail
                sh "echo '${emailBody}' | /bin/bash scripts/send_email.sh ${MY_EMAIL}"
            }
        }

        success {
            echo 'Pipeline executado com sucesso!'
        }

        failure {
            echo 'Houve um erro na execução do pipeline!'
        }
    }
}
