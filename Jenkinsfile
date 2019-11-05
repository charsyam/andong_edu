pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        sh '''pyenv local nadia-env
pyenv rehash
pip install -r ./requirements.txt
cd oss && ./run_tests.sh

ssh -i /var/lib/jenkins/id_rsa charsyam@nadia003.hawin.win "cd andong_edu && git pull"
ssh -i /var/lib/jenkins/id_rsa charsyam@nadia003.hawin.win "sudo systemctl restart gunicorn"
'''
      }
    }

  }
}