pipeline {
    agent any

    stages {

        stage('Stage One - Clone Repo') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/sejal2130/App.git'
            }
        }

        stage('Stage Two - Check Python Version') {
            steps {
                bat 'python --version'
            }
        }

        stage('Stage Three - Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Stage Four - Run Application') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
