for sem in range(1,5):
    print(f"\nSemana #{sem}")
    total_sem = 0
    
    for dia in range (1,8):
        gastos = float(input(f"Ingrese el gasto del día {dia}: C$"))
        total_sem += gastos
        total_mes = 0
        
    print(f"Total gastado en la semana {sem}: C${total_sem:2f}")
    total_mes += total_sem

print(f"\nTotal gastado en el mes: C${total_mes:.2f}")