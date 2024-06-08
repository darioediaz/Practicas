'''
#2
¿ES UN ANAGRAMA?
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
'''

def es_anagrama(palabra1, palabra2):
    if palabra1 == palabra2:
      print(f"Las palabras {palabra1} y {palabra2} no son anagrama")
    elif sorted(palabra1) == sorted(palabra2):
      print(f"Las palabras {palabra1} y {palabra2} son anagrama")
    else:
      print(f"Las palabras {palabra1} y {palabra2} no son anagrama")
  
palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")

es_anagrama(palabra1, palabra2)