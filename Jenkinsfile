pipeline {
    agent any
    stages{
        stage ('Playwright teste'){
            steps{
                dir('playwright-test'){
                    git 'https://github.com/viniciuswdmf/serverest_frontend_automation'
                    bat 'cd bdd'
                    bat 'behave -i login.feature -D ambiente=stage'
                }
            }
        }
    }
}