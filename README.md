# Pacote PjrCalculadora
Desafio 2 bootcamp - dio 

# Projeto: Pacote de uma calculadora em python
## Autora do Projeto: BarbosaXBarbosa
### Projeto: Descomplicando a criação de pacotes de em Python (DiO)
#### Tecnologia: Python
Data: 1/11/2022
-----------------------------------------
### Descrição
O pacote pjr_calculadora é usado para:

- Utilizar uma calculadora via CLI
- Fins de treino da lógica da programação utilizando python
- Fins de treino para pacotes em python
---------------------------------------------
## Passo a passo da configuração para hospedar um pacote em Python no ambiente de testes Test Pypi

- [x] Instalação das últimas versões de "setuptools" e "wheel"

```
pip install --upgrade setuptools wheel
```
- [x] Tenha certeza que o diretório no terminal seja o mesmo do arquivo "setup.py"

```
C:\User\user-name\your_project> py setup.py sdist bdist_wheel
```

- [x] Após completar a instalação, verifique se as pastas abaixo foram adicionadas ao projeto:
  - [x] build;
  - [x] dist;
  - [x] your_project.egg-info.

- [x] Basta subir os arquivos, usando o Twine, para o Test Pypi:

```
py -m twine upload --repository testpypi dist/*
```

- [x] Após rodar o comando acima no terminal, será pedido para inserir o usuário e senha. Feito isso, o projeto estará hospedado no Test Pypi.hospedá-lo no Pypi diretamente.

### O objetivo este projeto foi realizar um simples teste com o projeto da calculadora usando a hospedagem no Test Pypi em um projeto do bootcamp Unimed BH da DiO.

----------------------------------------------------
## Instalação local, após hospedagem no Test Pypi

- [x] Instalação de dependências
```
pip install -r requirements.txt
```

- [x] Instalção do Pacote

Use o gerenciador de pacotes ```pip install -i https://test.pypi.org/simple/ package-image-processing-vitor-souza ```para instalar your_project-test

```bash
pip install image-processing-test
```
-------------------------------------------------

## Desenvolvedor do projeto

[<br><sub>João Victor Barbosa</sub> ](https://github.com/barbosaxbarbosa)


[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://github.com/barbosaxbarbosa)

## License
[MIT](https://choosealicense.com/licenses/mit/)