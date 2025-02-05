# Treinamento da Rede YOLO com Dataset COCO no Google Colab

## 📌 Visão Geral

Este projeto envolve o treinamento da rede YOLO utilizando o dataset COCO e o Google Colab. O objetivo é rotular imagens, configurar o treinamento e resolver erros comuns encontrados no processo.

---

## 🔧 **1. Preparação do Ambiente**

### **1.1. Instalação das Dependências**

Antes de iniciar, instalamos as dependências necessárias:

```bash
!apt-get install nano -y  # Editor de texto
!pip install opencv-python numpy
```

### **1.2. Clonando o Darknet**

O Darknet é o framework necessário para treinar a YOLO:

```bash
!git clone https://github.com/AlexeyAB/darknet.git
%cd darknet
!make
```

---

## 📂 **2. Organização dos Dados**

### **2.1. Rotulando Imagens com LabelMe**

Para rotular as imagens manualmente, utilizamos o [LabelMe](http://labelme.csail.mit.edu/Release3.0/). Caso não queira rotular, podemos usar o dataset COCO já rotulado.

### **2.2. Estrutura das Pastas**

Certifique-se de que os dados estejam organizados corretamente:

```bash
/data/
 ├── images/
 │   ├── train/  # Imagens de treino
 │   ├── valid/  # Imagens de validação
 ├── labels/
 │   ├── train/  # Anotações de treino
 │   ├── valid/  # Anotações de validação
```

Caso a pasta `train` não exista, criamos com:

```bash
!mkdir -p data/images/train
```

---

## 🛠 **3. Configuração do YOLO**

### **3.1. Configuração do ****`obj.data`**

Criamos o arquivo `obj.data` com:

```
classes=2
train=data/train.txt
valid=data/valid.txt
names=data/obj.names
backup=backup/
```

### **3.2. Configuração do ****`obj.names`**

Definimos as classes a serem detectadas:

```
classe1
classe2
```

### **3.3. Arquivo de Configuração (****`yolov4.cfg`****)**

Alteramos o número de filtros na última camada convolucional:

```bash
filters = (classes + 5) * 3  # Para duas classes, filters = (2+5)*3 = 21
```

Também ajustamos os parâmetros de treinamento.

---

## 🚀 **4. Treinamento da Rede YOLO**

### **4.1. Gerando ****`train.txt`**

Certificamos que a lista de imagens de treino existe:

```python
import os
image_folder = "data/images/train"
image_files = [f"{image_folder}/{f}" for f in os.listdir(image_folder) if f.endswith(".jpg")]

with open("data/train.txt", "w") as f:
    f.write("\n".join(image_files))
```

Caso a pasta `train` não exista, criamos com:

```bash
!mkdir -p data/images/train
```

### **4.2. Executando o Treinamento**

```bash
!./darknet detector train data/obj.data cfg/yolov4.cfg yolov4.conv.137 -map
```

---

## 🛠 **5. Solução de Erros Comuns**

### **Erro 1: ****`Couldn't open file: data/train.txt`**

📌 Solução:

- Certifique-se de que as imagens de treino estão corretamente listadas no `train.txt`.
- Crie a pasta `data/images/train` se não existir.

### **Erro 2: ****`filters= in the [convolutional]-layer doesn't correspond to classes= in [yolo]-layer`**

📌 Solução:

- Ajuste os `filters` para `(classes + 5) * 3`.
- Verifique se `classes=2` está corretamente definido no arquivo `obj.data` e `yolo.cfg`.

### **Erro 3: ****`FileNotFoundError: [Errno 2] No such file or directory: 'data/images/train'`**

📌 Solução:

- Certifique-se de que a pasta `data/images/train` existe:

```bash
!mkdir -p data/images/train
```

---

## 📊 **6. Avaliação e Testes**

Após o treinamento, testamos a detecção com:

```bash
!./darknet detector test data/obj.data cfg/yolov4.cfg backup/yolov4_last.weights -thresh 0.3
```

E visualizamos os resultados.

---

## 📌 **Conclusão**

Este README documenta todo o processo de treinamento da YOLO com o dataset COCO, incluindo a preparação dos dados, configuração do treinamento e resolução de erros comuns. Agora a rede pode ser usada para detecção de objetos!

🚀 **Bons estudos e bom treinamento!**

faça as formatações adequadas

