clientes_atendidos = int(input("Ingese la cantidad de clientes atendidos: "))

total_ventas = 0

for cliente in range(clientes_atendidos):
    print(f"\nCliente {cliente + 1}:")
    
    porciones = int(input("¿Cuantas porciones de vigorón compró? "))
    
    total_cliente = 0
    
    for porcion in range(porciones):
        precio_unitario = float(input(f"Ingrese el precio de la porción #{porcion}: "))
        total_cliente += precio_unitario
        
    print(f"Total a pagar por el cliente {cliente}: C${total_cliente:2f}")
    
    total_ventas += total_cliente

print(f"\nTotal de ventas en toda la feria: C${total_ventas:2f}")