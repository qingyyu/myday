# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import *
# from django.db import models
# from djangotoolbox.fields import ListField, EmbeddedModelField

# Create your models here.
connect('myday')
class Slot(EmbeddedDocument):
    start_time = DateTimeField()
    end_time = DateTimeField()
    task = StringField(max_length=256)
# class T(Document):
#    t= StringField() 
class Note(EmbeddedDocument):
    tag = ListField()
    project = ListField()
    content = StringField()

class Todo(EmbeddedDocument):
    project = StringField()
    task = StringField()
    isToday = IntField()

class Day(EmbeddedDocument):
    tag = ListField()
    date = StringField()
    slot = ListField(EmbeddedDocumentField('Slot'))
    note = ListField(EmbeddedDocumentField('Note'))
    todo = ListField(EmbeddedDocumentField('Todo'))
    def __str__(self):
        return self.date    

class User(Document):
    username = StringField(max_length=256)
    day = ListField(EmbeddedDocumentField('Day'))
    def __str__(self):
        return self.username

