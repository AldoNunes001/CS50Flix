# CS50Flix

![CS50Flix Logo](https://github.com/AldoNunes001/CS50Flix/blob/5673bc943e3362dabfe2f3e37610fa03e10c3f90/static/images/cs50flix.png)

CS50Flix é um clone da Netflix voltado para cursos de programação e ciência da computação e foi desenvolvido como projeto de conclusão do curso CS50. 
Foi feito com Django, Tailwind para estilizição e um pouco de JavaScript para comportamento dinâmico no front end.

## Demo

Veja o vídeo demo no YouTube: [https://youtu.be/F5jocse0xnI](https://youtu.be/F5jocse0xnI)

## Planejamento inicial

1. Homepage
2. Login / Criar conta (Usuário e Autenticação): 
    1. Email
    2. Nome de usuário
    3. Senha
    4. Vídeos assistidos
    5. Editar perfil
3. Cursos: 
    1. Miniatura
    2. Título
    3. Descrição
    4. Categoria
    5. Número de visualizações
    6. Data de criação
    7. Aulas:
        1. Vídeos (link do YouTube)
        2. Título
        3. Curso
4. Barra de pesquisa

## Estrutura do Projeto

O projeto é composto por 10 arquivos HTML localizados no diretório `templates`, 1 arquivo CSS no diretório `static/css` e todas as imagens estão no diretório `static/images`. Além disso, foram editados os arquivos de configurações, administração, URLs, visualizações, modelos, formulários e apps.

## Funcionalidades

- **Criar Conta e Login:** na homepage, temos a opção de fazer login ou criar uma conta. O site verifica se o e-mail inserido já está registrado, redirecionando para a página de login ou criação de conta, conforme necessário. Todos os formulários possuem validações para garantir a integridade dos dados.

- **Homepage dinâmica:** uma vez logado, a homepage exibe sugestões de cursos aleatórias, novos cursos adicionados à plataforma, os mais populares e os cursos já assistidos, no estilo carrossel.

- **Pesquisa de Cursos:** existe uma caixa de pesquisa para cursos.

- **Edição de Perfil e Logout:** na página de edição de perfil, o usuário pode alterar o nome, e-mail e senha. Além disso, há uma opção para logout.

- **Visualização de Cursos:** ao clicar em um curso, o usuário é redirecionado para a página do curso, onde estão todas as aulas. Clicando na aula, o player de vídeo (YouTube) é aberto para assistir à aula.

## Como rodar localmente

```bash
git clone https://github.com/username/CS50Flix.git
cd CS50Flix
pip install -r requirements.txt
python manage.py runserver
```

Isso é CS50!
