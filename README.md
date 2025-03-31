# Dockerizando uma Aplicação Flask: Conversor de Distância

Este projeto tem como principal objetivo demonstrar **como empacotar uma aplicação Flask simples usando Docker** e publicá-la no Docker Hub, tornando sua execução e distribuição extremamente prática e portátil.

👉 **Imagem no Docker Hub**:  
https://hub.docker.com/r/eduardolentz/docker-conversao-distancia

---

## 📊 Diagrama do Fluxo Docker

![Fluxo Docker](https://github.com/eduardolentz/docker-conversao-distancia/raw/main/imagens/diagrama.png)

---

## 💡 Funcionalidades da Aplicação

- Conversão entre:
  - Metros ⇄ Quilômetros
  - Metros ⇄ Milhas
  - Metros ⇄ Pés
- Interface web simples com Bootstrap
- Exibição do nome e IP do servidor

---

## 🐳 Comandos Docker utilizados

### 🔧 1. Build da imagem Docker

```bash
docker build -t eduardolentz/docker-conversao-distancia .
```

### 🧪 2. Testar localmente

```bash
docker run -p 5000:5000 eduardolentz/docker-conversao-distancia
```

Acesse no navegador: http://localhost:5000

### 🧪 Imagem de teste

![Teste da aplicação](https://github.com/eduardolentz/docker-conversao-distancia/raw/main/imagens/teste.png)


### 🚀 3. Enviar para o Docker Hub

```bash
docker push eduardolentz/docker-conversao-distancia
```

---

## 🛑 Parar o container

Pressione `Ctrl+C` ou:

```bash
docker ps            # lista containers ativos
docker stop <ID>     # substitua pelo ID do container
```

---

## 📁 Estrutura do projeto

```
.
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   └── index.html
├── imagens/
│   └── diagrama.png
│   └── teste.png
└── README.md
```

---
### Eduardo O. Lentz
💻 Portfolio | 🔗 LinkedIn | 📂 GitHub | 📝 Medium | 📸 Instagram
