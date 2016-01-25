# Validação do estudo


# Configuração Eclipse com Pydev, Subclipse e Esbox #

Utilizamos o Eclipse Europa for C/C++ Developers para linux.
http://www.eclipse.org/downloads/packages/release/europa/winter

Instalamos os plugins Pydev, Subclipse e Esbox nessa ordem.
http://pydev.sourceforge.net/download.html
http://subclipse.tigris.org/
http://esbox.garage.maemo.org/



# Instalação e configuração do SDK, Scratchbox e Xephyr #

Para instalar as três ferramentas utilizou-se o seguinte tutorial: http://tablets-dev.nokia.com/4.1/INSTALL.txt

Para instalar o python, o qt4 e o pyqt4 no scrathbox utilizou-se os seguintes passos (as operações abaixo devem ser executadas como root no Scratchbox):

  * De dentro do Scratchbox, adicionar as linhas abaixo no arquivo /etc/apt/sources.list

```
deb http://repository.maemo.org/extras/ diablo free non-free
deb-src http://repository.maemo.org/extras/ diablo free
deb http://repository.maemo.org/extras-devel/ diablo free non-free
deb-src http://repository.maemo.org/extras-devel/ diablo free
```

  * Execute `apt-get update`

  * Execute `apt-get install python2.5-qt4-core python2.5-qt4-gui`

  * Caso ocorra problemas com o qemu (vide https://garage.maemo.org/pipermail/pymaemo-developers/2008-August/000480.html) na hora de rodar aplicações com PyQT, especialmente devido ao python 2.5, deve-se (baseado em http://setanta.wordpress.com/2007/11/20/qemu-arm-eabi-no-scratchbox/):
    1. sudo apt-get install gcc-3.4
    1. svn co https://qemu-arm-eabi.svn.sourceforge.net/svnroot/qemu-arm-eabi/trunk qemu-arm-eabi
    1. cd qemu-arm-eabi
    1. Seguir as instruções do README

# Instalação do Ambiente da Biblioteca Gráfica no Linux #

  1. Instalação do QT4 e QT4.4 via apt-get seguindo o tutorial 1 presente em http://flaviofabricio.blogspot.com/2008/08/tutorial-programando-para-qt-usando.html
  1. Instalação do PyQT4 através de apt-get com os seguintes módulos: python-qt4, python-qt4-dbg, python-qt4-common, python-qt4-dev, pyqt4-dev-tools


Para conseguir rodar projetos python atrvés do Esbox, instale o qemu-arm no scratchbox:
http://qemu-arm-eabi.wiki.sourceforge.net/

# Instalação do Latex e Kile e configuração do template #

  1. Para instalação do Latex e Kile seguimos o tutorial presente em http://www.ginux.ufla.br/node/18
  1. O template utilizado para a produção da monografia é o template que a SBC indica para construção de capítulos de livros (com algumas modificações). Esse template pode ser encontrado em http://www.sbc.org.br/index.php?language=1&content=downloads&id=287


# Configuração do ambiente no N800 #

Para instalar o OS Diablo no N800 foi feito download da imagem do OS no link abaixo:
http://tablets-dev.nokia.com/nokia_N800.php

Após isso, utilizou-se o seguinte tutorial para fazer o flash no equipamento:
http://fosswire.com/2007/12/30/n800-users-flash-to-os2008/

Antes de começar a instalar os ambiente no N800 foi necessário ativar os repositórios de desenvolvimento. Para isso, faça no N800:
  1. Start "Settings > Application Manager".
  1. Go to "Tools > Application catalogue", click "New".
  1. Enter "matrix" into the "Web Address" field and click "Cancel".
  1. Choosing the red pill will activate the red pill mode, obviously, and choosing the blue one will deactivate it.
Agora é possível instalar o openssh através do Application Manager. Habilite o catálogo Extras no Application catalogue e instale o openssh através do Application Manager.

Para instalar o ambiente de desenvolvimento de python no N800 é só acessar o N800 pelo ssh, se tornar root e rodar o comando "apt-get install maemo-python-device-env".

Após instalado o python, foi instalado o Qt no N800. Primeiro temos que ativar o repositório de desenvolvimento.

  * Faça ssh como root para o N800 e adicione as linhas abaixo no arquivo /etc/apt/sources.list

```
deb http://repository.maemo.org/extras/ diablo free non-free
deb-src http://repository.maemo.org/extras/ diablo free
deb http://repository.maemo.org/extras-devel/ diablo free non-free
deb-src http://repository.maemo.org/extras-devel/ diablo free
```

  * Execute `apt-get update`

Outra alternativa para ativar o repositório é clicar através do browser do N800 no link indicado na página do projeto (http://qt4.garage.maemo.org/) onde diz "How can I install Qt4 applications on my Maemo OS2008 Device?"

Após isso, logado como root no N800 instale os pacotes que você quer. Exemplo: `apt-get install libqt4-core`

Para instalar o PyQt, usamos o seguinte tutorial: http://pyqt.garage.maemo.org/installation.html


# Configuração USB N800 no Desktop #

  * Links de referência: http://wiki.maemo.org/USB_networking e http://maemo.org/development/documentation/pc_connectivity/
  * Ensure that the usbnet module is available to your kernel (try modprobe usbnet, then lsmod to check).
  * Edit the network interface configuration in the host's "/etc/network/interfaces" file appending:
> > mapping hotplug


> script grep
> map usb0

> auto usb0

> iface usb0 inet static

> address 192.168.2.14

> netmask 255.255.255.0

> network 192.168.2.0

> broadcast 192.168.2.255

> up iptables -t nat -A POSTROUTING -o eth0 -s 192.168.2.15 -j MASQUERADE

> up echo 1 > /proc/sys/net/ipv4/ip\_forward

> down iptables -t nat -D POSTROUTING -o eth0 -s 192.168.2.15 -j MASQUERADE

> down echo 0 > /proc/sys/net/ipv4/ip\_forward


  * On the Tablet:
    1. Run Settings > Control Panel > USB networking
    1. Click “Setup USB networking”
      1. ou may see a message saying “Unable to connect via USB. Memory card in use: Removable memory card”.
      1. If so:
        1. Unmount the drives on the host.
        1. Unplug the cable.
        1. Click “Setup USB networking” again.
    1. Plug in the USB cable.
  * On Desktop
    1. sudo ifdown usb0
    1. sudo ifup usb0
    1. Test the connection: "ping 192.168.2.15"
    1. ssh root@192.168.2.15
    1. scp arquivo root@192.168.2.15:/home/user/

# Estudo da Arquitetura Maemo #

Um dos membros do grupo estudou e apresentou para o restante o material dos cursos de Raul do Embedded. Foram cobertos os tópicos Scrathbox, SDK, Maemo, Esbox e Python para Maemo.

[maemo\_training\_pt](http://pyfinancial.googlecode.com/files/maemo_training_pt.pdf)
[maemo\_python](http://pyfinancial.googlecode.com/files/maemo_python.pdf)
[introducao\_python](http://pyfinancial.googlecode.com/files/introducao_python.pdf)


# Estudo de Python #

Para estudar python procuramos usar um tutorial para que já é programador. Usamos esse material que cobre de forma direta os principais conceitos da linguagem.
http://en.wikibooks.org/wiki/Python_Programming

Para estudar as diferenças de python para maemo, usamos o material oficial do projeto.
http://pymaemo.garage.maemo.org/documentation/pymaemo_tutorial/python_maemo_howto.html


# Estudo de PyUnit e PyEasyAccept #


## PyUnit ##

  1. Para estudo do PyUnit seguimos o tutorial http://pyunit.sourceforge.net/pyunit.html, criando casos de testes similares aos do tutorial.
  1. Preparou-se uma e realizou-se uma [apresentação](http://pyfinancial.googlecode.com/files/PyUnit.ppt) com os principais comandos e principal estruturação de testes usando a ferramenta.

## PyEasyAccept ##

  1. Para estudo do PyEasyAccept seguimos o tutorial http://pyeasyaccept.sourceforge.net/tutorial.html, criando casos de testes similares aos do tutorial.
  1. Preparou-se uma e realizou-se uma [apresentação](http://pyfinancial.googlecode.com/files/PyEasyAccept.ppt) com os principais comandos e principal estruturação de testes usando a ferramenta.



# Estudo de Qt, PyQt e QtDesigner #

## QT4.4 ##

  1. Leitura do overview da ferramenta em http://trolltech.com/products/appdev
  1. Leitura das principais seções relevantes a nosso trabalho do white-paper http://trolltech.com/products/files/pdf/qt-4.4-whitepaper: 2, 3, 4, 6, 7, 10, 12, 13, 15, 18, 19

## PyQt4 ##

  1. Leitura do tutorial http://zetcode.com/tutorials/pyqt4/ com desenvolvimento dos exemplos propostos
  1. Busca pela API da tecnologia: http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html
  1. Foram realizados testes de conversão de arquivos .ui gerados pelo QtDesigner para arquivos PyQt através do comando `pyuic -o <destino> <.ui origem>` seguindo a abordagem adotada em http://www.diotavelli.net/PyQtWiki/Creating_GUI_Applications_with_PyQt_and_Qt_Designer


## QtDesigner ##

  1. Leitura do manual da versão 4.4 (http://doc.trolltech.com/4.4/designer-manual.html) com desenvolvimento dos exemplos propostos. Em especial o tópico Using Qt Designer já que os demais retratam o uso de Qt juntamente com C++ que não é alvo de trabalho da equipe.
  1. Desenvolvimento de exemplos simples usando o conjunto de widgets existentes como toolbox, menus, bars, botões, etc.


# Estudo do .deb #



# Estudo do conceitos de matemática financeira #

  1. Leitura da [apostila introdutória](http://pyfinancial.googlegroups.com/web/5.+Fun%C3%A7Ses+B%C3%A1sicas+da+HP12C.doc?gda=I1lo21sAAAD3U4e8vu9PPSKlvlS0r9PSKm5b4a6wQOPTUgL34dz3aI_3kmXoikH4O8_3Soo-g9wKtosA8OcA_CeSZUeBvBGAVogPkaX-lTOduiVsLFTh7wZF2vdCvKU-TDZpFtcP-AU)
  1. Leitura dos primeiros pontos necessários do livro [Matemática Financeira](http://pyfinancial.googlegroups.com/web/MF-HP12C-JCS.pdf?gda=xWk--0IAAAD3U4e8vu9PPSKlvlS0r9PS8xYBDzsVBh4mv8WlrGok85iMwSep2Ry9c2aiT4Cuxa1V4u3aa4iAIyYQIqbG9naPgh6o8ccLBvP6Chud5KMzIQ)


# Gerar calculadora de exemplo #

Para gerar a calculadora de exemplo utilizou-se a [rpCalc](http://rpcalc.bellz.org/) como referência.

# Gerar .deb #

Primeiramente é necessário gerar um arquivo setup.py que vai gerar automaticamente o .deb. Para isso seguimos o seguinte tutorial: http://home.cfl.rr.com/genecash/nokia/making_packages.html

## Geração do pacote de instalação ##

  1. Vá na raiz do projeto e apague as pasta build e dist se tiver
  1. python setup.py bdist\_debian
  1. As pastas dist/ e build/ devem ter sido criadas
  1. Entre na pasta dist/ e copie o arquivo pyfinancialcalculator_{ID de versão}_all.deb para o N800 via scp
  1. Instale a aplicação com: dpkg -i pyfinancialcalculator_{ID de versão}_all.deb




[Artefatos](http://code.google.com/p/pyfinancial/wiki/artefatos)