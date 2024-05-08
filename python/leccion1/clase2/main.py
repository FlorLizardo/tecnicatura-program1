'''
miVar = 3
print(miVar)
miVar = 'Hola a todos'
print(miVar)
miVar = 3.5
# print es una funcion
print(miVar)
# cada valor e suna literal: una literal es un valor que
# se puede asignar a nuestras variables
x = 10
y = 2
z = x + y
print(id(x))  # id nos muestra la direccion de memoria donde
# esta guardada nuestra literal. En este caso tenems una
# funcion (id) dentro de oytra funcion (print)
# las literales se escriben x168 (se antepone una x y
# los ultimos tres nros de nuestra direccion de memoria.
# Esta direccion no es permanente. Se llama 'referencia de memoria'
print(id(y))
print(id(z))

# tipos de datos
a: str = 'Hola a todos'  # tipo string. con str le estoy diciendo
# que tipo de variable es. Es solo una referencia, solo digo que
# tipo de dato deberia ser, pero no me da error si le pongo otro
# tipo de dato. Es como una 'pista' acerca del tipo
print(type(a))  # para mostrar el tipo. Es una funcion dentro de otra
b = 10.78  # FLOAT
print(type(b))
c = True  # boolean. True y False tienen que ir con la primera letra
# en mayuscula
print(type(c))
# los tipos de datos son clases
d = 10  # tipo int
print(type(d))

x = 10
print(x)
print(type(x))
x = 15.5
print(x)
print(type(x))
x = 'Hola'
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# manejo de cadenas
miGrupoFavorito = 'Chayanne:'  # no es necesario
# poner el sigo mas en una cadena de caracteres para concatenar
caracteristicas = 'Aprobado por Chayanne'
print('Mi grupo favorito es', miGrupoFavorito, caracteristicas)

num1 = '7'
num2 = '8'
print(int(num1) + int(num2))  # si son cadenas, los concatena.
# con int los transformo a nro. Si no son nros, no se puede usar int

# tipos booleans (bool)
miBool = True
print(miBool)
miBool = False
print(miBool)
miBool = 1 > 2
print(miBool)
miBool = 1 < 3
print(miBool)

# CONDICIONAL CON BOOLEANS
if miBool:
    print('El resultado es verdadero')
else:
    print('El resultado es falso')

# procesar entrada del usuario
# funcion input, pedir datos al usuario
# resultado = input('Digite un nro: ')  # regresa un dato tipo string
# print(resultado)
'''

'''
# conversion de la entrada de datos funcion input
numero1 = int(input('Escribe el primer nro: '))
numero2 = int(input('Escribe el segundo nro: '))
resultado = numero1 + numero2
print('El resultado de la suma es', resultado)
'''

'''
Ejercicio 1: Califica tu día 
¿Cómo estuvo tu día (1 al 10)?
Mi día estuvo de: 10
'''

'''
miDia = int(input('¿Cómo estuvo tu día (1 al 10)? '))
print('Mi día estuvo de:', miDia)

'''

'''
Ejercicio 2: 
Se solicita incluir la siguiente información acerca de un libro:
- título
- autor
Debes imprimir la información en el siguiente formato:
Proporciona el título:
Proporciona el autor:
<título> fue escrito por <autor>
'''

'''
print('Mis libros')
titulo = input('Proporciona el título: ')
autor = input('Proporciona el autor: ')
print(titulo, 'fue escrito por', autor)

'''

'''
# operadores aritmeticos: suma
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print('Resultado: ', suma)
print(f'el resultado es: {suma}')  # interpolacion: la f es obligatoria

# operadores arit: resta
resta = operandoA - operandoB
print(f'resta: {resta}')

# multiplicacion
multiplicacion = operandoA * operandoB
print(f'multiplicacion: {multiplicacion}')

# division
division = operandoA / operandoB
print(f'division: {division}')

# division con resultado en enteros
divisionInt = operandoA // operandoB
print(f'division (int): {divisionInt}')

#modulo
modulo = operandoA % operandoB
print(f'modulo: {modulo}')

# exponente
exponente = operandoA ** operandoB
print(f'exponente: {exponente}')

'''

'''
ejercicio: calcular el area y el eprimetro de un rectangulo.
Para ello, crear variables alto(int) y ancho(int). El usuario debe
proporcionar los valores de alto y ancho, despues se debe imprimir el 
resultado.
'''
'''
alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'Area: {area}')
print(f'Perimetro: {perimetro}')
'''

'''
# operadores aritmeticos: asignacion
miVariable3 = 10
print(miVariable3)

# operadores: reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

# incremento con reasignacion reducida
miVariable3 += 1
print(miVariable3)

# reasignacion resta
miVariable3 -= 2
print(miVariable3)

# reasignacion multiplicacion
miVariable3 *= 3
print(miVariable3)

# reasignacion division
miVariable3 /= 2
print(miVariable3)

# operadores de comparacion
# igualdad
d = 4
b = 2
resultado = d == b  # como resultado dara un boolean
print(resultado)

# operador: diferentes
resultado = d != b
print(resultado)

# operador: mayor/menor que
resultado = d > b
print(resultado)

resultado = d < b
print(resultado)

# mayor/menor o igual que
resultado = d >= b
print(resultado)

resultado = d <= b
print(resultado)
'''

'''
Ejercicio: nro par o impar
1) solicitamos al usuario que ingrese un nro
2) este se asigna a una variable
3) se debe usar la estructura if/else
4) si es true imprimos que es par
5) si es false imprimimos que es impar
'''
'''
num = int(input('Ingrese un nro: '))
print(f'El residuo de la division es: {num % 2}')

if (num % 2 == 0):
    print(f'El nro {num} es par')
else:
    print(f'El nro {num} es impar')
'''

'''
Ejercicio: determinar si es mayor de edad.
1) pedir un nro al usuario
2) almacenar el valor en un variable
3) usar la estructura if/else
4) la formula es: <num> >= 18
5) True: eres mayor de edad
6) false: eres menor de edad
'''

edadAdulto = 18
edad = int(input('Ingrese su edad: '))

if (edad >= edadAdulto):
    print(f'Tu edad es {edad} años, eres mayor de edad')
else:
    print(f'Tu edad es {edad} años, eres menor de edad')
