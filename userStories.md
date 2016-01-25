# User Stories #

# Projeto I #

## US01 ##

| Estudos das ferramentas/linguagens necessárias para o ambiente de trabalho. Aqui deve-se estudar Python, PyUnit e PyEasyAccept para testes, framework QT para interface gráfica e estudar como gerar um pacote de instalação para Debian (.deb). Deve-se, também estudar conceitos de matemática financeira, bem como o funcionamento da HP12-C. |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Cada integrante será responsável por estudar uma das novas tecnologias e como resultado apresentará um seminário para os demais membros da equipe.                                                                                                                                                                                        |
| TA 2 - Cada integrante da equipe deverá implementar uma calculadora de funções básicas (soma, subtração, multiplicação, divisão) utilizando as tecnologias a serem empregadas ( python, interface em Qt, instalador .deb, tratamento de erros) para validar o estudo. Essa calculadora deve rodar no N800.                                       |
| TA 3 - Cada integrante deverá cumprir uma série de exercícios pré-selecionados para demonstrar o aprendizado na manipulacão da calculadora.                                                                                                                                                                                                      |
| **Estimativa Inicial: 88 h**                                                                                                                                                                                                                                                                                                                     |

## US02 ##

| Configuração do ambiente de trabalho. Aqui deve-se configurar: sistema operacional Ubuntu, IDE Eclipse, plugin PyDev, frameworks PyUnit e PyEasyAccept para testes, framework QT para interface gráfica, bind de Qt para Python, Scratchbox e Qt Designer (aqui será realizada uma avaliação da ferramenta de modo a verificar a compatibilidade da mesma com o PyQt). Além disso deve-se realizar as configurações necessárias no N800 como Python, Maemo Diablo, QT, etc. |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Estimativa Inicial: 42 h**                                                                                                                                                                                                                                                                                                                                                                                                                                                |



## US03 ##

| O usuário deve ser capaz de entrar valores na calculadora, determinando a formatação dos mesmos, bem como limpar os valores que ficarem armazenados em registradores. Essa US consiste em implementar o setor de entrada de dados e setor de limpeza. Aqui estamos considerando implementar interface, lógica e instalador. |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Comparar os resultados obtidos com a nossa implementação com os da HP-12c                                                                                                                                                                                                                                            |
| **Estimativa Inicial: 36 h**                                                                                                                                                                                                                                                                                                |

## US04 ##

| O usuário deve ser capaz de utilizar a calculadora como calculadora matemática. O mesmo deve poder realizar operações de soma, subtração, multiplicação e divisão. Essa US consiste em implementar o setor de operações matemáticas básicas da HP-12c e CHS: +, -, ×, ÷. |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Comparar os resultados obtidos com a nossa implementação com os da HP-12c                                                                                                                                                                                         |
| **Estimativa Inicial: 30 h**                                                                                                                                                                                                                                             |

## US05 ##

| O usuário deve ser capaz de realizar um conjunto de operações financeiras de modo à determinar períodos de investimento, taxa de juros, valor presente, valor futuro e parcela de pagamento. Essa US consiste em implementar as funções financeiras básicas (n, i, PV, PMT, FV). |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Comparar os resultados obtidos com a nossa implementação com os da HP-12c                                                                                                                                                                                                 |
| **Estimativa Inicial: 36 h**                                                                                                                                                                                                                                                     |

## US06 ##

| O usuário deve ser capaz de avaliar, além dos valores da US anterior para seus investimentos, os dados referentes ao valor presente líquido e a taxa interna de retorno do mesmo. Essa US consiste em implementar as funções financeiras: NPV, IRR. |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Comparar os resultados obtidos com a nossa implementação com os da HP-12c                                                                                                                                                                    |
| **Estimativa Inicial: 29 h**                                                                                                                                                                                                                        |

## US07 ##

| O usuário deve ser capaz de avaliar a amortização no pagamento de parcelas, os juros acumulados no período do investimento e arredondar valores calculados. Essa US consiste em implementar as funções financeiras: AMORT Simples, AMORT Francesa, RND. |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Comparar os resultados obtidos com a nossa implementação com os da HP-12c                                                                                                                                                                        |
| **Estimativa Inicial: 20 h**                                                                                                                                                                                                                            |


## US08 ##

