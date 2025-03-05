productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}
valor_limite = 1.0

productos_filtrados = [producto for producto, precio in productos.items() if precio > valor_limite]

print(f"Productos con precio mayor a ${valor_limite}: {productos_filtrados}")
