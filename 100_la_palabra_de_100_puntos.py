'''
#100
LA PALABRA DE 100 PUNTOS
/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */
'''



palabra = input("Ingrese palabra para conocer puntaje: ")
palabra.lower()

def valor_palabra(palabra):
  abecedario = "abcdefghijklmnopqrstuvwxyz"
  sumador = 0
  for letra in palabra:
    for i in range(len(abecedario)):
      if letra == abecedario[i]:
        puntaje = i + 1
        sumador += puntaje
  
  return print(f"La palabra {palabra} suma {sumador} puntos") 

valor_palabra(palabra)
  