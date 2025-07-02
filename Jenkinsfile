pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Ka-Deepashree/python-ci-project.git'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python main.py'
            }
        }
    }
}
