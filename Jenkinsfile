pipeline {
    agent any

    stages {
        stage ('stage one') {
            steps {
                git branch: 'master',
                  url: 'https://github.com/sejal2130/App.git'
            }
        }
        stage ('stage Two') {
            steps {
                sh """ python --version """
            }
        }
        stage('stage Three') {
            steps {
                bat """
                    pip install -r requirements.txt
                    """

            }
        }
        stage('stage Four') {
            steps {
                baat """
                 python app.py 
                """
            }
        }
    }
}
