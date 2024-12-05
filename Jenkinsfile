pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from the Git repository
                git branch: 'main', url: 'https://github.com/aminaTr/nextjs-app.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Pull the Node.js image
                    def nodeImage = docker.image('node:20') // Specify your Node.js version here
                    nodeImage.pull() // Pull the image if not already available

                    // Run npm install inside the Docker container
                    nodeImage.inside {
                        sh 'export NPM_CONFIG_CACHE=/var/lib/jenkins/.npm'
                        sh 'npm install'
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests inside the Docker container
                    docker.image('node:20').inside {
                        sh 'npm test'
                    }
                }
            }
        }

        stage('Build Application') {
            steps {
                script {
                    // Build the application inside the Docker container
                    docker.image('node:20').inside {
                        sh 'npm run build'
                    }
                }
            }
        }
    }

    post {
        always {
            // Archive artifacts or perform cleanup
            echo 'Pipeline completed!'
        }
    }
}
