# test_env
1. docker-compose up -d
2. docker exec -it jenkins2 bash
2.1 ssh-keygen -t rsa -f jenkins_agent
2.2 manage jenkins->credentials->add->SSH Username with private key->save
2.3 docker run -d --user root --name ssh-agent --expose 22 -e "JENKINS_AGENT_SSH_PUBKEY=$( cat .ssh/jenkins_agent.pub )" --network ddev_default jenkins/ssh-agent:jdk11
2.4 configure agent JavaPath=/opt/java/openjdk/bin/java, host=ssh-agent, remote_dir=/home/jenkins/agent ...
    
