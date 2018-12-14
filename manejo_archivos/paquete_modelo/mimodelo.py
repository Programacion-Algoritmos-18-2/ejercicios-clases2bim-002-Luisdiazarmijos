"""
    creación de clases
"""

class Persona(object):
    """
    """
    #Definimos los atributos que vamos a ocupar
    def __init__(self, n, ape, ed, cod, not1, not2):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(not1)
        self.nota2 = int(not2)
   #Definimos agregar nombre que recibe un parametro
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n
    #Definimos  obtener obtener
    def obtener_nombre(self):
        """
        """
        return self.nombre
        # Definimos edad que recibe un parametro
    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)
        # Definimos obtener edad
    def obtener_edad(self):
        """
        """
        return self.edad
     # Definimos agregar codigo que recibe un parametro
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)
        #Definimos obtener codigo
    def obtener_codigo(self):
        """
        """
        return self.codigo
     #Definimos obtener apellido
    def obtener_apellido(self):
        """
        """
        return self.apellido
        # Definimos agregar nota 1 qyue recibe un parametro
    def agregar_nota1(self, n):
        self.nota1 = int(n)
        pass
    def obtener_nota1(self):
        return self.nota1
        pass
    def agregar_nota2(self, n):
        self.nota2 = int(n)
    def obtener_nota2(self):
        return self.nota2
        pass

    #Sobrescribimos el metodo
    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.nota1, self.nota2)


class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado
        #Declaramos el metodo obtener promedio n1
    def obtener_promedio_n1(self):
    	#Indicialisamos suma 
        suma=0
        #Creamos un for para recorrer la lista
        for n in self.listado_personas:
        	#Almacenamos el valor obtenido en la variable suma
            suma= suma + n.obtener_nota1()
            #Sacamos el promedio con len para llegar al limite
        promedio = suma / len(self.listado_personas)
        #retornamos promedio
        return promedio    
        pass
        #Declarmos obtener promedio
    def obtener_promedio_n2(self):
    	#Declaramos suma
        suma=0
        #Declaramos cadena para imprimir al final
        cadena=""
        #Recorremos la lista con un for
        for n in self.listado_personas:
        	#Almacenamos suma
            suma = suma+ n.obtener_nota2()
            #Sacamos promedio
        promedio = suma / len(self.listado_personas)
        #Retornamos promedio
        return promedio   
        pass
        #Declaramos obtener listado n1 para sacar las notas menores a 15 de nota1
    def obtener_listado_n1(self):
    	#Declaramos una cadena para la concatenacion
        cadena=""
        #Declaramos un for para recorrer la lista 
        for n in self.listado_personas:
        	#Creamos un if para hacer la comparacion para poder imprimir
            if (n.obtener_nota1() < 15):
            	#Concatenamos cadena 
                cadena="%s%s%s\n"%(cadena, n.obtener_nombre(), n.obtener_apellido())
                #Imprimimos cadena
        return cadena

        
        #Declaramos obtener listado n2 para sacar las notas menores a 15 de nota2
    def obtener_listado_n2(self):
    	#Declaramos una cadena para la concatenacion
        cadena=""
        #Declaramos un for para recorrer la lista 
        for n in self.listado_personas:
        	#Creamos un if para hacer la comparacion para poder imprimir
           if (n.obtener_nota2() < 15):
           	#Concatenamos cadena 
              cadena="%s%s%s\n"%(cadena, n.obtener_nombre(),  n.obtener_apellido())
              #Retornamos cadena
        return cadena
    # Declaramos menores empiecen su nombre con un "R" o "J"
    def obtener_listado_personas(self, a, b):
    	#Declaramos una cadena para la concatenacion
        cadena=" "
        #Declaramos un for para recorrer la lista
        for n in self.listado_personas:
        #Declaramos un if para la compracion  de menores empiecen su nombre con un "R" o "J"
            if (n.obtener_nombre()[0:1]==a or n.obtener_nombre()[0:1]==b):
            	#Concatenamos cadena
                cadena="%s%s%s\n"%(cadena, n.obtener_nombre(), n.obtener_apellido())
                #Retornamos cadena
        return cadena
        pass



    def __str__(self):
    	#Declaramos cadena para la concatenacion
        cadena= ""
        #Creamos un for para recorrer la lista
        for n in self.listado_personas:
        	#Concatenamos cadena
            cadena="%s %s %s\n" %(cadena, n.obtener_nombre(), n.obtener_apellido())
            #Retornamos cadena
        return cadena
           
   