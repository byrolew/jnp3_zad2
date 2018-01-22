from collections import namedtuple
import random

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse

from .models import (
    Experiment, 
    Event,
    TaskRandom,
    Task,
)


def menu(request):
    return render(request, 'core/menu.html', {'next_url': reverse('menu')})

def pe(request):
    if request.method == 'POST':
        # update tasks
        if request.POST.get('content'):
            last_task = Task.objects.latest('my_id')
            content_1 = request.POST.get('content_1')
            content_2 = request.POST.get('content_2')
            Q = request.POST.get('Q')
            nQ = request.POST.get('nQ')
            P = request.POST.get('P')
            nP = request.POST.get('nP')
            rule = request.POST.get('rule')
            instr = request.POST.get('instruction')
            if any([content_1, content_2, Q, nQ, P, nP, rule, instr]):
                Task.objects.create(
                    content=content,
                    Q=Q,
                    nQ=nQ,
                    P=P,
                    nP=nP,
                    rule=rule,
                    instruction=instr,
                    my_id=last_task.my_id + 1
                )
        else:
            post = request.POST
            ex_tasks = post.getlist('tasks')
            tasks = list(Task.objects.filter(my_id__in=ex_tasks))

            if tasks is not None:
                experiment = Experiment(
                    mode=post.get('mode'),
                    time_to_red=post.get('time_to_red'),
                    time_train_gil=post.get('time_train_gil'),
                    time_test_gil=post.get('time_test_gil'),
                    time_train_cards=post.get('time_train_cards'),
                    welcome=post.get('welcome'),
                    instr_gil=post.get('instr_gil'),
                    instr_cards=post.get('instr_cards'),
                )
                experiment.save()

                random.shuffle(tasks)
                rand_tasks = []
                for t in tasks:
                    rand_tasks.append(
                        TaskRandom(
                            experiment=experiment,
                            task=t,
                            trial=False,
                        ),
                    )

                TaskRandom.objects.bulk_create(rand_tasks)

    Time = namedtuple('Time', ['name', 'text', 'default'])
    times = [
        Time('time_to_red', 'Czas do zapalenia czerwonego ekranu [ms]', 'domyślny czas'),
        Time('time_train_gil', 'Czas treningu GIL [ms]', 'domyślny czas'),
        Time('time_test_gil', 'Czas testu GIL [ms]', 'domyślny czas'),
        Time('time_train_cards', 'Czas treningu karty + GIL [ms]', 'domyślny czas'),
    ]
    Inp = namedtuple('Inp', ['name', 'text', 'default'])
    input_names = [
        Inp('welcome', 'Tekst powitania', 'domyślny tekst'),
        Inp('instr_gil', 'GIL - instrukcja', 'domyślny tekst'),
        Inp('instr_cards', 'Karty - instrukcja', 'domyślny tekst'),
    ]

    tasks = Task.objects.all()

    return render(request, 'core/pe.html', {
        'input_names': input_names, 
        'times': times,
        'tasks': tasks,
        })
