pipeline {
    agent any

    environment {
        PYTHON_BIN = 'C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo '📥 Cloning GitHub repository...'
                git branch: 'main', url: 'https://github.com/nilay2004/Crop-Recomendation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                bat """
                    "%PYTHON_BIN%" -m pip install --upgrade pip
                    "%PYTHON_BIN%" -m pip install -r requirements.txt
                """
            }
        }

        stage('Verify Model Load') {
            steps {
                echo '🤖 Verifying RF.pkl model loading...'
                bat """
                    "%PYTHON_BIN%" -c "import pickle; pickle.load(open('RF.pkl', 'rb')); print('Model Loaded Successfully ✅')"
                """
            }
        }

        stage('Run App Test') {
            steps {
                echo '🧪 Running app.py for basic check...'
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat "\"%PYTHON_BIN%\" app.py"
                }
            }
        }

        stage('Deploy (Optional)') {
            when {
                expression { fileExists('webapp.py') }
            }
            steps {
                echo '🚀 Simulating deployment...'
                // Add deployment logic here if needed
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
