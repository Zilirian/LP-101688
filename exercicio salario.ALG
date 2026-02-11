Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 11/02/2026
Var
// Seção de Declarações das variáveis 
   salario : real
   salario_minimo : real
   quantidade_salarios : real
   imposto_renda : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreval("Informe seu salário")
   escreval
   
   escreval("Digite seu salário:")
   leia(salario)
   
   escreval
   
   salario_minimo <- 1621
   quantidade_salarios <- salario / salario_minimo
   imposto_renda <- (salario * 22) / 100

   se(quantidade_salarios >= 3) entao
   escreval("Seu imposto de renda será: ", imposto_renda)
   fimse
   

   escreval("A quantidade de salários é: ", quantidade_salarios:3:2)
   
   
   
   
Fimalgoritmo