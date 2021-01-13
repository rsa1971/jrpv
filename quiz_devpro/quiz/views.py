from django.http import HttpResponse
from django.shortcuts import render

from quiz_devpro.quiz.models import Pergunta


def indice(requisicao):
    # return HttpResponse('Olá Mundo!')
    return render(requisicao, 'quiz/indice.html')


def perguntas(requisicao, indice):
    pergunta=Pergunta.objects.all.filter(disponivel=True).order_by('id')[0]
    # return HttpResponse('Olá Mundo!')
    contexto = {'indice': indice}
    return render(requisicao, 'quiz/perguntas.html', contexto, pergunta)


def classificacao(requisicao):
    # return HttpResponse('Olá Mundo!')
    return render(requisicao, 'quiz/classificacao.html')
