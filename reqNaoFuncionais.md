# Requisitos Não-funcionais #

### Interface ###

Para a calculadora a ser desenvolvida no projeto, deseja-se que sua interface seja similar a da calculadora HP12-C que estamos usando como base. Deseja-se não necessariamente que a interface seja uma cópia da calculadora em questão, mas que a disposição de botões e o agrupamento de funções nos mesmos siga o modelo da HP12-C.

A entrada de dados será realizada através do toque na tela nas regiões referentes a cada botão em questão.

![http://upload.wikimedia.org/wikipedia/commons/9/94/Hp12c.jpg](http://upload.wikimedia.org/wikipedia/commons/9/94/Hp12c.jpg)

### Facilidade de uso necessária ###

O público alvo do produto serão os empregados de bancos, economistas e administradores que constantemente estão envolvidos com o uso de funções financeiras.

Tomando por base a HP12-C, desejamos que o nível de dificuldade encontrado para uso de nossa calculadora seja o mesmo encontrada na calculadora real. Ou seja, faz-se necessário um certo treinamento inicial a respeito do que é cada uma das funções financeiras, ou mesmo ainda na parte aritmética é necessário que o usuário seja treinado sobre como usar as várias funções contidas em cada botão, bem como ser informado a respeito da notação utilizada nas operações (http://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_Polonesa_Inversa).

### Volume de utilização ###

A calculadora será mono-usuário, porém devendo ser robusta o suficiente para ser utilizada durante um longo intervalo de tempo ininterruptamente sem apresentar problemas.

### Hardware e software alvo para o produto ###

A calculadora deverá funcionar no Internet Tablet N800 da nokia (http://www.nseries.com/products/n800/#l=products,n800), no sistema operacional Maemo Diablo (4.1.x) (http://maemo.org/maemo_release_documentation/maemo4.1.x/Maemo_Diablo_Reference_Manual_for_maemo_4.1.pdf), com Python, PyQt e Qt4 (falta especificar as versões).

### Qualidade ###

Com relação a precisão, deseja-se que os valores calculados em nossa calculadora não devam diferir em mais de 0.001 unidades dos valores calculados na HP12-C original.

### Tolerância a falha ###

A calculadora deve fazer logs dos valores armazenados em seus registradores correspondentes aos últimos valores utilizados pelo usuário, para em eventual pane poder recuperar os mesmos ao ser novamente acionada.

Entradas equivocadas do usuário deverão apresentar mensagens de erros que devem ser mais intuitivas do que as apresentadas pela calculadora original como "Erro 6".

Veja a [tabela de erros](tabErros.md)

### Desempenho ###

O tempo de resposta dos resultados não deve ultrapassar o tempo que a calculadora HP12-C leva para executar as mesmas operações (considerando que só o programa da calculadora esteja em execução).

### Segurança ###

Os arquivos que conterão os valores dos registradores recém utilizados pelo usuário deverão ficar protegidos de alteração externa.

### Compatibilidade ###

É desejável que a aplicação possa ser portada para versões mais novas do dispositivo alvo, como o N810, bem como para novas versões do Maemo.

### Internacionalização ###

A calculadora deve ser desenvolvida para tornar possível a internacionalização.

### Documentação ###

As classes do sistema devem ser todas documentadas em inglês

### Uso de padrões ###

Iremos utilizar o padrão MVC [aqui](http://www.dsc.ufcg.edu.br/~jacques/cursos/map/html/arqu/mvc/mvc.htm), bem como qualquer outro padrão que seja visto necessário durante o desenvolvimento.

### Packaging ###

A distribuição do aplicativo será realizada através de um arquivo .deb que servirá como instalador para o mesmo.

### Riscos aceitáveis ###

Embora haja a suspeita de que o Framework QT será bastante utilizado no desenvolvimento
de interfaces gráficas para dispositivos móveis, podemos considerar que no momento estaremos enfrentando um risco ao fazer uso do mesmo. Isso se dá pelo fato de que o processo de portar o QT para os dispositivos está ocorrendo no momento, mas já temos versões do mesmo que podem ser utilizadas nos dispositivos.

### Padrão de Codificação ###

#### IDENTAÇÃO ####

> 4 Espaços (aqui pode-se configurar o TAB do editor para o número de espaços propostos)

#### LINHAS EM BRANCO ####

  1. 2 Linhas em branco antes da declaração de uma função ou classe
  1. 1 Linha em branco para separar os métodos de uma classe
  1. Linhas em branco extras podem ser usados para separa trechos lógicos, grupos de funções, declarações

#### ENCODING ####

> Utilizar o UTF-8 como codificação do arquivo

#### IMPORTAÇÃO DE MÓDULOS ####

> Sempre realizar todas as importações no início do arquivo de modo que cada módulo deverá ser importado em uma linha, a não ser que se esteja especificando submódulos de um determeniado módulo. Ex:

> Certo: import os                 			Errado: import sys, os

> import sys

> from subprocess import Popen, PIPE

#### ESPAÇOS EM BRANCO (FUNÇÕES E EXPRESSÕES) ####

> Evitar os espaços em branco nas seguintes situações:

  1. Dentro de (parênteses) [colchetes](colchetes.md) e {chaves}, a não ser em casos com muita agregação dos mesmos
    1. Certo: spam(ham[1](1.md), {eggs: 2})                 Errado:  spam( ham[1 ](.md), { eggs: 2 } )
  1. Antes de uma “,” virgula, “;” ponto e virgula e “:” dois pontos
    1. Certo: if x == 4: print x, y; x, y = y, x      Errado:  if x == 4 : print x , y ; x , y = y , x
  1. Antes da abertura de parênteses em chamada de funções, definições e listas
    1. Certo: spam(1)                                 Errado:  spam (1)
  1. Antes da abertura de colchetes de indices e { chaves } de dicionários
    1. Certo: dict['key'] = list[index ](.md)               Errado:  dict ['key'] = list [index](index.md)
  1. Mais de um espaço em atribuições de valores
    1. Certo: x = 1                                   Errado:  x       = 1
  1. Não utilizar espaços com em chamadas de métodos com passagem de chaves nos parâmetros e também nos dicionários
    1. Certo: def complex(real, imag=0.0):            Errado: def complex(real, imag = 0.0):
  1. Sempre utilizar espaço simples ao se trabalhar com operadores (=, +=, -=, +, -, **, <=, ==, !=, and, not, ……… )**


#### COMENTÁRIOS ####

> Devem ser identados ao mesmo nível do código no qual se faz pertinente e sempre será utilizado comentários de blocos iniciados por “”" e finalizados por “”" (também chamados de docstring). Ao se utilizar uma descrição breve abrir e fechar a documentação na mesma linha.
> Serão comentados todas as funções que sejam públicas (exceto os get e set)

#### CONVENÇÕES DE NOME ####

> Nomes a evitar:

  1. Os seguintes caracteres: l (ele minuscúlo), O (o maiúsculo), I (i maiúsculo), ou qualquer outra letra como nomes de variáveis

> Pacotes e módulos:

  1. Pacotes e Módulos devem ser curtos, com a primeira palavra iniciando em minúsculo e as seguintes iniciando em maiúsculo de forma similar a nomenclatura de classes abaixo

> Classes

  1. UtilizarCapitalizarNomeSemExceção

> Variáveis Global

  1. UTILIZAR\_TODAS\_AS\_LETRAS\_EM\_MAIÚSCULA\_E\_COM\_UNDERLINE

> Nomes de funções e métodos

  1. Iniciar em minúscula para diferir das classes contudo utilizar Maiúsculas para formar mais palavras sem underline
  1. Métodos privados utilizam dois underlines  no inicio do método

> Variáveis, argumentos de métodos e variáveis de classes

  1. Nomenclatura similar a de métodos
  1. Atributos privados utilizam dois underlines  no inicio do nome






[Artefatos](http://code.google.com/p/pyfinancial/wiki/artefatos)