# API de Gerenciamento Escolar - Flask MVC

Projeto de API RESTful completa, desenvolvida em **Flask** e estruturada no padrão **MVC (Model-View-Controller)** para o gerenciamento de:

- Professores  
- Turmas  
- Alunos  

A documentação da API é gerada automaticamente com **Swagger**, disponível após rodar a aplicação.

---

## 📚 Funcionalidades

A API permite operações CRUD (Criar, Ler, Atualizar e Deletar) para as entidades:

- Professores  
- Turmas  
- Alunos  

---

## 🚀 Rodando a aplicação

### Pré-requisitos

- Docker instalado na sua máquina

### Passos

#### 1. Construir a imagem Docker

```bash
docker build -t minha-api-flask .

#### 1. Rodar o container

```bash
docker run -d -p 5000:5000 --name api minha-api-flask

#### 2. Acessar a aplicação

Abra no navegador ou use o Postman o endereço:

http://localhost:5000

#### 3. Documentação da API (Swagger)

Acesse a documentação interativa no link:

http://localhost:5000/apidocs





## 📁 Estrutura do projeto

- **Controllers/** - Controladores que gerenciam a lógica das requisições  
- **Instance/** - Configuração da instância do banco de dados  
- **Models/** - Modelos das tabelas para banco de dados (Aluno, Professor e Turma)  
- **Routes/** - Rotas de acesso com métodos GET, POST, PUT, DELETE  
- **app.py** - Inicialização da aplicação Flask e configuração geral  
- **Dockerfile** - Configuração da imagem Docker para containerização  
- **run.py** - Arquivo principal para rodar a aplicação  

---

## 👥 Integrantes do Grupo

| Nome                        | RA       |
|-----------------------------|----------|
| Ronaldo Filgueira Cavalcante | 2403661  |
| Luis Gabriel                 | 2402947  |

| Maycon Pereira               | 2402929  |
