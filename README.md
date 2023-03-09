
# Exercício Toscrap - Raspagem de Dados
Baseando-se nesta página http://books.toscrape.com/catalogue/the-grand-design_405/index.html, foi realizado a raspagem dos seguintes dados: título, preço, descrição e capa.

O retorno esperado é:
```bash
The Grand Design,13.76,THE FIRST MAJOR WORK IN NEARLY A DECADE...,http://books.toscrape.com/catalogue/../../media/cache/9b/69/9b696c2064d6ee387774b6121bb4be91.jpg
```
 





## Instalação

Para rodar o exercício é necessário criar um ambiente virtual Python: 

1 - Cria o ambiente virtual
```bash
$ python3 -m venv .venv
```
2 - Ativa o ambiente virtual
```bash
$ source .venv/bin/activate
```
3 - E instala as dependências no ambiente virtual
```bash
$ python3 -m pip install -r dev-requirements.txt
```



    
## Teste
Para executar o teste basta rodar o seguinte comando:
```bash
$ python3 -m pytest
```
