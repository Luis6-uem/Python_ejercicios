productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}

print("Lista de productos y precios:")
for producto, precio in productos.items():
    print(f"{producto}: ${precio:.2f}")
