/* 1) Observe o trecho de código abaixo: 
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA? */

let i = 13;
let k = 0;
let soma = 0;

while (k < i) {
    k++;
    soma += k;
}

console.log(`Soma = ${soma}`);

/* Console retorna com soma = 91 */