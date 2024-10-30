# Verificar se o Docker Swarm esta inicializado
$swarmStatus = docker info | Select-String "Swarm: active"
if (-not $swarmStatus) {
    Write-Output "Inicializando o Docker Swarm..."
    docker swarm init
} else {
    Write-Output "Swarm ja esta inicializado."
}

# Construir a imagem do backend
Write-Output "Construindo a imagem do backend..."
docker build -t mean_backend -f ../backEnd/dockerFile ../backEnd

# Construir a imagem do frontend
Write-Output "Construindo a imagem do frontend..."
docker build -t mean_frontend -f ../frontEnd/dockerFile ../frontEnd

# Executar o Docker Stack com as imagens recem-criadas
Write-Output "Iniciando o deploy no Docker Swarm..."
docker stack deploy --compose-file docker-compose.yml mean-stack

# Verificar o status dos servicos na stack
Write-Output "Verificando o status dos servicos da stack..."
docker stack services mean-stack

Write-Output "Deploy concluido. Todos os servicos foram iniciados."
