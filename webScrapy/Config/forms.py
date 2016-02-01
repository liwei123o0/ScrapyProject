# -*- coding: utf-8 -*-
#! /usr/bin/env python
from django import forms

class PdForm(forms.Form):

    name=forms.IntegerField()