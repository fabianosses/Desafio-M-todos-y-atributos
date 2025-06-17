import ingredientes

class Pizza:

# métodos de clases
  precio = 10000
  tipo = "Tamaño Familiar"

# método estático de validación de masa, proteina y vegetal
  @staticmethod
  def validar_elemento_en_lista(elemento, lista):
    return elemento in lista

# método no estático 
  def pedido(self, masa, proteico, *vegetales):
    self.masa = masa
    self.proteico = proteico
    self.vegetales = vegetales
    self.ingredientes = [self.proteico, *self.vegetales, self.masa]
    return self.ingredientes

  # solicita ingreso de proteina
  proteico_seleccionado = None
  while proteico_seleccionado not in ingredientes.proteicos:
    proteico_seleccionado = input(f"Seleccione el ingrediente proteico {ingredientes.proteicos}: ")
    if not validar_elemento_en_lista(proteico_seleccionado, ingredientes.proteicos):
      print("Ingrediente proteico no válido. Por favor, seleccione de la lista.")

  # solicita ingreso de dos vegetales
  vegetales_seleccionados = []
  while len(vegetales_seleccionados) < 2:
    vegetal_seleccionado = input(f"Seleccione un ingrediente vegetal {ingredientes.vegetales} ({len(vegetales_seleccionados) + 1} de 2): ")
    if validar_elemento_en_lista(vegetal_seleccionado, ingredientes.vegetales):
      if vegetal_seleccionado not in vegetales_seleccionados:
        vegetales_seleccionados.append(vegetal_seleccionado)
      else:
        print("Este vegetal ya ha sido seleccionado.")
    else:
      print("Ingrediente vegetal no válido. Por favor, seleccione de la lista.")

  # solicita ingreso de masa
  masa_seleccionada = None
  while masa_seleccionada not in ingredientes.masas:
    masa_seleccionada = input(f"Seleccione el tipo de masa {ingredientes.masas}: ")
    if not validar_elemento_en_lista(masa_seleccionada, ingredientes.masas):
      print("Masa no válida. Por favor, seleccione de la lista.")

