Algoritmo "semnome"

Var
// Seção de Declarações das variáveis 
   idade : inteiro
   nome : caractere
   primeira_nota : real
   segunda_nota  : real
   soma : real
   media : real
   resultado : caractere
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

   escreval("Digite seu nome:")
   leia(nome)
   
   escreval
   
   escreval("Digite sua idade:")
   leia(idade)

   escreval

   escreval("Digite a primeira nota:")
   leia(primeira_nota)

   escreval

   escreval("Digite a segunda nota:")
   leia(segunda_nota)
   
   escreval
   
   soma <- primeira_nota + segunda_nota
   media <- soma / 2
   
   escreval
   
   se media >= 6 entao
    resultado <- "Aprovado"
   senao
    resultado <- "Reprovado"
   fimse
    
   escreval("Esta é sua idade: ", idade)
   escreval("Esta é seu nome: ", nome)
   escreval("Esta é media das notas: ", media)
   escreval
   escreval("Você foi ", resultado)

Fimalgoritmo