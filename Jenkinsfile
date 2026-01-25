pipeline {
    agent any

    environment {
        PYTHON = "C:\\Python311\\python.exe"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/sejal2130/App.git'
            }
        }

        stage('Check Python Version') {
            steps {
                bat '"%PYTHON%" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                bat '"%PYTHON%" app.py'
            }
        }
    }
}
