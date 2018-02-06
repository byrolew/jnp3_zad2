from django.db import models

class Task(models.Model):
    content_1 = models.TextField()
    content_2 = models.TextField()
    Q = models.TextField()
    nQ = models.TextField()
    P = models.TextField()
    nP = models.TextField()
    rule = models.TextField()
    instruction = models.TextField()
    my_id = models.IntegerField()
        

class Experiment(models.Model):
    username = models.CharField(max_length=256, blank=True, null=True)
    is_male = models.NullBooleanField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    mode = models.IntegerField()
    time_to_red = models.IntegerField()
    time_train_gil = models.IntegerField()
    time_test_gil = models.IntegerField()
    time_train_cards = models.IntegerField()
    welcome = models.TextField()
    instr_gil = models.TextField()
    instr_cards = models.TextField()
    instr_test_gil = models.TextField()


class Event(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=True)
    type_of_event = models.CharField(max_length=256)
    time = models.FloatField()
    trial = models.BooleanField()
    task = models.ForeignKey('TaskRandom', on_delete=True, blank=True, null=True)


class TaskRandom(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=True)
    task = models.ForeignKey('Task', on_delete=False)
    is_done = models.BooleanField(default=0)
    trial = models.BooleanField()