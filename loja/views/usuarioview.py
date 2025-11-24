from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.userusuarioform import UserUsuarioForm, UserForm

def list_usuario_view(request):
    usuarios = Usuario.objects.filter(perfil=2)
    return render(request, 'usuario/usuario.html', {'usuarios': usuarios})

def edit_usuario_view(request):
    usuario = get_object_or_404(Usuario, user=request.user)

    if request.method == 'POST':
        usuarioForm = UserUsuarioForm(request.POST, instance=usuario)
        userForm = UserForm(request.POST, instance=request.user)

        if usuarioForm.is_valid() and userForm.is_valid():
            usuarioForm.save()
            userForm.save()
            return redirect('usuario')
    else:
        usuarioForm = UserUsuarioForm(instance=usuario)
        userForm = UserForm(instance=request.user)

    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm,
    }

    return render(request, 'usuario/usuario-edit.html', context)
