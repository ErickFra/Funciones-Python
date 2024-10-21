class Limpieza:
    
    def EliminarEspacios(self, texto: str):
        
        # Reemplazamos los saltos de linea (si existen en el texto).
        eliminar_saltos_linea = texto.replace("\n", "")
        
        # Separamos el texto por palabras.
        texto_lista = eliminar_saltos_linea.split(" ")
        
        # Seleccionamos los textos en la lista que no sean espacios.
        texto_lista_sin_espacios = [i for i in texto_lista if i != ""]
        
        # Unimos los textos con un espacio
        texto_limpio = " ".join(texto_lista_sin_espacios)
        
        return texto_limpio
    
    def EliminarCaracteresEspeciales(self, texto: str, old: list = ['á', 'é','í', 'ó', 'ú', 'ñ'], new: list = ['a', 'e', 'i', 'o', 'u', 'n']):
        
        # Variable auxiliar.
        texto_auxiliar = texto
        
        # Hacemos el cambio de los caracteres especiales que se pasen por parametro.
        for i in range(len(old)):
            texto_auxiliar = texto_auxiliar.replace(old[i], new[i])
            
        return texto_auxiliar
    
    def EliminarEspaciosCaracteresEspeciales(self, texto: str, old: list = ['á', 'é','í', 'ó', 'ú', 'ñ'], new: list = ['a', 'e', 'i', 'o', 'u', 'n']):
        
        texto_correcto = self.EliminarEspacios(texto)
        texto_correcto = self.EliminarCaracteresEspeciales(texto_correcto, old, new)
        
        return texto_correcto
        
