print(" ")
print("Alvaro Campechano 3W")
print(" ")

def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    """
    Calcula el total de una factura luego de aplicar el IVA.
    
    Args:
    cantidad_sin_iva (float): El monto total sin IVA.
    porcentaje_iva (float, opcional): El porcentaje de IVA a aplicar. Por defecto es 21%.
    
    Returns:
    float: El total de la factura incluyendo el IVA.
    """
    # Calcular el monto de IVA
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    
    # Calcular el total de la factura
    total_factura = cantidad_sin_iva + iva
    
    return total_factura

# Ejemplo de uso
monto_sin_iva = 100  # Puedes cambiar este valor
total = calcular_total_factura(monto_sin_iva)
print(f"El total de la factura es: {total:.2f}")
