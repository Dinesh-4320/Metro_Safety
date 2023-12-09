pipeline{
  agent any
  stages{
    stage("Making Prediction on images"){
      steps{
      	sh '''
      		python generate_Payload.py
      	'''  
        }
      }
    }
  }
}
