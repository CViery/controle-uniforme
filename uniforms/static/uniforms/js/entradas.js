
const calcular_valor = () => {
    let quantidade = document.getElementById('quantidade').value;
    let valor_uni = document.getElementById('valor_uni').value;

    // Converte os valores para número
    let valor_total = parseFloat(quantidade) * parseFloat(valor_uni);

    // Define o valor total no campo
    document.getElementById('valor_total').value = valor_total.toFixed(2); // Exibe com duas casas decimais
}