class Pizza:

    masas = {
        1: {"Nombre": "Tradicional"},
        2: {"Nombre": "Delgada"}
    }

    proteinas = {
        1 : {"Nombre": "Pollo"},
        2 : {"Nombre": "Vacuno"},
        3 : {"Nombre": "Carne vegetal"}
    }

    vegetales = {
        1: {"Nombre": "Tomate"}, 
        2: {"Nombre": "Aceitunas"},
        3: {"Nombre": "Champiñones"}
    }

    def validate(opciones, eleccion):
        # Definir validación de eleccion
        ##########################################################################
        while eleccion not in opciones:
            print("Opción no válida, ingrese una de las opciones válidas: ")
            eleccion = input("Ingresa una Opción: ").lower()
        ##########################################################################
        return eleccion


    def pedido():
        pass

    # método pedido de masa
masa = input("""
    Elige masa:
    1. Tradicional.
    2. Delgada.
    """)
        
        # validación de datos ingresados
masa = Pizza.validate(["1","2"], masa)
print(type(masa),f"N°: {masa}")
masa = Pizza.masas[int(masa)]
print(f"tu proteina: {masa}")

    # método pedido de proteina
proteina = input("""
    Elige el sabor proteina:
    1. Pollo.
    2. Vacuno.
    3. Carne vegetal.
    """)
print(type(proteina),f"N°: {proteina}")
        # validación de datos ingresados
proteina = Pizza.validate(["1", "2", "3"],proteina)
proteina = Pizza.proteinas[int(proteina)]
print(f"tu proteina: {proteina}")


    # método pedido de vegetales
vegetal = input("""
    Elige los vegetales:
    1. Tomate.
    2. Aceitunas.
    3. Champiñones.
    """)
        #validación de datos ingresados
vegetal = Pizza.validate(["1","2","3"], vegetal)
print(type(vegetal),f"N°: {vegetal}")
vegetal = Pizza.vegetales[int(vegetal)]
print(f"tu proteina: {vegetal}")

