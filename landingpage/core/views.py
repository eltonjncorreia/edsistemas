from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from landingpage.core.forms import ContatoForm


def home(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso, logo entraremos em contato')
    else:
        form = ContatoForm()

    return render(request, 'core/index.html', {'form': form})












