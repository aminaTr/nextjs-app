pipeline {
    agent any 
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Environment Check') {
            steps {
                sh 'node --version'
                sh 'npm --version'
            }
        }
        stage('Build') {
            steps {
                sh 'npm config set cache ${WORKSPACE}/.npm-cache --global'
                sh 'npm install'
                sh 'npm run build'
            }
        }
        stage('Test') {
            steps {
                sh 'echo test cases run'
            }
        }
        stage('Package') {
            steps {
                sh 'npm run package'
            }
        }
    }
    post {
        always {
            echo 'Pipeline is completed!!'
        }
    }
}
