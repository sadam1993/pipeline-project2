print('My first python job  within Jenkinsfile.')
pipeline {
    agent any
    stages {
        stage('run') {
            steps {
                echo 'Welcome to Jenkins World'
                sh 'python --version'
                sh 'python pipeline.py'
                sh 'date'
            }
        }
    }
}
