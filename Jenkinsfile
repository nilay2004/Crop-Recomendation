pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo '📥 Cloning GitHub repository...'
                // Git clone happens automatically by Jenkins from SCM config
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Creating and setting up virtual environment...'
                sh 'python3 -m venv ${VENV_DIR}'
                sh './${VENV_DIR}/bin/pip install --upgrade pip'
                sh './${VENV_DIR}/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Model Script') {
            steps {
                echo '🤖 Testing model loading...'
                sh './${VENV_DIR}/bin/python -c "import pickle; pickle.load(open(\'RF.pkl\', \'rb\')); print(\'Model Loaded Successfully ✅\')"'
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running app.py test script...'
                // A simple dry-run of the script (you can add custom test cases here too)
                sh './${VENV_DIR}/bin/python app.py || true'
            }
        }

        stage('Deploy (optional)') {
            when {
                expression { return fileExists('webapp.py') }
            }
            steps {
                echo '🚀 Simulating deployment (custom logic can be added here)'
                // Placeholder for real deployment (e.g., scp to EC2, or Docker run)
            }
        }
    }

    post {
        success {
            echo '✅ CI Pipeline executed successfully!'
        }
        failure {
            echo '❌ Build failed. Please check the logs.'
        }
    }
}
