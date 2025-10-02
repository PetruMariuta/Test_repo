pipeline {
    agent { docker { image 'node:22.20.0-alpine3.22' } }
    stages {
        stage('build') {
            steps {
                sh 'node --version'
            }
        }
        stage("test") {
            steps {
                echo "Testing..."
            }


        }

        stage("Deploy") {

            steps {

                echo "Deploy...."
            }
        }
    }
}