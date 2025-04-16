pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON_BIN = 'C:\\Python310\\python.exe'
        PIP_BIN = 'venv\\Scripts\\pip.exe'
        PYTHON_VENV_BIN = 'venv\\Scripts\\python.exe'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo '📥 Cloning GitHub repository...'
                // Jenkins handles SCM checkout
            }
        }

        stage('Setup Environment') {
            steps {
                echo '📦 Setting up virtual environment and installing dependencies...'
                bat """
                    "%PYTHON_BIN%" -m venv %VENV_DIR%
                    %PIP_BIN% install --upgrade pip
                    %PIP_BIN% install -r requirements.txt
                """
            }
        }

        stage('Verify Model Load') {
            steps {
                echo '🤖 Verifying model loading...'
                bat """
                    %PYTHON_VENV_BIN% -c "import pickle; pickle.load(open('RF.pkl', 'rb')); print('Model Loaded Successfully ✅')"
                """
            }
        }

        stage('Run App Test') {
            steps {
                echo '🧪 Running app.py for basic check...'
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat "%PYTHON_VENV_BIN% app.py"
                }
            }
        }

        stage('Deploy (Optional)') {
            when {
                expression { fileExists('webapp.py') }
            }
            steps {
                echo '🚀 Simulating deployment...'
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
