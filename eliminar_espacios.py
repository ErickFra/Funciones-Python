def eliminar_espacios (text: str):
    
    # Reemplazamos los saltos de linea si existen (\n).
    reemplazo_salto_linea = text.replace("\n", "")
    
    # Dividimos la cadena de texto por los espacios que tenga
    texto_lista = reemplazo_salto_linea.split(" ")
    
    # seleccionamos solo los que son palabras.
    texto_lista_sin_vacios = [i for i in texto_lista if i != ""]
    
    # Unimos la cadena, ppr un solo espacio.
    texto_limpio = " ".join(texto_lista_sin_vacios)
    
    return texto_limpio
