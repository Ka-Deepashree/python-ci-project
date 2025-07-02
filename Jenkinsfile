pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'httpsgithub.comKa-Deepashreepython-ci-project.git'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'python main.py'
            }
        }
    }
}
