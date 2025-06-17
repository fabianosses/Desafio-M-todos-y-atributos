from pizza import Pizza

print(Pizza.precio)
print(Pizza.tipo)

mi_pizza = Pizza()

masa = Pizza.masa_seleccionada
proteico = Pizza.proteico_seleccionado
vegetal = Pizza.vegetales_seleccionados

mi_pizza.pedido(masa, proteico, *vegetal)
# imprime selección de masa, proteina, vegetales, resumen de ingredientes, precio y tamaño
print("\n--- Resumen de su Pedido ---")
print(f"Masa seleccionada: {mi_pizza.masa}")
print(f"Ingrediente proteico: {mi_pizza.proteico}")
print(f"Ingredientes vegetales: {mi_pizza.vegetales}")
print(f"Pizza válida: {mi_pizza.ingredientes}")
print(f"Precio: ${Pizza.precio}")
print(f"Tamaño: {Pizza.tipo}")