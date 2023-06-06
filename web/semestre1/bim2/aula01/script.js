var xml = "";
var atualiza;
var table;

function conexao(){
	atualiza = setInterval(function() {loadDoc();}, 3000);
}

function loadDoc(){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if (xhttp.readyState == 4 && xhttp.status == 200){
			atualizar(xhttp)
		}else{
			//depois faz...
		}
    };
	xhttp.open("GET",xml,true);
	xhttp.send();
}

function atualizar(xml){
	var i;
	var xmldoc = xml.responseXML;
	table = "<tr><th>Nome</th> <th>Banda</th> <th>Ano</th> <th>Preço</th> </tr>";
	var x = xmldoc.getElementsByTagName("CD");
	for(i=0; i < x.length ; i++){
		table+="<tr><td>"+x[i].getElementsByTagName("NOME")[0].childNodes[0].nodeValue
		+"</td><td>"+x[i].getElementsByTagName("BANDA")[0].childNodes[0].nodeValue
		+"</td><td>"+x[i].getElementsByTagName("ANO")[0].childNodes[0].nodeValue
		+"</td><td>"+x[i].getElementsByTagName("PRECO")[0].childNodes[0].nodeValue
		+"</td></tr>";
	}
	document.getElementById("tabArticle").innerHTML = null;
	document.getElementById("tabMenu").innerHTML = table;
}

function atualizaArticle(){
	var articleTab = table;
	document.getElementById("tabMenu").innerHTML = null;
	document.getElementById("tabArticle").innerHTML = articleTab;
}

function conectaAjax(){
	if (xml == ""){
		xml = "codcatalog.xml";
		window.alert("Conectado");
		document.getElementById("btnxml").innerHTML = "Desconectar XML";
	}else {
		xml = "";
		window.alert("Desconectado");
		document.getElementById("btnxml").innerHTML = "Conectar XML";
		atualizaArticle();
	}
}