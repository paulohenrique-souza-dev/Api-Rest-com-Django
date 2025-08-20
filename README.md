# Passo a Passo Api Rest com Django Rest Framework

1:digite no terminal do vs code,ou outro editor de preferência: git clone https://github.com/paulohenrique-souza-dev/Api-Rest-com-Django.git

2:Após ter os arquivos na máquina,basta criar a venv.

                    python -m venv venv  
                    venv\Scripts\activate

3: Com a virtualenv criada, instale as dependências, digite no terminal:pip install -r requirements.txt


4:Caso o push do github não foi,ou você está iniciando manual os apps, digite no terminal, dentro da pasta do seu projeto e com a virtualenv ativada, rode os comandos:

                    django-admin startproject core .    /aqui fica as configurações do projeto.
                                    
                    python manage.py startapp api  /criando apps  
                   
                                    

5: Após criar seu projeto e apps, é hora de criar o banco de dados,em seu sgbd de preferência crie as tabelas relacionais,vou deixar todos os códigos de criação aqui no repositório,lembre de configurar o settings.

6: Após ter as tabelas tudo certo no Sql,é hora de importar as tabelas do bd para o models do django,ou seja para subir a api.Use o código a seguir : python manage.py inspectdb > api/models.py
Isso faz com que todas tabelas que estão no bd configurado em settings,serem importadas para models de api/models.


7: Para acessar o painel de admin, crie um superusuário com o código a seguir,é opcional,porem para uma boa gestão e boas práticas é indicado.

                    python manage.py createsuperuser


9: Depois dos arquivos estarem de acordo com o desse passo a passo basta digitar : python manage.py runserver e seu sistema já deve rodar,se não for verifique a pasta que está manage.py.  

Obrigado pela sua atenção até aqui, até mais!








