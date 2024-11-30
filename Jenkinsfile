pipeline {
    agent {
        docker {
            image 'node:20.17.0' // Replace with a suitable image for your app
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'npm install' // Replace with your app's build commands
            }
        }
        stage('Test') {
            steps {
                sh 'npm test' // Replace with your app's test commands
            }
        }
        stage('Package') {
            steps {
                sh 'npm run build' // Replace with your app's packaging commands
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
