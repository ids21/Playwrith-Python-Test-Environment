# test_env
1. docker-compose up -d
2. docker exec -it jenkins2 bash\
2.1 ssh-keygen -t rsa -f jenkins_agent\
2.2 manage jenkins->credentials->add->SSH Username with private key->save\
3. docker exec -it ssh-agent bash
3.1 cat id_rsa.pub >> authorized_keys
4. docker exec -it ssh-agent bash\
4.1 apt-get update && apt-get -y install python3.9 python3-pip allure