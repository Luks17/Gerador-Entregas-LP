
# Gerador de Entregas de Linguagem de Programação

Para usar, você precisa ter instalado Python e Git. 
Para usuários de Windows, recomendo utilizar o [GitForWindows](https://gitforwindows.org/).

## Instalação do programa e do ambiente

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

## Utilização

Primeiro de tudo, ative o ambiente igual como foi mostrado anteriormente.

Após isso, para usar este programa é só colocar a pasta src com seu código, a pasta prints com seus prints, sua assinatura e arquivo .sql (se houver) na pasta input, e rodar index.py:

```bash
$ python index.py
```

Exemplos foram disponibilizados na pasta input deste repositório para testar.
