from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
lista_personas =[]
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])
for d in lista:
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])
    lista_personas.append(p)
operaciones = OperacionesPersona(lista_personas)
print(operaciones)
print("El promedio de notas 1 es: ",operaciones.obtener_promedio_n1())
print("El promedio de notas 2 es: ",operaciones.obtener_promedio_n2())

print("Las personas de nota1, con notas menores a 15 son",operaciones.obtener_listado_n1()) # que retorne los personas con notas1\
    # menores que 15
print("Las personas de nota2, con notas menores a 15 son",operaciones.obtener_listado_n2()) # que retorne los personas con notas2\
      # menores que 15
print("Las personas que empiezan con las letras R J  son:\n",operaciones.obtener_listado_personas("R", "J")) # que retorne listado de personas

        # menores empiecen su nombre con un "R" o "J"





   
