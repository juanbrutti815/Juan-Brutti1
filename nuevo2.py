def evaluar(nombre,nota1,nota2):
    promedio=(nota1+nota2)/2
    
    if promedio >= 6:
        return f"{nombre} aprobo con {promedio}"
    else:
        return f"{nombre} reprobo con {promedio}"
resultado=evaluar("Juan",10,9)
print(resultado)