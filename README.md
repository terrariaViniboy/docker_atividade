# Virtualização na Prática com Docker 🐳

![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=GREEN&style=for-the-badge)
![Badge Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Badge Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Badge Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

> Atividade prática desenvolvida para a disciplina de **Fundamentos de Sistemas de Informação** do curso de Sistemas de Informação do IFTO - Campus Paraíso do Tocantins.

---

## 📝 Sobre o Projeto

Este projeto tem como objetivo demonstrar a implantação de uma aplicação web simples utilizando a tecnologia de virtualização de containers **Docker**.

O uso do Docker permitiu empacotar a aplicação junto com todas as suas dependências (Python e Framework Flask), garantindo a portabilidade, a padronização do ambiente e a facilidade de execução em diferentes sistemas operacionais.

### 🎯 Funcionalidade
A aplicação consiste em uma página web simples que, ao ser acessada, retorna a mensagem:
> **"Aplicação rodando em Docker"**

---

## 📂 Estrutura do Projeto

A organização dos arquivos segue a estrutura abaixo:

```text
docker-flask-app/
│
├── app.py             # Código fonte principal da aplicação (Rota e lógica do Flask)
├── Dockerfile         # Arquivo de configuração para construção da imagem Docker
├── requirements.txt   # Lista de dependências do projeto (Bibliotecas Python)
└── README.md          # Documentação do projeto
```
---

## 🚀 Tecnologias Utilizadas

* **[Python 3.10](https://www.python.org/):** Linguagem de programação utilizada.
* **[Flask](https://flask.palletsprojects.com/):** Micro-framework web para Python.
* **[Docker](https://www.docker.com/):** Plataforma para criação e gerenciamento de containers.

---

## ⚙️ Pré-requisitos

Antes de começar, você precisa ter instalado em sua máquina:
* [Docker Engine](https://docs.docker.com/engine/install/)

---

## 🛠️ Como Executar o Projeto

Siga os passos abaixo para construir e rodar a aplicação via terminal:

### 1. Construção da Imagem (Build)

Navegue até a pasta raiz do projeto e execute o comando para criar a imagem Docker com o nome `flask-docker-app`:

```bash
docker build -t flask-docker-app .

```
Nota: O Dockerfile utiliza a imagem base python:3.10-slim e configura o diretório de trabalho /app.

```bash
docker run -d -p 8080:5000 --name flask-container flask-docker-app
```

---

## 👨‍💻 Autores

* **Gustavo Romão** - [Perfil no GitHub](https://github.com/seu-usuario)
* **Vinicio Moreira** - [Perfil no GitHub](https://github.com/seu-usuario)

**Instituição:** Instituto Federal de Educação, Ciência e Tecnologia do Tocantins (IFTO) - Campus Paraíso do Tocantins  
**Disciplina:** Fundamentos de Sistemas de Informação  
**Professor:** Marcos Raimundo Mendes Ramos

---
📄 Licença
Este projeto é de cunho educacional.
