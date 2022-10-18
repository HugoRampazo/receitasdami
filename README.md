# receitasdami
Esse projeto foi desenvolvido para minha digníssima esposa publicar suas receitas favoritas.

# Para baixar/clonar projeto:
1º Abra o CMD.

2º Digite o seguinte comando no CMD para acessar a área de trabalho:

    cd desktop


3º Clone o projeto no seu computador, colando o seguinte comando no CMD:

    git clone https://github.com/HugoRampazo/receitasdami.git


# Para criar o ambiente virtual e instalar os pacotes necessários:
1º Acesse a pasta do projeto no CMD com o seguinte comando:

    cd receitasdami


2º Crie um ambiente virtual seguindo os seguintes comandos no CMD (deve ser inserido apenas um comando de cada vez):

    pip install --upgrade virtualenv

    pip install --upgrade virtualenvwrapper-win

    pip install --upgrade pip

    mkvirtualenv receitasdamivenv


3º Agora vamos acessar nosso ambiente virtual com o seguinte comando no CMD:

    workon receitasdamivenv


4º Nessa etapa vamos instalar os pacotes utilizados no desenvolvimento do projeto em nosso ambiente virtual, no CMD:

    pip install -r requirements.txt


# Para criar um super usuário:

    python manage.py createsuperuser

(Informe um usuário, email e senha de sua escolha)
   
   
# Para rodar o projeto:
1º Ainda no CMD, vamos inserir o seguinte comando:

    python manage.py runserver
    
    
2º Com o CMD aberto, abra seu navegador e acesse:

    http://localhost:8000/
    

3º Tudo pronto! Entre com usuário e senha que você criou para ter acesso à áreas restritas do site.
