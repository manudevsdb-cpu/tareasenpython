compra = float(input("Valor de la compra: "))

if compra <= 50:
    descuento = 0
else:
    if compra <= 100:
        descuento = compra * 0.10
    else:
        if compra <= 200:
            descuento = compra * 0.20
        else:
            descuento = compra * 0.30

precio_final = compra - descuento

print("Descuento:", descuento)
print("Total a pagar:", precio_final)
