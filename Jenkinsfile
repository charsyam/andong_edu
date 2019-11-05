pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        sh '''pyenv local nadia-env
pyenv rehash
pip install -r ./requirements.txt
cd oss && ./run_tests.sh
'''
      }
    }

  }
}
