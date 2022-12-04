
# Gerador de Entregas de Linguagem de Programação

Para usar, você precisa ter instalado Python e Git. 
Para usuários de Windows, se estará assumindo que se está utilizando o [GitForWindows](https://gitforwindows.org/).

## Instalação automática usando run.sh

Abra o terminal (ou use GitForWindows se estiver usando Windows) e coloque os seguintes comandos:

```bash
$ git clone https://github.com/Luks17/Gerador-Entregas-LP.git && cd ./Gerador-Entregas-LP
$ chmod +x ./run.sh && ./run.sh
```

Se tudo deu certo, o programa agora está instalado e irá rodar automáticamente após a instalação. 

Para rodar ele daqui adiante, basta abrir o terminal (ou GitForWindows) no diretório do programa e escrever:

```bash
$ ./run.sh
```

## Instalação Manual

### Instalação do programa e do ambiente

Rode os seguintes comandos para instalar este programa:

```bash
$ git clone https://github.com/Luks17/Gerador-Entregas-LP.git
$ cd ./Gerador-Entregas-LP
$ python -m venv env
```

#### Ativação do ambiente

Para ativar o ambiente instalado em sistemas baseados em Unix use:
```bash
$ source ./env/bin/activate
```

Para ativar o ambiente instalado em Windows utilize:
```bash
$ source ./env/Scripts/activate
```

#### Instalação das dependencias

Para instalar as dependencias, ative o ambiente e rode o seguinte comando:
```bash
$ pip install -r requirements.txt
```

### Utilização

Primeiro de tudo, ative o ambiente igual como foi mostrado anteriormente.

Após isso, para usar este programa é só colocar a pasta src com seu código, a pasta prints com seus prints, sua assinatura e arquivo .sql (se houver) na pasta input, e rodar run.sh:

```bash
$ ./run.sh
```

Exemplos foram disponibilizados na pasta input deste repositório para testar.
