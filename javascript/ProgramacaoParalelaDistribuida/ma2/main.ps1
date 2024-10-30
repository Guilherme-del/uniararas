Write-Output "Iniciando a configuracao da rede e dos nodes..."

# 1) Rede com 5 PCs, 2 MASTERs e 3 SLAVEs

Write-Output "Passo 1: Criando a rede 'mynetwork'..."
docker network create mynetwork

Write-Output "Passo 2: Criando os containers MASTER..."
docker run -d --name master1 --network mynetwork alpine sleep infinity
docker run -d --name master2 --network mynetwork alpine sleep infinity

Write-Output "Passo 3: Criando os containers SLAVE..."
docker run -d --name slave1 --network mynetwork alpine sleep infinity
docker run -d --name slave2 --network mynetwork alpine sleep infinity
docker run -d --name slave3 --network mynetwork alpine sleep infinity

Write-Output "Passo 4: Adicionando o token aos MASTERs..."
docker exec master1 sh -c "echo 'TOKEN_MASTER=XYZ123' >> /etc/environment"
docker exec master2 sh -c "echo 'TOKEN_MASTER=XYZ123' >> /etc/environment"

Write-Output "Passo 5: Exibindo o token do MASTER 1..."
docker exec master1 sh -c 'source /etc/environment && echo $TOKEN_MASTER'

Write-Output "Passo 6: Listando todos os nodes criados na rede 'mynetwork'..."
docker ps --filter "network=mynetwork" --format "{{.Names}}"

# 2) Containers iterativos com distribuicoes Ubuntu e Fedora

Write-Output "Passo 7: Criando containers iterativos para Ubuntu e Fedora..."
docker run -d --name ubuntu_container ubuntu sleep infinity
docker run -d --name fedora_container fedora sleep infinity

Write-Output "Passo 8: Verificando a distribuicao no container Ubuntu..."
docker exec ubuntu_container cat /etc/os-release

Write-Output "Passo 9: Verificando a distribuicao no container Fedora..."
docker exec fedora_container cat /etc/os-release

Write-Output "Passo 10: Exibindo o tamanho dos containers Ubuntu e Fedora..."
docker ps -s --filter "name=ubuntu_container"
docker ps -s --filter "name=fedora_container"

Write-Output "Passo 11: Listando os containers Ubuntu e Fedora criados..."
docker ps -a --filter "name=ubuntu_container"
docker ps -a --filter "name=fedora_container"

Write-Output "Passo 12: Removendo os containers Ubuntu e Fedora..."
docker rm -f ubuntu_container fedora_container

# 3) Containers nao iterativos para servidores (CAAS)

Write-Output "Passo 13: Criando containers de servidores para Apache, MySQL e WildFly..."
docker run -d --name apache_server httpd:latest
docker run -d --name mysql_server -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:latest
docker run -d --name wildfly_server jboss/wildfly:latest

Write-Output "Passo 14: Listando os containers de servidores criados..."
docker ps --filter "name=apache_server"
docker ps --filter "name=mysql_server"
docker ps --filter "name=wildfly_server"

Write-Output "Script concluido com sucesso."
