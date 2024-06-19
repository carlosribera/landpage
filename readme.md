# Pasos para Ejecutar el proyecto
## 1. Crear y Activar un Entorno Virtual (Opcional pero Recomendado)
Es buena práctica usar un entorno virtual para gestionar las dependencias de tu proyecto. Aquí están los pasos para crear y activar uno:

Crear un Entorno Virtual

```
python -m venv nombre_del_entorno
```

Activar el Entorno Virtual
En Windows:
```
nombre_del_entorno\Scripts\activate
```
En macOS y Linux:
```
source nombre_del_entorno/bin/activate
```

## 2. Instalar los Requisitos en el Entorno Virtual
Una vez que el entorno virtual está activado, instala los requisitos:

```
pip install -r requirements.txt
```

3. Verificar la Instalación
Para asegurarte de que todas las dependencias se han instalado correctamente, puedes listar los paquetes instalados con:

```
pip list
```
Esto mostrará una lista de todos los paquetes instalados en tu entorno virtual.