| O usuário deve ser capaz de manipular fluxos de caixa na análise de seus investimentos. Essa US consiste em implementar as funções financeiras: CFo, CFj, Nj. |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Comparar os resultados obtidos com a nossa implementação com os da HP-12c                                                                              |
| **Estimativa Inicial: 40 h**                                                                                                                                  |



---


# Projeto 2 #


## US 09 ##

| Essa US consiste em elaborar a documentação formal do projeto através da escrita de uma monografia a ser entregue no final do semestre. |
|:----------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Avaliacao da mesma segundo o cliente                                                                                             |
| **Estimativa Inicial: 30h**                                                                                                             |

## US10 ##

| Dados os problemas encontrados na convergência das fórmulas o objetivo dessa US é encontrar um conjunto final de fórmulas a serem utilizadas cujos resultados sejam coerentes com os apresentados pela HP12-C.  |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Elaboracao de testes de aceitação e unidade para os mesmos de acordo com os resultados da HP12-C                                                                                                         |
| TA 2 - Documentação das fórmulas                                                                                                                                                                                |
| **Estimativa Inicial: 30 h**                                                                                                                                                                                    |

## US11 ##

| Essa US deve permitir ao usuário da calculadora realizar conversões de taxas de juros e períodos de aplicação. O usuário será capaz de informar uma taxa de juros anual e requisitar sua conversão para uma taxa mensal (função 12/) ou ainda informar um período em anos de seu investimento e requisitar a conversão desse período para meses (função 12x).  |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Elaboração de testes de aceitação para os mesmos conforme resultados da HP12-C.                                                                                                                                                                                                                                                                         |
| **Estimativa Inicial: 30 h**                                                                                                                                                                                                                                                                                                                                   |

## US12 ##

| O usuário da calculadora deverá ser capaz de manipular os 18 registradores simples da mesma, fora os outros 5 financeiros. Com isso o usuário deve ser capaz de atribuir valores a esses registradores, bem como recuperar os valores armazenados. Aqui também teremos a implementação da função de rolagem de valores dos registradores X, Y, Z e W. |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Comparar os resultados obtidos com a nossa implementação com os da HP-12c                                                                                                                                                                                                                                                                      |
| **Estimativa Inicial: 20 h**                                                                                                                                                                                                                                                                                                                          |


## US13 ##

| O usuário deve poder realizar cálculos percentuais com qualquer um dos valores armazenados na calculadora. Os cálculos permitidos serão porcentagem, diferença percentual e porcentagem do total, vide a HP12-C. |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Comparar os resultados obtidos com a nossa implementação com os da HP-12c                                                                                                                                 |
| **Estimativa Inicial: 20 h**                                                                                                                                                                                     |


## US14 ##

| O usuário deve ser capaz de recuperar os valores de sua última análise ao religar a calculadora. Essa US consiste em implementar a persitência periódica dos registradores e sua recuperação no religamento da calculadora. |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Garantir integridade dos dados salvos                                                                                                                                                                                |
| **Estimativa Inicial: 20 h**                                                                                                                                                                                                |

## US15 ##

| O usuário deve ser capaz de realizar operações matemáticas mais elaboradas com qualquer um dos valores que estejam armazenados em registradores. As operações permitidas serão e<sup>x, x</sup>2, ln, y<sup>x, x</sup>1/2, parte fracionária e parte inteira. |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Comparar os resultados obtidos com a nossa implementação com os da HP-12c                                                                                                                                                                              |
| **Estimativa Inicial: 20 h**                                                                                                                                                                                                                                  |

## US16 ##

| Essa US consiste em reorganizar a interface da nossa calculadora de modo a conseguir uma maior independência do formato adotado na HP12-C. Durante nossos estudos percebemos que várias funções da HP12-C são bem complicadas de serem utilizadas, e aqui iremos facilitar o uso de tais funções, principalmentes para usuários que não estão habituados com o uso de calculadoras desse porte. |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TA 1 - Produção de um aplicativo com interface mais intuitiva do que a que está sendo usada.                                                                                                                                                                                                                                                                                                    |
| **Estimativa Inicial: 20 h**                                                                                                                                                                                                                                                                                                                                                                    |


[Artefatos](http://code.google.com/p/pyfinancial/wiki/artefatos)