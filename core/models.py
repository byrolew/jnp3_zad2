from django.db import models


class Experiment(models.Model):
    username = models.CharField(max_length=256, blank=True, null=True)
    feedback = models.BooleanField()
    all_buttons = models.BooleanField()
    lighting_time = models.IntegerField(default=0)
    interval_time = models.IntegerField(default=0)
    session_time = models.IntegerField(default=0)
    is_trial = models.BooleanField()

    def __str__(self):
        return self.username


class Sequence(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=True)
    seq_id = models.IntegerField()
    is_done = models.BooleanField(default=0)
    trial = models.BooleanField()

    def __str__(self):
        return self.experiment.username + ' ' + str(self.seq_id)


class Session(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=True)
    time_spent = models.IntegerField(default=0)
    first_ts = models.FloatField(default=0)
    last_ts = models.FloatField(default=0)


class Event(models.Model):
    session = models.ForeignKey('Session', on_delete=True)
    sequence = models.ForeignKey('Sequence', on_delete=True)
    timestamp = models.FloatField()
    event_type = models.CharField(max_length=16)

    def __str__(self):
        return 'ET: {}, SEQ_ID: {}'.format(self.event_type , self.sequence.seq_id)
