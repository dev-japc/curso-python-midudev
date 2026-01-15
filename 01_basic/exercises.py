###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
name = Giorgio
city = world
print(f"Hello people my name is{name} and I live in {city}")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"tipo de dato de a: {a} {type(a)},\n tipo de dato de b: {b} {type(b)},\n tipo de dato de  c: {c} {type(c)}")
print(f"tipo de dato de d: {d} {type(d)},\n tipo de dato de e: {e} {type(e)},\n FIN ----- XD")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
### Da error si introduces un caracter no numerico
exm_str_number = "12345"
int_exm_str_number = int(exm_str_number)
print(f"ejemplo de cadena de texto numerica transformada en entero: {int_exm_str_number} {type(int_exm_str_number)}")
print("--------------")

# str to float number exercise
float_exm_str_number = float(exm_str_number)
print(f"ejemplo de cadena de texto casteada a float: {float_exm_str_number} {type(float_exm_str_number)}")

#float to int example exercise
float_number = 3.99
float_to_int_number = int(float_number)
print(f"------el resultado de float a int es: {float_to_int_number}")
print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = "Midu"
last_name = "Dev"
user_age = 39
height = 1.70
print(f"Hola me llame {name} {last_name} y mi edad es {user_age} vueltas al sol, mido {height} metros")
print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi_variable = 3.14
print(f"pi variable: {pi_variable}")

rounded_pi = round(pi_variable)
print(f"--- rounded pi variable: {rounded_pi}")
print(f"dividing rounded pi against 2: {rounded_pi / 2}")

print("--------------")
