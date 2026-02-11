Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
Var
// Seção de Declarações das variáveis 
   nota1 : real
   nota2 : real
   nota3 : real
   media : real
 

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
  escreval("Digite sua 1° nota")
  leia(nota1)
  escreval
  escreval("Digite sua 2° nota")
  leia(nota2)
  escreval
  escreval("Digite sua 3° nota")
  leia(nota3)
  escreval

  media <- (nota1 + nota2 + nota3) / 3

  escreval("Sua média é:", media)

  se( media >= 7) entao
  escreva("O aluno foi aprovado")
  senao
  escreva("O aluno foi reprovado")
  fimse
  escreval
  

Fimalgoritmo
