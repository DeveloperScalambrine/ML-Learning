import tensorflow as tf
import numpy as np
import json
from pycocotools.coco import COCO
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

CLASSES_COCO = ['person', 'car', 'chair', 'bottle'] 
IMG_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 10

coco_train = COCO('/content/annotations/instances_train2017.json')  
coco_val = COCO('/content/annotations/instances_val2017.json') 

def load_image(image_id):
    img_data = coco_train.loadImgs(image_id)[0]
    img_path = 'coco/train2017/' + img_data['car_1']  
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    return img

def data_generator(coco, classes):
    while True:
        image_ids = coco.getImgIds()
        np.random.shuffle(image_ids)
        for i in range(0, len(image_ids), BATCH_SIZE):
            batch_ids = image_ids[i:i + BATCH_SIZE]
            batch_images = []
            batch_labels = []
            for image_id in batch_ids:
                img = load_image(image_id)
                ann_ids = coco.getAnnIds(imgIds=image_id)
                anns = coco.loadAnns(ann_ids)
                # Criação de labels multi-classe (um vetor para cada classe)
                labels = np.zeros(len(classes))
                for ann in anns:
                    cat_id = ann['category_id']
                    cat_name = coco.loadCats(cat_id)[0]['name']
                    if cat_name in classes:
                        class_index = classes.index(cat_name)
                        labels[class_index] = 1  # 1 se o objeto está presente na imagem
                batch_images.append(img)
                batch_labels.append(labels)
            yield np.array(batch_images), np.array(batch_labels)

# Modelo
base_model = tf.keras.applications.ResNet50(weights='imagenet', include_top=False, input_shape=(IMG_SIZE, IMG_SIZE, 3))
x = base_model.output
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
predictions = tf.keras.layers.Dense(len(CLASSES_COCO), activation='sigmoid')(x)  # Sigmoid para multi-classe
model = tf.keras.models.Model(inputs=base_model.input, outputs=predictions)

# Compilação e Treinamento
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Binary_crossentropy para multi-classe

train_generator = data_generator(coco_train, CLASSES_COCO)
val_generator = data_generator(coco_val, CLASSES_COCO)

model.fit(train_generator, steps_per_epoch=len(coco_train.getImgIds()) // BATCH_SIZE, epochs=EPOCHS,
          validation_data=val_generator, validation_steps=len(coco_val.getImgIds()) // BATCH_SIZE)

def extract_features(model, coco, classes):
    features = []
    image_ids = coco.getImgIds()
    for image_id in image_ids:
        img = load_image(image_id)
        # Adicione uma dimensão de batch (necessário para o modelo)
        img = np.expand_dims(img, axis=0)
        feature = model.predict(img)
        features.append(feature.flatten())  # Adicione flatten para ter um vetor 1D
    return np.array(features)

train_features = extract_features(model, coco_train, CLASSES_COCO)
val_features = extract_features(model, coco_val, CLASSES_COCO)

def recommend_similar_images(image_features, all_features, top_n=5):
    # Calcula a similaridade cosseno entre a imagem e todas as outras
    similarities = cosine_similarity(image_features.reshape(1, -1), all_features)
    # Obtém os índices das imagens mais similares
    similar_indices = np.argsort(similarities[0])[::-1][1:top_n+1]  # Exclui a própria imagem
    return similar_indices

# Exemplo de uso:
image_id_referencia = coco_train.getImgIds()[0]  # Escolha um ID de imagem de referência
img_referencia = load_image(image_id_referencia)
feature_referencia = model.predict(np.expand_dims(img_referencia, axis=0)).flatten()

indices_similares = recommend_similar_images(feature_referencia, train_features)
# Exiba as imagens recomendadas (você precisará adaptar esta parte para sua aplicação)
for indice in indices_similares:
    img_id = coco_train.getImgIds()[indice]
    img_data = coco_train.loadImgs(img_id)[0]
    img_path = 'coco/train2017/' + img_data['car_1']  # Ajuste o caminho
    img = plt.imread(img_path)
    plt.imshow(img)
    plt.title(f"Similaridade: {cosine_similarity(feature_referencia.reshape(1, -1), train_features[indice].reshape(1, -1))[0][0]}")
    plt.show()
