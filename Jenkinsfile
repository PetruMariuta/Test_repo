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
                sh 'make check || true' 
                junit '*.xml'
                echo "Done fra"
            }


        }

        stage("Deploy") {

            steps {

                echo "Deploy...."
                echo "Done fra"
            }
        }
    }
}