# Mensagens de erro presentes na bilbioteca financeira #

|**Mensagem** | **Descrição** | **Correspondente na HP12c** |
|:------------|:--------------|:----------------------------|
|"Invalid scenario: Impossible operations." |  Valores declarados tornam impossível a execução da operação, seja por tipos incompatíveis, divisão por zero, etc. | Error 0                     |
|"Invalid scenario: Should select BEG or END." | Seletores BEG ou END não selecionados | -                           |
|"Invalid scenario: i value equal or less than -100%." | Valor de i menor que -100| Error 5                     |
| "Invalid scenario: Infinite n." | Valor de n grande o suficiente pra ser considerado infinito | -                           |
| "Invalid scenario: Error(s) in the values of operators capitalization (n, i, PV, FV or PMT)." | Sinaliza erro na operação de capitalização composta, como erros no uso de sinais - e + nos valores monetários (n, i, PV, FV ou PMT) ou algum destes com valor 0 quando isso não é permitido. | Error 5                     |
|"Some values for calculating amortization have not been provided." |Alguns dos valores necessários para o cálculo da amortização não foram fornecidos. | Error 7                     |
|"Error in some operands to calculate the percent difference." | Valores apresentados para o cálculo da variação de porcentagem são inválidos | Error 0                     |
|"Error in some operands to calculate the percent total." | Valores apresentados para o cálculo da porcentagem total são inválidos | Error 0                     |



# Mensagens de erro presentes na calculadora #

|**Mensagem** | **Descrição** | **Correspondente na HP12c** |
|:------------|:--------------|:----------------------------|
|"All cash flow registers already fulfilled!" | Impossível a inclusão de novos valores, os registradores estão todos preenchidos | -                           |
|"There are only "  + Num + " cash flows occurences" | Existem poucos fluxos de caixa definidos para o cálculo | -                           |
|"Nj must be an integer value between 1 and 99" | Valor estabelecido para Nj fora dos limites | Error 6                     |
|"Invalid cash flow index!" | Número do fluxo solicitado em desacordo com a quantidade de registradores | -                           |
|"Invalid amortization plan!" | Índice escolhido não corresponde a nenhum dos planos de amortização possíveis | -                           |
|"Invalid number pushed: "+ NUM | Número digitado considerado inválido | -                           |

[Artefatos](artefatos.md)