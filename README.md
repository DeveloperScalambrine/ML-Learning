# Sistema de Assistência Virtual com PLN em Python

Este repositório contém um sistema de assistência virtual desenvolvido em Python, utilizando Processamento de Linguagem Natural (PLN) para interagir com o usuário através de voz e texto.

## Funcionalidades

O sistema possui dois módulos principais:

1.  **Text-to-Speech (TTS):** Transforma texto em áudio, permitindo que o sistema "fale" com o usuário.
2.  **Speech-to-Text (STT):** Transforma a fala do usuário em texto, possibilitando que o sistema "entenda" os comandos e perguntas.

Além disso, o sistema oferece as seguintes funções automatizadas, acionadas por comandos de voz:

*   **Pesquisa no Wikipedia:** Abre a página do Wikipedia com o termo pesquisado.
*   **Abertura do Youtube:** Abre o Youtube no navegador padrão do usuário.

## Requisitos

Para executar o sistema, você precisará ter o Python instalado em seu computador, além das seguintes bibliotecas:

*   `speech_recognition`
*   `gTTS`
*   `wikipedia`
*   `webbrowser`

Você pode instalar as bibliotecas utilizando o pip:

```bash
pip install speech_recognition, gTTS, wikipedia, webbrowser
```
Licença
Este projeto está licenciado sob a licença MIT.

Desenvolvido por: Carlos Henrique Scalambrine de Souza

Data: 18/02/2025
