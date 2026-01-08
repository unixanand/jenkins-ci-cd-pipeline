pipeline {
    agent any

    environment {
        APP_DIR = "/home/ec2-user/app"
        VENV_DIR = "/home/ec2-user/app/venv"
        PORT = "8501"
    }

    stages {

        stage('Clone Repo') {
            steps {
                sh '''
                rm -rf /home/ec2-user/app/*
                git clone https://github.com/unixanand/jenkins-ci-cd-pipeline.git /home/ec2-user/app
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv $VENV_DIR
                $VENV_DIR/bin/pip install --upgrade pip
                $VENV_DIR/bin/pip install -r /home/ec2-user/app/requirements.txt
                '''
            }
        }

        stage('Stop Old App') {
            steps {
                sh '''
                pkill -f streamlit || true
                '''
            }
        }

        stage('Start Streamlit App') {
            steps {
                sh '''
                nohup $VENV_DIR/bin/streamlit run /app/demo.py --server.port $PORT --server.address 0.0.0.0 > /home/ec2-user/app/app.log 2>&1 &
                '''
            }
        }
    }
}
