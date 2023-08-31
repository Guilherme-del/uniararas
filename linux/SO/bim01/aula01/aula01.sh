if [ $1 == "--help" ] || [ $# -eq 0 ]
then
	echo "Uso: ./installFHO.sh [-p proxy] pacotes"
else
	read -p "RA: " RA
	read -s -p "Senha: " PASS

	FHO_PROXY="proxylab2.uniararas.br:8080"
	PACKS=$@
	if [ $1 == "-p" ]
	then
		if [ $# -gt 2 ]
		then
			FHO_PROXY=$2
			PACKS=${@:3:$#}
			echo -e "Serão instalados:\n$PACKS"
		else
			echo -e "Número de parâmetros inválidos!\n"
			exit 1
		fi
	fi
	PROXY_HTTP="http://$RA:$PASS@$FHO_PROXY"
	PROXY_HTTPS="https://$RA:$PASS@$FHO_PROXY"

	sudo echo -e "Acquire::http::Proxy \"$PROXY_HTTP\";\nAcquire::https::Proxy \"$PROXY_HTTPS\";" > /etc/apt/apt.conf

	sudo apt update -y
	sudo apt upgrade -y
	sudo apt install $PACKS

	unset PASS PROXY_HTTP PROXY_HTTPS
fi