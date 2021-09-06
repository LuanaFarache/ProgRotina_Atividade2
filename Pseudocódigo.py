Algoritmo: Utilização_do_Lokomat®
Var: Aptidão, Seleção_Colete, Medidas_Software, Posicionar_Paciente, Iniciar_Terapia, Vigilância_Paciente e Treino_Marcha: Booleano
Início
Escreva (“O paciente pode usar o Lokomat?  Digite 1 para “sim”, digite 0 para “não””)
  Leia (Apto) 
Escreva (“Colete selecionado? Digite 1 para “Sim”, 0 para “Não””)
  Leia (Colete correto)
Escreva (“Já acrescentou medidas ao software? Digite 1 para “Sim”, 0 para “Não””)
  Leia (Medidas conferidas)
 Escreva (“Paciente posicionado? Digite 1 para “Sim”, 0 para “Não””)
  Leia (Paciente posicionado)
Escreva (“Paciente posicionado? Digite 1 para “Sim”, 0 para “Não””)
  Leia (Paciente posicionado)
Se (Aptidão == 1 & Seleção_Colete == 1 & Medidas_Software == 1 & Posicionar_Paciente == 1) então 
Escreva (“Iniciar Terapia”)
Senão
    Escreva (“Reajustar o sistema”)
Escreva (“Paciente seguro? Digite 1 para “Sim”, 0 para “Não””)
   Leia (Continuar treino)   
Se (Vigilância_Paciente ==1 & Treino_Marcha ==1) então
   Escreva (“Terapia finalizada”)
Senão
   Escreva (“Reajuste terapia)
Fim_se
Fim
