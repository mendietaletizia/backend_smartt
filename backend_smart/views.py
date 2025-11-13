from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

User = get_user_model()


@require_http_methods(["GET"])
def setup_admin(request):
    if not getattr(settings, 'ENABLE_SETUP_ENDPOINT', False):
        return HttpResponse("Endpoint deshabilitado.", status=403)

    env_token = getattr(settings, 'SETUP_ADMIN_TOKEN', '')
    request_token = request.GET.get('token', '')
    if env_token and env_token != request_token:
        return HttpResponse("Token inválido.", status=403)

    try:
        call_command('migrate', interactive=False)

        username = getattr(settings, 'SETUP_ADMIN_USERNAME', 'admin')
        email = getattr(settings, 'SETUP_ADMIN_EMAIL', 'admin@example.com')
        password = getattr(settings, 'SETUP_ADMIN_PASSWORD', '')

        if not password:
            return HttpResponse("⚠️ Configura SETUP_ADMIN_PASSWORD antes de usar este endpoint.")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            return HttpResponse(f"✅ Migraciones ejecutadas y superusuario '{username}' creado.")

        return HttpResponse(f"⚠️ Superusuario '{username}' ya existe, migraciones ejecutadas.")
    except Exception as exc:
        return HttpResponse(f"❌ Error: {exc}", status=500)
