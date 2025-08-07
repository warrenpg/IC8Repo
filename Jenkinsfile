pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sshagent(['ubuntu']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@3.81.125.60 <<EOF
if [ ! -d "repo" ]; then
    git clone https://github.com/warrenpg/IC8Repo.git repo
else
    echo "Repository already exists."
    cd repo
    git pull
fi
EOF
                    '''
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sshagent(['ubuntu']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@3.81.125.60 <<EOF
sudo apt update
sudo apt install -y python3-flask
sudo apt install -y python3-flask-cors
EOF
                    '''
                }
            }
        }
        
        stage('Build and Run') {
            steps {
                sshagent(['ubuntu']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@3.81.125.60 <<EOF
cd repo

# Stop any running Flask app instance
sudo pkill -f "app.py" || echo "Flask app is not running."

# Start the Flask app in the background
sudo nohup python3 app.py > nohup.out 2>&1 &
disown
EOF
                    '''
                }
            }
        }
    }
}