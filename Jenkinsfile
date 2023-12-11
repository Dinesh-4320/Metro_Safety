pipeline{
  agent any
  stages{
    stage("Making Prediction on images"){
      steps{
      	sh '''
      		python3 generate_Payload.py
      	'''  
      }
    }
  }
}
