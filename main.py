numero_gallinas = int(input("¿Cuantas gallinas tienes?"))
huevos_por_gallina= 200
print("Tienes", numero_gallinas, "gallinas")
huevos_totales = numero_gallinas * huevos_por_gallina
print("Tus gallinas producen", huevos_totales, "huevos al año")
docenas_totales = huevos_totales / 12
print("Tu producción anual de huevos es de", docenas_totales, "docenas")
docenas_completas = huevos_totales // 12
print("Tu producción anual de huevos es de", docenas_completas, "docenas completas")
huevos_sueltos = huevos_totales % 12
print("Por lo tanto, te sobran", huevos_sueltos, "huevos")
precio_docena = float(input("Cuál es el precio de venta por docena?"))
ingresos_anuales = docenas_completas * precio_docena
print(f"Ingresos anuales estimados por la venta de huevos: {ingresos_anuales:.2f} €")
if numero_gallinas <= 30:
    print("Autoconsumo")
    print("No puedes vender huevos")
elif numero_gallinas <=150:
    print("Explotación reducida")
    print("Puedes vender huevos")
else:
    print("Explotación ordinaria")
    print("Puedes vender huevos")

print("Fin del programa")