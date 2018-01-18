import random

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import (
    Experiment, 
    Sequence, 
    Session, 
    Event,
)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        if username == 'admin':
            return redirect('panel_admin')
        else:
            experiment = get_object_or_404(Experiment, username=username)
            return redirect('desc')
    else:
        return render(request, 'core/login.html', {})

def form1(request):
    if request.method == 'POST':
        feedback = bool(int(request.POST.get('feedback')))
        all_buttons = bool(int(request.POST.get('all_buttons')))

        experiment = Experiment.objects.create(
            feedback=feedback,
            all_buttons=all_buttons,
            is_trial=True,
        )
        experiment.save()

        return redirect('form2')
    
    else:
        return render(request, 'core/form1.html', {})

def form2(request):
    if request.method == 'POST':
        # create experiment
        experiment = Experiment.objects.filter(username=request.POST.get('username'))
        if len(experiment) > 0:
            raise ValueError('There is such experiment! Use different name.')

        experiment = Experiment.objects.latest('pk')
        experiment.lighting_time = int(request.POST.get('lighting_time'))
        experiment.interval_time = int(request.POST.get('interval_time'))
        experiment.session_time = 60*1000*int(request.POST.get('session_time'))
        experiment.username = request.POST.get('username')
        experiment.save()

        # create sequences
        seq_ids = list(range(1, 1024))
        random.shuffle(seq_ids)
        seq = []
        for seq_id in seq_ids:
            seq.append(
                Sequence(
                    experiment=experiment,
                    seq_id=seq_id,
                    trial=False,
                ),
            )

        n_trials = 5
        for seq_id in random.sample(seq_ids, n_trials):
            seq.append(
                Sequence(
                    experiment=experiment,
                    seq_id=seq_id,
                    trial=True,
                ),
            )

        Sequence.objects.bulk_create(seq)

        # create session
        new_session = Session(experiment=experiment)
        new_session.save()

        return redirect('login_page')
    
    else:
        return render(request, 'core/form2.html', {})

def desc(request):
    experiment = Experiment.objects.latest('pk')
    return render(request, 'core/desc.html', {'exp': experiment})

def end_trial(request):
    return render(request, 'core/end_trial.html', {})

def experiment_page(request):
    session = Session.objects.latest('pk')
    experiment = Experiment.objects.latest('pk')

    if request.method == 'POST':
        # update sequence

        prev_seq_pk = request.POST.get('prev_seq_pk')
        prev_seq = Sequence.objects.get(pk=prev_seq_pk)
        prev_seq.is_done = True
        prev_seq.save()

        # update events
        for name, ts in request.POST.items():
            if not name.startswith('event_'):
                continue

            new_event = Event.objects.create(
                sequence=prev_seq,
                session=session,
                timestamp=ts,
                event_type=name.split('_')[-1],
            )
            new_event.save()

        # update session
        all_ts = [ts for name, ts in request.POST.items() if name.startswith('event_')]
        time_spent = float(request.POST.get('time_spent'))
        session.time_spent += time_spent
        session.last_ts = max(all_ts)
        if session.first_ts == 0:
            session.first_ts = min(all_ts)
        session.save()

        if session.time_spent > experiment.session_time:
            session = Session.objects.create(experiment=experiment)
            return redirect('end_of_session')

    try:
        sequence = Sequence.objects.filter(experiment=experiment, is_done=False).order_by('-trial')[0]
    except IndexError:
        return redirect('end')

    trials_left = len(Sequence.objects.filter(trial=True, is_done=False))
    if trials_left == 0 and experiment.is_trial:
        experiment.is_trial = False
        experiment.save()
        return redirect('end_trial')

    seq_id_bin = '{0:b}'.format(sequence.seq_id)
    seq_id_bin = '0'*(10-len(seq_id_bin))+seq_id_bin
    seq_id_bin = ['on' if bool(int(c)) else 'off' for c in seq_id_bin]

    return render(
        request, 
        'core/experiment.html', 
        {
            'exp': experiment, 
            'seq': seq_id_bin, 
            'seq_pk':sequence.pk,
        },
    )

def end_of_session(request):
    return render(request, 'core/end_of_session.html', {})

def end(request):
    return render(request, 'core/end.html', {})

def reset(request):
    Experiment.objects.all().delete()

def report(request):
    exp = Experiment.objects.latest('pk')
    events = Event.objects.filter(session__experiment=exp)
    results = ['event_type,timestamp,username,time_spent,first_ts,last_ts,seq_id,trial']
    for e in events:
        results.append(','.join(map(str, [
            e.event_type,
            e.timestamp,
            e.session.experiment.username,
            e.session.time_spent,
            e.session.first_ts,
            e.session.last_ts,
            e.sequence.seq_id,
            e.sequence.trial,
        ])))

    return HttpResponse('\n'.join(results))

def panel_admin(request):
    return render(request, 'core/panel_admin.html', {})

