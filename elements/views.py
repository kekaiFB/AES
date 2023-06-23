from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import *
from django.db.models import Prefetch

# ---------------------------------Главная----------------------
class ElementsView(TemplateView):
    template_name = 'elements/elements_list.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        title = 'Главная'
        
        # elements = Element.objects.select_related().prefetch_related('files', 'images')
        # for elem in elements:
        #     print(elem)
        tab = Tab.objects.prefetch_related('elements', 'elements__files', 'elements__images')
       
        context['tab'] = tab

        return context