/* 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;  */

// Número a ser verificado
let numberToCheck = parseInt(prompt("Qual valor deseja verificar?"), 10);

let fibSequence = [0, 1];
let nextNumber = 1;

while (nextNumber < numberToCheck) {
  nextNumber = fibSequence[fibSequence.length - 1] + fibSequence[fibSequence.length - 2];
  fibSequence.push(nextNumber);
}

if (fibSequence.includes(numberToCheck)) {
  console.log(`O número ${numberToCheck} pertence à sequência de Fibonacci. \n Sequência de Fibonacci gerada: ${fibSequence}`);
  alert(`O número ${numberToCheck} pertence à sequência de Fibonacci.\n Sequência de Fibonacci gerada: ${fibSequence}`);
} else {
  console.log(`O número ${numberToCheck} não pertence à sequência de Fibonacci. \n Sequência de Fibonacci gerada: ${fibSequence}`);
  alert(`O número ${numberToCheck} não pertence à sequência de Fibonacci. \n Sequência de Fibonacci gerada: ${fibSequence}`)
}