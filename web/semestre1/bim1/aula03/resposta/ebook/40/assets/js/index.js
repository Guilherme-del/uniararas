function calcularValor() {
  var numNoites = document.getElementById("num-noites").value;
  var numConvidados = document.getElementById("num-convidados").value;
  var diarias = numNoites * 99; // valor das diárias sem adição de convidados
  var adicionalConvidados = numConvidados * 10 * numNoites; // valor do adicional de convidados
  var total = diarias + adicionalConvidados;
  
  document.getElementById("total").value = total.toFixed(2); // formata o valor com duas casas decimais
}