# Predicción con Modelo de Machine Learning – Dockerizado

## Presentado por
**Omar Torres**  
Estudiante de Ingeniería de Sistemas  
Proyecto Machine Learning: *Predictor en Actividades Bancarias*

## Entregado a
**Raul Ramos Pollan, Jonathan Granda**  
Facultad de Ingeniería  
Universidad de Antioquia

## Fecha de entrega
Octubre 2025

---

## Descripción del proyecto

Este proyecto implementa un modelo de Machine Learning en Python para predecir el resultado de ciertas actividades bancarias.  
El modelo y el flujo de predicción se ejecutan dentro de un contenedor Docker, lo cual garantiza un entorno limpio y reproducible.

## Nota 1
El profesor debe descargar el repositorio ubicado en la siguiente dirección
```bash
https://github.com/hombremono873/entrega_fase_2_con_descarga_kaggle.git

```
## Nota 2
```bash
El profesor debe unirse a la competencia de Kaggle fuente de este trabajo en los enlaces,

https://www.kaggle.com/competitions/playground-series-s5e8/overview
https://www.kaggle.com/competitions/playground-series-s5e8/data

```
El profesor debe obtener un token de acceso "kaggle.json" para acceder a los datasets 
train.csv, test.csv.
Debe ubicarse el archivo kaggle.json a la misma altura del archivo Dockerfile dentro de la carpeta,
predick_bank.

---

## Requisitos previos

- Docker Desktop instalado y ejecutándose
- Sistema operativo Windows con acceso a terminal (CMD o PowerShell)
- Proyecto organizado con la siguiente estructura:

## taller_IA_fase2/ # Carpeta principal del proyecto
## ├── datos/ # Carpeta externa para datasets y modelo entrenado
## │ ├── train.csv # Dataset de entrenamiento (descargado desde Kaggle)
## │ ├── test.csv # Dataset de prueba (descargado desde Kaggle)
## │ ├── sample_submission.csv # Archivo de ejemplo de submission (Kaggle)
## │ └── modelo_entrenado.pkl  # Modelo entrenado guardado
## ├── predict_bank/      # Código fuente del proyecto
## │ ├── app/             # Scripts principales
## │ │ ├── train.py       # Script de entrenamiento del modelo
## │ │ ├── predict.py     # Script de predicción
## │ │ └── init.py        # (opcional) indica que es un paquete Python
## │ ├── Dockerfile       # Configuración del contenedor Docker
## │ ├── requirements.txt # Dependencias del proyecto
## │ └── README.md        #  Documentación del proyecto
## | └──kaggle.json       # Credenciales de la API de Kaggle
## └──



---
## Ejecución del proyecto
## Construcción de la imagen Docker

1. Inicie la aplicación docker desktop
1. Arranque la aplicacion Doker Desktop
2. Ubíquese en la raíz del proyecto predict_bank

```bash

---

## Construcción de la imagen Docker

```bash
# Ubíquese en la raíz del proyecto a la altura de Dokerfile. Por ejemplo (Mi caso):
cd C:\Users\OMAR TORRES\Desktop\taller_IA_fase2\predict_bank

## Construir la imagen Docker
docker build -t predict-bank-app .

## Ejecutar el docker en modo interactivo
docker run -it --rm predict-bank-app
docker run -it --name predict-run predict-bank-app
```

Despues de haber construido la imagen del docker, la aplicación queda en modo interactivo,
Si es la primera vez que se ejecuta la aplicación ocurre lo siguiente.
Al ejecutar el train.py se accede a la clave almacenada en json, se descarga automaticamente los datasets
(train.csv, test.csv) almacenados en la carpeta temporal datos. Adicionalmente se genera el archivo modelo_entrenado.pkl y se ubica en la carpeta temporal datos.
Al ejecutar test.csv se prueba el modelo y se genera los archivos test.txt y sumisscion.csv, que se ubicaran en la carpeta temporal datos del docker. Igualmente se imprime en consola algunos resultados de la prediccion.

Entrenamiento del modelo
## Entrenamiento del modelo
root@4820ed2101ab:/app# python train.py
**Nota_1:** Se accede a los datasets (train.csv y test.csv), se realiza el entrenamiento, el modelo entrenado
  se almacena en la carpeta datos;  temporal en el docker
 
**Nota_2** El siguiente comando ejecuta las predicciones, al finalizar se descarga en la carpata temporal datos el archivo predicciones.txt

#Ejecutar predict.py
root@4820ed2101ab:/app# python predict.py

Para ver los archivos *.csv, resultados.txt, modelo entrenado.pkl, sample_submissions.csv
ejecute lo siguiente
```bash
root@014f8c1ffe20:/app# cd datos
root@014f8c1ffe20:/app/datos# ls
ls -lh datos  

```bash
#extraer predicciones.txt
#El comando muestra el docker activo y el <ID_O_NOMBRE>

Este es mi caso:
CONTAINER ID   IMAGE              COMMAND   CREATED          STATUS          PORTS     NAMES
4820ed2101ab   predict-bank-app   "bash"    16 minutes ago   Up 16 minutes             epic_zhukovsky

docker ps
<ID_O_NOMBRE> = 4820ed2101ab
docker cp <ID_O_NOMBRE>:/app/datos/predicciones.txt "%USERPROFILE%\Downloads\predicciones.txt"
**En mi caso el archivo de predicciones queda en descargas**

```

## Nota

```bash
# Gestión cierre de imagenes y docker

# Ver contenedores activos
 C:\cualquier ruta> doker ps
 # Ver contenedores activos y detenidos
 C:\cualquier ruta> doker ps -a
 # Elimna contenedores detenidos
 C:\cualquier ruta> docker container prune
 # Elimina todas las imagenes 
  C:\cualquier ruta>docker image prune -a

```
## En caso de consulta contactar a:
Omar Alberto Torres
tel: 3043440112
Correo: omar.torresm@udea.edu.co

Nota: En caso de requerir orientación adicional sobre la ejecución o los detalles técnicos del proyecto, puede contactarme al correo institucional o revisar los comentarios en el código fuente.





