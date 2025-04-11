<p align="center">
  <a href="#">
    🔗 <img src="https://github.com/Gelzieny/fastapi-do-zero/blob/main/.github/img/fast-api.png?raw=true" />
  </a>
</p>


## Descrição
Este projeto utiliza o framework FastAPI para criar uma API robusta e eficiente. FastAPI é um framework web moderno para Python que oferece suporte nativo a tipagem, validação automática de dados e documentação interativa.

## Documentação
Documentação completa do FastAPI pode ser encontrada em [Dunossauro](https://fastapidozero.dunossauro.com/).

Playlist de vídeos sobre FastAPI: [Curso de FastAPI](https://www.youtube.com/watch?v=QShMRcicxnE&list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP&t=2s)

## Tecnologias Utilizadas

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,vscode,fastapi,postgres,python,uvicorn" />
</a>


## Instalação

1. Clone este repositório:
  ```bash
    git clone https://github.com/Gelzieny/fastapi_do_zero.git
    cd fastapi-do-zero
  ```

2. Ative o ambiente virtual com:
  ```bash
    poetry env activate

    # No Windows, o comando acima apenas exibe o caminho do ambiente virtual, então você precisa ativá-lo manualmente:

    poetry env info --path

    # Exemplo de saída:
    C:\Users\SeuUsuario\AppData\Local\pypoetry\Cache\virtualenvs\nome-do-projeto-hash

    # Com esse caminho em mãos, rode:
    & "C:\Users\SeuUsuario\AppData\Local\pypoetry\Cache\virtualenvs\nome-do-projeto-hash\Scripts\Activate.ps1"

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
