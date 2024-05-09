def factoral(n):
    if n== 0:
       return 1
    else:
       return n * factoral(n - 1)
       
nombre = 5          
resultat = factoral(nombre)
print(f"le factoriell du {nombre} is {resultat}.")
