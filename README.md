<p align="center">
  <a href="#">
    🔗 <img src="https://github.com/Gelzieny/fastapi-do-zero/blob/main/.github/img/fast-api.png?raw=true" />
  </a>
</p>


## Descrição
Este projeto utiliza o framework FastAPI para criar uma API robusta e eficiente. FastAPI é um framework web moderno para Python que oferece suporte nativo a tipagem, validação automática de dados e documentação interativa.

## Tecnologias Utilizadas

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git, vscode, fastapi, postgres, python" />
</a>

- Python 11
- FastAPI
- Uvicorn
- Banco de dados (SQLite, PostgreSQL, ou outro)
- Prisma (se aplicável)
- Docker (se aplicável)
- Pytest para testes automatizados

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/Gelzieny/fastapi-do-zero.git
   cd fastapi-do-zero
   ```

2. Crie e ative um ambiente virtual:
  ```bash
  # Linux/macOS
  python -m venv venv && source venv/bin/activate && pip install -r requirements.txt 

  # Windows
  python -m venv venv && venv\Scripts\activate.bat && pip install -r requirements.txt     
  ```

3. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

## Executando o Projeto
1. Inicie o servidor FastAPI com Uvicorn:
  ```bash 
    python manage.py
  ```
2. Acesse a documentação interativa no navegador:
  
  - [Swagger UI](http://127.0.0.1:5092/docs)
  - [Redoc](http://127.0.0.1:5092/redoc)

## Estrutura do Projeto
```
seu-projeto/
│── src/
│   ├── app.py          # Ponto de entrada da API
│   ├── models.py       # Modelos de dados
│   ├── routes.py       # Definição das rotas
│   ├── database.py     # Configuração do banco de dados
│   ├── schemas.py      # Esquemas Pydantic
│── tests/
│   ├── test_main.py    # Testes automatizados
│── .env                # Variáveis de ambiente
│── requirements.txt    # Dependências do projeto
│── README.md           # Documentação do projeto
```

## Executando Testes
Execute os testes com pytest:
```bash
  pytest
```

## Docker (Opcional)
Para executar o projeto com Docker:
```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

## Contribuição
1. Fork este repositório
2. Crie uma nova branch (`git checkout -b feature-nova`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Envie para o branch (`git push origin feature-nova`)
5. Abra um Pull Request

# 🧑🏻‍💻 Autor

Feito com ❤️ por Gelzieny R. Martins 👋🏽 [Entre em contato!](https://www.linkedin.com/in/gelzieny-r-martins-180551106/)

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).
