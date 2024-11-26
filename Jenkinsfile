pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-jenkins-pandas-numpy:latest'  // Nome da imagem Docker
    }

    stages {
        stage('Checkout') {
            steps {
                // Clonar o repositório Git
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Construir a imagem Docker a partir do Dockerfile
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Data Collection') {
            steps {
                script {
                    // Rodar o script Python para coleta de dados dentro do container Docker
                    docker.image(DOCKER_IMAGE).inside {
                        // Rodar o script Python de coleta de dados (ajuste conforme sua aplicação)
                        sh 'python3 collect_data.py'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // (Opcional) Push da imagem Docker para o Docker Hub ou outro registro
                    echo 'Push Docker Image (não implementado neste exemplo)'
                    // docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                    //     docker.image(DOCKER_IMAGE).push()
                    // }
                }
            }
        }
    }

    post {
        always {
            // Limpar o workspace após a execução do pipeline
            cleanWs()
        }
    }
}
