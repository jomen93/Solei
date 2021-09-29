<p align="center">
	<img="images/databiz_image.jpeg" width="200" title="logotipo_databiz">
<p>

# Solei

Solei es una herramienta que se crea fundamentalmente para hacer extracción de documentos de identidad de documentos en diferentes formatos como pdf, jpeg, jpg, png, svg. y permite administrar la clasificación de documentos de almacenados por documentos de identidad. En versiones posteriores se pretende incluir en la extracción de información otros campos asociados como nombres, direcciones y cualquier otra información de valor que se puedan extraer para clasificar la gestión documental de una empresa

Es un código de OCR basado en dos API´s. La primera de ellas es Tesseract que contiene un motor de OCR basado en redes neuronales del tipo LSTM que se centra en el reconocimiento de líneas. Tesseract es compatible con Unicode (UTF-8)y viene preprogramado para reconocer alrededor de 100 idiomas. 

## Tesseract

### Requisitos mínimos

* Soporte de C++17 es requerido para la compilación

### Uso

Para ignorar los warnigs por compilación se debe imponer

```python
ignore_warnings = True
```

Cuando el programa hace el reconocimiento crea archivos adicionales con el mismo nombre y adicionandole el numero de identificación que se encontró. si se desean activar cajas para encerrar las palabras encontradas se debe activar la siguiente bandera

```
Save_boxes = True
```

Por otra parte este código hace un análizis reducido en resolución para hacer más económico el computo, si se necesita utilizar con imagenes de resolucion más baja se debe activar un método de análisis de mayor resolución, que se activa con la siguiente bandera, es preciso mencionar que esto puede hacer que el código tarde aproximadamente cuatro veces más:

```
High_analysis = True
```

Para hacer la ejecución de este programa de identificación de documentos de identidad se debe posicionar la terminal en el mismo nivel de jerarquia del archivo "OCR.py" teniendo el entorno virtual activo "enviroment.yml ", finalmente ejecutar  el script de la siguiente manera 

```bash
python OCR.py
```

## Visión por computadora de Azure




--

## Modo de uso 

```python
import reading
import reconigzed
```


	

