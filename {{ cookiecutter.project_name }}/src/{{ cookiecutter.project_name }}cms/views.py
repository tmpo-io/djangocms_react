#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.views.generic import ListView, DetailView


'''
class NoticiaDetail(DetailView):
    template_name = 'noticia_detail.html'
    model = Noticia

    def get_context_data(self, **kwargs):
        context = super(NoticiaDetail, self).get_context_data(**kwargs)
        context['latest'] = Noticia.objects.filter(status='public')
        return context


class NoticiaListView(ListView):
    template_name = 'noticies_list.html'
    model = Noticia

    def get_queryset(self):
        return Noticia.objects.filter(status='public')
'''
