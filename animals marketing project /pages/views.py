
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CattleForm,MachineryForm,GoatForm
from .models import Cattle,Machinery,Goat
from datetime import datetime
from django.db.models import Q


# Create your views here.

class HomePageView(TemplateView):
    template_name='home.html'

class MainPageView(LoginRequiredMixin, TemplateView):
    template_name='main.html'
    login_url = 'login'


class AnimalPageView(LoginRequiredMixin,TemplateView):
    template_name='main.html'
    login_url = 'login'
    #FOR CATTLE
class CattleListView(LoginRequiredMixin,ListView):
    model=Cattle
    template_name='animalstemplates/cattle_list.html'
    login_url = 'login'
class SearchPageView(LoginRequiredMixin,ListView):
    model=Cattle
    template_name='animalstemplates/search.html'
    def get_queryset(self):
        querry=self.request.GET.get('search')
        object_list=Cattle.objects.filter(
            Q(weight__icontains=querry) | Q(breed__icontains=querry) | Q(location__icontains=querry) | Q(cattle_age__icontains=querry) | Q(selling_price_range__icontains=querry) 
            )
        return object_list
    login_url = 'login'
class CattleUpdateView(LoginRequiredMixin,UpdateView):
    model=Cattle
    # fields='__all__'
    form_class=CattleForm
    success_url=reverse_lazy('cattle_list')
    template_name='animalstemplates/cattle_edit.html'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class CattleDeleteView(LoginRequiredMixin,DeleteView):
    model=Cattle
    success_url=reverse_lazy('cattle_list')
    template_name='animalstemplates/cattle_delete.html'   
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class CattleUploadView(LoginRequiredMixin,CreateView):
    day = datetime.now().time()
    {'day':day}
    model=Cattle
    form=CattleForm
    form_class=CattleForm
    # fields=('owner_contact','breed','weight','selling_price_range','location','cattle_age','cattle_sex_based_on','health_record_book','cattle_picture')
    success_url=reverse_lazy('cattle_list')
    template_name='animalstemplates/cattle_upload.html'
    def form_valid(self, form): 
        form.instance.owner_name = self.request.user
        return super().form_valid(form)


    #for goat
class GoatPageView(LoginRequiredMixin, ListView):
    model=Goat
    template_name='goat/goat.html'
    login_url = 'login'
class GoatSearchPageView(ListView):
    model=Goat
    template_name='goat/goat_search.html'
    def get_queryset(self):
        goatsearch=self.request.GET.get('goatsearch')
        object_list=Goat.objects.filter(
            Q(location__icontains=goatsearch) | Q(breed__icontains=goatsearch) | Q(weight__icontains=goatsearch) | Q(goat_age__icontains=goatsearch) | Q(maximum_selling_price__icontains=goatsearch)
            )
        return object_list
class GoatDeleteView(DeleteView):
    model=Goat
    success_url=reverse_lazy('goat_list')
    template_name='goat/goat_delete.html'   
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class GoatUpdateView(UpdateView):
    model=Goat
    form_class=GoatForm
    success_url=reverse_lazy('goat_list')
    template_name='goat/goat_edit.html'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class GoatUploadView(CreateView):
    day = datetime.now().time()
    {'day':day}
    model=Goat
    form=GoatForm
    form_class=GoatForm
    # fields=('owner_contact','breed','weight','selling_price_range','location','cattle_age','cattle_sex_based_on','health_record_book','cattle_picture')
    success_url=reverse_lazy('goat_list')
    template_name='goat/goat_upload.html'
    def form_valid(self, form): 
        form.instance.owner_name = self.request.user
        return super().form_valid(form)



     #FOR ANIMALS MACHINES AND TOOLS
class MachineryPageView(LoginRequiredMixin,ListView):
    model=Machinery
    template_name='machinery/machinery.html'
    login_url = 'login'
class ToolSearchPageView(LoginRequiredMixin,ListView):
    model=Machinery
    template_name='machinery/machinery_search.html'
    def get_queryset(self):
        feedback=self.request.GET.get('feedback')
        object_list=Machinery.objects.filter(
            Q(location__icontains=feedback) | Q(tool_name__icontains=feedback) | Q(brief_its_usage__icontains=feedback) | Q(animals_type__icontains=feedback)
            )
        return object_list
    login_url = 'login'
class MachineryUploadView(LoginRequiredMixin,CreateView):
    day = datetime.now().time()
    {'day':day}
    model=Machinery
    form_class=MachineryForm
    success_url=reverse_lazy('machinery')
    template_name='machinery/machinery_upload.html'
    def form_valid(self, form): 
        form.instance.owner_name = self.request.user
        return super().form_valid(form)
class MachineryDeleteView(DeleteView):
    model=Machinery
    template_name='machinery/machinery_delete.html'
    success_url=reverse_lazy('machinery')
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
class MachineryUpdateView(UpdateView):
    model=Machinery
    form_class=MachineryForm
    template_name='machinery/machinery_edit.html'
    success_url=reverse_lazy('machinery')
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner_name != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class AnimalfeedPageView(ListView):
    template_name='animalfeed.html'

class AnimalmedicinePageView(ListView):
    template_name='animalmedicine.html'







    