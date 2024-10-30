#!/bin/bash

# Inicializar o Docker Swarm, caso ainda não esteja inicializado
echo "Inicializando o Docker Swarm..."
docker swarm init || echo "Swarm já inicializado ou erro ao inicializar."

# Construir a imagem do backend
echo "Construindo a imagem do backend..."
docker build -t mean_backend -f ../backEnd/dockerFile ../backEnd

# Construir a imagem do frontend
echo "Construindo a imagem do frontend..."
docker build -t mean_frontend -f ../frontEnd/dockerFile ../frontEnd

# Executar o Docker Stack com as imagens recém-criadas
echo "Iniciando o deploy no Docker Swarm..."
docker stack deploy --compose-file docker-compose.yml mean-stack

# Verificar o status dos serviços na stack
echo "Verificando o status dos serviços da stack..."
docker stack services mean-stack

echo "Deploy concluído. Todos os serviços foram iniciados."
