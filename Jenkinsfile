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
            sh '''
               cd scripts
               chmod 775 *
               ./shell.sh
               '''
        }

        success {
            echo 'Pipeline executado com sucesso!'
            sh '''
               cd scripts
               chmod 775 *
               ./shell.sh
               '''
        }

        failure {
            echo 'Houve um erro na execução do pipeline!'
        }
    }
}
