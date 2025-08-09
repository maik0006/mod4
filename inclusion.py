productos_disponibles = ["manzana","naranja","platano","uva","pera"]
productos_deseados = ["manzana","kiwi","pera"]
for producto in productos_deseados:
    disponible = producto in productos_disponibles
    if disponible:
        estado = "disponible"
    else:
        estado = "no disponible"    
print(f"El producto '{producto}' esta {estado}")