pipeline {
    agent any

    environment {
        IMAGE_NAME = 'story-analyser-ai'
        IMAGE_TAG  = "build-${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Sanity: compile') {
            // Fast feedback: byte-compile all sources to catch syntax errors
            steps {
                sh 'python3 -m py_compile app.py backend/*.py views/*.py'
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Smoke test') {
            // Start the container, confirm Streamlit serves, then tear down
            steps {
                sh '''
                    docker rm -f ${IMAGE_NAME}-smoke || true
                    docker run -d --name ${IMAGE_NAME}-smoke -p 8599:8501 ${IMAGE_NAME}:${IMAGE_TAG}
                    for i in $(seq 1 20); do
                        if curl -sf http://localhost:8599/_stcore/health; then
                            echo "Streamlit is up"; exit 0
                        fi
                        sleep 3
                    done
                    echo "Streamlit did not become healthy"; exit 1
                '''
            }
            post {
                always {
                    sh 'docker rm -f ${IMAGE_NAME}-smoke || true'
                }
            }
        }
    }

    post {
        success { echo "Built ${IMAGE_NAME}:${IMAGE_TAG} successfully." }
        failure { echo 'Pipeline failed — check the stage logs above.' }
    }
}
