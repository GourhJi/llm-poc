pipeline {

 agent any

 stages {

  stage('Build Image') {
   steps {
    sh 'docker build -t llm-model:${BUILD_NUMBER} .'
   }
  }

  stage('Run Container') {
   steps {
    sh '''
    docker stop llm-app || true
    docker rm llm-app || true
    docker run -d -p 8000:8000 --name llm-app llm-model:${BUILD_NUMBER}
    '''
   }
  }

 }

}
