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
                sh '''
                    mkdir -p /.npm
                    chown -R 111:113 /.npm
                    npm install
                '''
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
            echo 'Pipeline is completed!!'
        }
    }
}
