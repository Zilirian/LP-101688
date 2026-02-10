Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 10/02/2026
Var
// Seção de Declarações das variáveis 
   idade_de_joao : inteiro
   idade_de_marcia : inteiro
   idade_de_gabriel : inteiro
   soma : inteiro
   subtracao : inteiro
   multiplicacao : inteiro
   divisao : real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreval("Digite um número")
   leia(idade_de_joao)
   escreval
   escreval("Digite outro número")
   leia(idade_de_marcia)
   escreval
   escreval("Digite outro número")
   leia(idade_de_gabriel)
   escreval
   
   soma <- idade_de_joao + idade_de_marcia + idade_de_gabriel
   subtracao <- idade_de_joao - idade_de_marcia - idade_de_gabriel
   multiplicacao <- idade_de_joao * idade_de_marcia * idade_de_gabriel
   divisao <- idade_de_joao / idade_de_marcia / idade_de_gabriel
   
   escreval("A soma das idades é:", soma)
   escreval("a subtração das idades é: ", subtracao)
   escreval("a multiplicação das idades é: ", multiplicacao)
   escreval("a divisão das idades é: ", divisao)
Fimalgoritmo