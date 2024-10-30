#!/bin/bash

echo "Iniciando a configuracao da rede e dos nodes..."

# Passo 1: Criar a rede
echo "Passo 1: Criando a rede 'mynetwork'..."
docker network create mynetwork

# Passo 2: Criar containers MASTER
echo "Passo 2: Criando os containers MASTER..."
docker run -d --name master1 --network mynetwork alpine sleep infinity
docker run -d --name master2 --network mynetwork alpine sleep infinity

# Passo 3: Criar containers SLAVE
echo "Passo 3: Criando os containers SLAVE..."
docker run -d --name slave1 --network mynetwork alpine sleep infinity
docker run -d --name slave2 --network mynetwork alpine sleep infinity
docker run -d --name slave3 --network mynetwork alpine sleep infinity

# Passo 4: Adicionar token aos MASTERs
echo "Passo 4: Adicionando o token aos MASTERs..."
TOKEN="XYZ123"
echo $TOKEN | docker exec -i master1 sh -c "cat > /token.txt"
echo $TOKEN | docker exec -i master2 sh -c "cat > /token.txt"

# Passo 5: Exibir o token do MASTER 1
echo "Passo 5: Exibindo o token do MASTER 1..."
docker exec master1 cat /token.txt

# Passo 6: Listar todos os nodes criados
echo "Passo 6: Listando todos os nodes criados na rede 'mynetwork'..."
docker ps --filter "network=mynetwork" --format "{{.Names}}"

# Passo 7: Criar containers Ubuntu e Fedora
echo "Passo 7: Criando containers iterativos para Ubuntu e Fedora..."
docker run -d --name ubuntu_container ubuntu sleep infinity
docker run -d --name fedora_container fedora sleep infinity

# Passo 8: Verificar distribuicao no container Ubuntu
echo "Passo 8: Verificando a distribuicao no container Ubuntu..."
docker exec ubuntu_container cat /etc/os-release

# Passo 9: Verificar distribuicao no container Fedora
echo "Passo 9: Verificando a distribuicao no container Fedora..."
docker exec fedora_container cat /etc/os-release

# Passo 10: Exibir tamanho dos containers Ubuntu e Fedora
echo "Passo 10: Exibindo o tamanho dos containers Ubuntu e Fedora..."
docker ps --filter "name=ubuntu_container" --size
docker ps --filter "name=fedora_container" --size

# Passo 11: Listar containers Ubuntu e Fedora
echo "Passo 11: Listando os containers Ubuntu e Fedora criados..."
docker ps --filter "name=ubuntu_container"
docker ps --filter "name=fedora_container"

# Passo 12: Remover containers Ubuntu e Fedora
echo "Passo 12: Removendo os containers Ubuntu e Fedora..."
docker rm -f ubuntu_container fedora_container

# Passo 13: Criar containers de servidores para Apache, MySQL e WildFly
echo "Passo 13: Criando containers de servidores para Apache, MySQL e WildFly..."
docker run -d --name apache_server httpd:latest
docker run -d --name mysql_server mysql:latest
docker run -d --name wildfly_server jboss/wildfly:latest

# Passo 14: Listar containers de servidores criados
echo "Passo 14: Listando os containers de servidores criados..."
docker ps --filter "name=apache_server"
docker ps --filter "name=mysql_server"
docker ps --filter "name=wildfly_server"

echo "Script concluido com sucesso."
