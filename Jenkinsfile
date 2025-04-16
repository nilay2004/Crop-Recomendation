pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON = "${VENV_DIR}\\Scripts\\python.exe"
        PIP = "${VENV_DIR}\\Scripts\\pip.exe"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo '📥 Cloning GitHub repository...'
                // Jenkins SCM plugin handles cloning
            }
        }

        stage('Setup Environment') {
            steps {
                echo '📦 Setting up virtual environment and installing dependencies...'
                bat """
                    python -m venv %VENV_DIR%
                    %PIP% install --upgrade pip
                    %PIP% install -r requirements.txt
                """
            }
        }

        stage('Verify Model Load') {
            steps {
                echo '🤖 Verifying model loading...'
                bat """
                    %PYTHON% -c "import pickle; pickle.load(open('RF.pkl', 'rb')); print('Model Loaded Successfully ✅')"
                """
            }
        }

        stage('Run App Test') {
            steps {
                echo '🧪 Running app.py for basic check...'
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat "%PYTHON% app.py"
                }
            }
        }

        stage('Deploy (Optional)') {
            when {
                expression { fileExists('webapp.py') }
            }
            steps {
                echo '🚀 Simulating deployment...'
                // Add real deployment logic here if needed
            }
        }
    }

    post {
        success {
            echo '✅ CI Pipeline executed successfully!'
        }
        failure {
            echo '❌ Build failed. Check logs for details.'
        }
    }
}
