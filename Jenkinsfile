pipeline {
    agent any 
        stages {
            stage ('Checkout code') {
                steps {
                   git credentialsId: 'MY_PAT', url: "https://github.com/gayathri7022/practice2.git", branch: "master"
                }
            }

            stage ('Install dpendencies') {
                steps {
                   bat '''
                    "C:\\Users\\mjmnj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                    call .\\venv\\Scripts\\activate
                    pip install -upgrade pip
                    pip install pytest
                    '''
                }
            }

            stage ('Test') {
                steps {
                    bat '''
                    call .\\venv\\Scripts\\activate
                    pytest test.py
                    '''
                }
            }

            stage ('Deploy') {
                steps {
                    bat '''
                    call .\\venv\\Scripts\\activate
                    "C:\\Users\\mjmnj\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" palindrome.py
                    '''
                }
            }
        }        
    

        post {
            success {
                echo 'pipeline succeded'
            }
            failure {
                echo 'pipeline failed'
             }
        }
}