#!/bin/sh
# init-replica.sh

echo "Aguardando MongoDB iniciar..."

# Loop para verificar a disponibilidade do MongoDB antes de prosseguir
until mongosh "mongodb://mongo:27017" --eval "db.runCommand({ ping: 1 })" &>/dev/null; do
  echo "MongoDB ainda não está disponível, aguardando..."
  sleep 2
done

echo "MongoDB está disponível, iniciando replica set"

mongosh "mongodb://mongo:27017" <<EOF
rs.initiate()
rs.add("mongo_replica_1:27017")
rs.add("mongo_replica_2:27017")
EOF

echo "Replica set iniciado com sucesso"
