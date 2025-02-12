# Reconhecimento Facial com Transfer Learning

## Descrição

Este projeto implementa um sistema de reconhecimento facial utilizando Transfer Learning com o modelo ResNet50 e a biblioteca OpenCV. O sistema é capaz de reconhecer rostos em tempo real através da câmera do notebook, permitindo identificar pessoas previamente cadastradas.

## Funcionalidades

- Detecção de rostos em tempo real
- Reconhecimento de identidades
- Treinamento do modelo com novas faces
- Captura de imagens da câmera

## Pré-requisitos

- Python 3.7+
- TensorFlow 2.0+
- Keras 2.0+
- OpenCV 4.0+
- NumPy
- Matplotlib

## Instalação

1. Clone este repositório: `git clone https://github.com/seu-nome/reconhecimento-facial.git`
2. Crie um ambiente virtual: `python3 -m venv .venv`
3. Ative o ambiente virtual: `source .venv/bin/activate`
4. Instale as dependências: `pip install -r requirements.txt`

## Como usar

1. Prepare o conjunto de dados:
   - Crie uma pasta `imagens_rosto`
   - Dentro dela, crie subpastas com o nome de cada pessoa
   - Coloque as fotos de cada pessoa em sua respectiva pasta

2. Execute o script de treinamento: `python treinar_modelo.py`

3. Execute o script de reconhecimento facial: `python reconhecer_faces.py`

## Estrutura de pastas

- `imagens_rosto`: Pasta com as imagens para treinamento
- `modelo_reconhecimento_facial.h5`: Arquivo com o modelo treinado
- `treinar_modelo.py`: Script para treinar o modelo
- `reconhecer_faces.py`: Script para reconhecimento facial com a câmera
- `requirements.txt`: Arquivo com as dependências do projeto

## Resultados

O modelo de reconhecimento facial apresenta uma precisão de X% no conjunto de dados de teste.

## Próximos passos

- Implementar detecção de faces múltiplas
- Otimizar o código para melhor desempenho
- Criar interface gráfica

## Licença

MIT License

## Autor

Carlos Henrique Scalambrine de Souza
