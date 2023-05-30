# matricula
PI-1 da Univesp dos cursos do Eixo de Computação/2021:
"WebSite Aplicação para cadastramento de pré-matrícula de alunos da rede pública de ensino. Visa auxiliar e agilizar as matrículas e
planejamento dos cursos da grade do ensino fundamental e EJA no município de Guarulhos"

Requisitos para rodar a aplicação com Framework Flask e Banco de Dados SqLite :

1- instalar o Python no seu computador - não esquecer de marcar o box "Add Python to Path" na instalação (para poder digitar comandos no terminal do Windows);

2- instalar o Pycharm;

... após instalados os softwares acima seguir os passos abaixo:

Criar ambiente de programação:
(isso faz com que sua aplicação rode apenas no repositório e evita danificar sua instalação raiz do Python)

Para sistema operacional Windows:

3- abre o terminal;
comando -> cmd.exe

4- crie um diretório chamado "matricula" num local desejado;
comando -> mkdir matricula

5- entre no diretorio;
comando -> cd matricula

6 - crie o ambiente de programação;
comando -> virtualenv env

7- ativa o ambiente de programação;
comando -> env\Scripts\activate

8- instalar bibliotecas no ambiente de programação:

(instala o framework flask)
comando -> pip3 install flask

(instala o sqlalchemy para operar com o banco de dados)
comando -> pip3 install sqlalchemy

(instala o flask-sqlalchemy para manipular objetos no banco de dados)
comando -> pip3 install flask-sqlalchemy

9- extraia os arquivos zipados que encontram-se na arquivo "matricula.zip" para dentro da pasta repositório "matricula" criada acima no item "4";
 
10- abre o repositório "matricula" na IDE PyCharm;

11- no terminal, exporte as variáveis de ambiente;
comando -> set FLASK_APP=app
comando -> set FLASK_ENV=development

12- roda o servidor Web no seu computador;
comando -> flask run --debug

13- irá aparecer o endereço do servidor que vc deverá copiar e colar no seu navegador web para visualizar o site e as aplicações desenvolvidas;
endereço: http://127.0.0.1:5000

Pronto, agora vc já pode alterar as aplicações do site e testá-las no seu computador.

Caso precise parar o servidor "Flask", utilize o comando -> crt+c no teclado.

Para desativar o ambiente de programação utilize o comando -> env\Scripts\deactivate
