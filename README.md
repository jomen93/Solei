<p align="center">
	<img src="images/databiz_image.jpeg" width="200" title="logotipo_databiz">
</p>

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

---

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

2. La segunda función se basa en las expresiones regulares, se identifican solamente los números con la suntaxis adecuada usando regex. Además de esto se incluye la identifiación de cédulas de ciudadanía que estén escrita con separadores de miles. Para hacer el refinamiento de esta función se consideran tres condiciones. Las dos primeras es que la longitud de cadena de números encontradas se ubiquen dentro de los 6 y 10 elementos. La siguiente condición se hace para diferenciar los números de cédula y los números de celular, esto se hace descartando los números encontrados que empicen en tres. La razón es la siguiente:

> Desde el 2006 la registraduría nacional del estado civil bajo la resolución 3007 de 2004, en su artículo 5 adopta que se establece el Número único de identificacioón personal (NUIP) cuya estructura alfanumérica determina la oficina de registro del estado civil y los iete siguientes a un consecutivo numérico. Desde el 2004 se empezó a asignar el NUIP iniciando su numeración en mil millones 1.000.000 en forma consecutiva sin hacer diferencia entre hombres y mujeres. Para conmesurar esto se consulta las tatas de natalidad del DANE



| Año          | % Natalidad    | Población     |
| :---:        |     :---:      |    :---:      |
| 2015         | 1.55 %         | 47.52 M       |
| 2016         | 1.53 %         | 48.18 M       |
| 2017         | 1.51 %         | 48.91 M       |
| 2018         | 1.49 %         | 49.66 M       |
| 2019         | 1.47 %         | 50.34 M       |

>  Los NIUP que se asignaron al cabo de 5 años son alrededor de 36 M, puede decirse que que en promedio , según la tendencia se consumen alrededor de 7.4 M digitos/año, veamos a este ritmo cuantos años durara de primer dígito el número 1:

<p aling="center">
	<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{999999999\text{&space;digitos}}{7400000&space;\text{&space;digitos/ano}}&space;\approx&space;135&space;\text{&space;anos}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{999999999\text{&space;digitos}}{7400000&space;\text{&space;digitos/ano}}&space;\approx&space;135&space;\text{&space;anos}" title="\frac{999999999\text{ digitos}}{7400000 \text{ digitos/ano}} \approx 135 \text{ anos}" /></a>
</p>
