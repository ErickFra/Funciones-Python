def eliminar_caracteres_especiales(text: str, old: list = ['á', 'é','í', 'ó', 'ú', 'ñ'], new: list = ['a', 'e', 'i', 'o', 'u', 'n']):
    
    texto_auxiliar = text
    
    # iteramo, reemplazamos y asignamos el texto sin los caracteres.
    for i in range(len(old)):
        texto_auxiliar = texto_auxiliar.replace(old[i], new[i])
        
    return texto_auxiliar
