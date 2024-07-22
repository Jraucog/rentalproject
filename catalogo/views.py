from django.shortcuts import render


def catalogo(request):
    # Asumiendo que tienes una lista de objetos de equipos (puedes reemplazar esto con tus datos reales)
    equipment_list = [
        {'name': 'Laptop', 'description': 'Potente laptop para desarrollo'},
        {'name': 'Impresora', 'description': 'Impresora de alta calidad para uso en la oficina'},
        {'name': 'Monitor', 'description': 'Monitor grande para una mejor productividad'},
        # Agrega más elementos de equipos aquí
    ]

    # Renderiza la plantilla con la lista de equipos
    return render(request, 'catalogo.html', {'equipment_list': equipment_list})
