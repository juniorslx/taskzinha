from django.shortcuts import render, redirect
from .forms import MensagensForm
from .models import Mensagens
from django.shortcuts import get_object_or_404

def home(request):
    if request.method == 'POST':
        form = MensagensForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MensagensForm()

    mensagens = Mensagens.objects.order_by('-criado_em')
    return render(request, 'home.html', {'form': form, 'mensagens': mensagens})


def delete_mensagem(request, pk):
    mensagem = get_object_or_404(Mensagens, pk=pk)
    if request.method == 'POST':
        mensagem.delete()
        return redirect('home')
    # Se quiser pode dar um GET e mostrar um aviso, mas pra simplicidade só redireciona
    return redirect('home')
