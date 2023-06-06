function displayZoo(i) {
  // carrega o arquivo XML usando AJAX
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // cria uma referência à árvore DOM do arquivo XML
      var xmlDoc = this.responseXML;
      // obtém a lista de elementos "animal" no arquivo XML
      var animals = xmlDoc.getElementsByTagName("animal");
      // obtém o elemento "animal" correspondente à posição i
      var animal = animals[i];
      // obtém os valores dos elementos do animal
      var nome = animal.getElementsByTagName("nome")[0].childNodes[0].nodeValue;
      var nomecientifico = animal.getElementsByTagName("nomecientifico")[0].childNodes[0].nodeValue;
      var sexo = animal.getElementsByTagName("sexo")[0].childNodes[0].nodeValue;
      var datanascimento = animal.getElementsByTagName("datanascimento")[0].childNodes[0].nodeValue;
      var origem = animal.getElementsByTagName("origem")[0].childNodes[0].nodeValue;
      var veterinarioresponsavel = animal.getElementsByTagName("veterinarioresponsavel")[0].childNodes[0].nodeValue;
      // exibe as informações do animal na tela
      var info = "Nome: " + nome + "<br>" +
                 "Nome científico: " + nomecientifico + "<br>" +
                 "Sexo: " + sexo + "<br>" +
                 "Data de nascimento: " + datanascimento + "<br>" +
                 "Origem: " + origem + "<br>" +
                 "Veterinário responsável: " + veterinarioresponsavel;
      document.getElementById("info").innerHTML = info;
    }
  };
  xmlhttp.open("GET", "zoo_catalog.xml", true);
  xmlhttp.send();
}