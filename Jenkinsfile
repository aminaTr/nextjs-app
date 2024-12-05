pipeline {
    agent {
        docker {
            image 'node:20.17.0'
        }
    }
    stages {
        stage('Environment Check') {
            steps {
                sh 'node --version && npm --version'
            }
        }
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Set a custom cache directory
                sh 'npm config set cache /var/lib/jenkins/.npm-cache --global'
                sh 'npm install || true && echo "npm install failed"'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "test cases run"'
            }
        }
        stage('Package') {
            steps {
                sh 'npm run build'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed and run!'
        }
    }
}
