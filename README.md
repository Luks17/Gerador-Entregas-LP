
# Gerador de Entregas de Linguagem de Programação

Para usar, você precisa ter instalado Python e Git. 
Para usuários de Windows, recomendo utilizar o Git Bash.

Após instalar ambos, rode os seguintes comandos para instalar este programa:

```bash
$ git clone https://github.com/Luks17/Gerador-Entregas-LP.git
$ cd ./Gerador-Entregas-LP
$ python -m venv env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

Por fim, para usar ele é só colocar a pasta src com seu código, a pasta prints com seus prints, sua assinatura e arquivo .sql (se houver) na pasta input, e rodar index.py:

```bash
$ ./env/bin/python index.py
```

Exemplos foram disponibilizados na pasta input deste repositório para testar.
