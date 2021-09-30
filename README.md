<p align="center">
	<img src="images/databiz_image.jpeg" width="200" title="logotipo_databiz">
<p>

# Solei

Solei es una herramienta que se crea fundamentalmente para hacer extracción de numeros de documentos de identidad en archivos de diferentes formatos como pdf, jpeg, jpg, png, svg. Permite administrar la clasificación de estos registros por documentos de identidad. En versiones posteriores se pretende incluir en la extracción de información otros campos asociados, tales como nombres, direcciones y cualquier otra información de valor que se puedan extraer para clasificar la gestión documental de una empresa

Es un código de OCR basado en dos API´s. La primera de ellas es Tesseract que contiene un motor de OCR basado en redes neuronales del tipo LSTM que se centra en el reconocimiento de líneas. Tesseract es compatible con Unicode (UTF-8)y viene preprogramado para reconocer alrededor de 100 idiomas. La segunda se relaciona con la visión por computador de Azure. 

## Tesseract

### Requisitos mínimos

* Soporte de C++17 es requerido para la compilación

### Uso

Para ignorar los warnigs por compilación se debe imponer

```python
Ignore_warnings = True
```

Cuando el programa hace el reconocimiento crea archivos adicionales con el mismo nombre y adicionandole el numero de identificación que se encontró. si se desean activar cajas para encerrar las palabras encontradas se debe activar la siguiente bandera

```python
Save_boxes = True
```

Por otra parte este código hace un análizis reducido en resolución para hacer más económico el computo, si se necesita utilizar con imagenes de resolucion más baja se debe activar un método de análisis de mayor resolución, que se activa con la siguiente bandera, es preciso mencionar que esto puede hacer que el código tarde aproximadamente cuatro veces más:

```python
High_analysis = True
```

Para hacer la ejecución de este programa de identificación de documentos de identidad se debe posicionar la terminal en el mismo nivel de jerarquia del archivo "OCR.py" teniendo el entorno virtual activo "enviroment.yml ", finalmente ejecutar  el script de la siguiente manera 

```bash
python OCR.py
```

## Visión por computadora de Azure

En este caso se utiliza la API de visión por computadora de Azure, se incluyen las credenciales dentro del código, en el caso ideal debería encriptarse o manejar de mejor manera la seguridad de las peticiones al servicio de Azure. Para usar el código hace falta activar el entorno virtual `enviroment.yml` y ejecutar el programa principal, de la siguiente manera

```python
python OCR_main.py
```

En este caso para la identificación del modelo se hace 

--

## Identificacion 

Para identificar las cedulas de ciudadanía dentro de una bolsa de palabras que encuentran los dos métodos planteados anteriormente se escriben dos funciones que ayudan a este respecto:

1. Una función basada en dos condiciones, la primera de ellas es imponer la condición que solamente se quiere obtener las cadenas de texto que tengan entre 6 y 10 elementos, además de esto que estas cadenas de texto que pasen esta condición deberas poder transformarse a numeros enteros. Una vez hecho solamente se eligen los elementos únicos que se encuentren

```python
def get_cc(x):
	numbers = []
	for i in range(len(x)):
		for j in x[i].split():
			try:
				if len(j) > 6 and len(j) <=10:
					numbers.append(int(j))
			except:
				pass
	numbers = np.array(numbers)
	u, c = np.unique(numbers, return_counts=True)
	if len(c) == 1 and c[0] == 1:
		return u
	else:
		return u[c>1]
```


	

