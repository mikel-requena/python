venta = float(input("Ingrese Monto De La Venta: $"))
if venta <= 250.00:
    descuento = 0.05
    ventaTotal = venta - (venta * descuento)
elif venta <= 700.00:
    descuento = 0.085
    ventaTotal = venta - (venta * descuento)
elif venta <= 1000.00:
    descuento = 0.10
    ventaTotal = venta - (venta * descuento)
elif venta > 1000:
    descuento = 0.15
    ventaTotal = venta - (venta * descuento)
descuentoReal = descuento * 100
print(f"Monto Original: ${venta}. Descuento: {descuentoReal}%. Monto Con Descuento: ${ventaTotal}")