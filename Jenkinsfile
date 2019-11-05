pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        sh '''pip install -r ./requirements.txt
cd oss && ./run_tests.sh'''
      }
    }

  }
}