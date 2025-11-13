from django.contrib.auth.models import User
from django.http import HttpResponse

def crear_admin(request):
    # Verifica si el admin ya existe
    if not User.objects.filter(username="leti").exists():
        # Crea el superusuario
        User.objects.create_superuser(
            username="leti",
            email="leti@gmail.com",
            password="222009020Leti"
        )
        return HttpResponse("✅ Superusuario 'leti' creado con éxito.")
    return HttpResponse("⚠️ El superusuario 'leti' ya existe.")
