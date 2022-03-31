from django import forms
from .models import Cattle,CattleSex,Machinery,Goat

class GoatForm(forms.ModelForm):
    class Meta:
        model=Goat
        fields=('owner_contact','breed','weight','maximum_selling_price','location','goat_age','goat_sex_based_on','health_record_book','goat_picture')
    def __init__(self,*args,**kwargs,): 
        super(GoatForm,self).__init__(*args,**kwargs)
        self.fields['goat_sex_based_on'].empty_label='select'


class CattleForm(forms.ModelForm):
    class Meta:
        model=Cattle
        fields=('owner_contact','breed','weight','selling_price_range','location','cattle_age','cattle_sex_based_on','health_record_book','cattle_picture')
        # fields='__all__'
        labels={
            'selling_price_range':'Maximum Selling Price',
            'cattle_age':'Cattle Age In Years',
            'weight':'Weight In Kilograms',
            'location':'County Location',
            'cattle_sex_based_on':'Cattle Age & Sex Based On',
        }
    def __init__(self,*args,**kwargs,): 
        super(CattleForm,self).__init__(*args,**kwargs)
        self.fields['cattle_sex_based_on'].empty_label='select'

class MachineryForm(forms.ModelForm):
    class Meta:
        model=Machinery
        fields=('owner_contact','tool_name','brief_its_usage','location','tools_number','maximum_selling_price','tool_purpose','animal_type','animals_type','machinery_tool_picture')
        labels={
            'tool_name':'Machinery, Tool or Equipment Name',
            'location':'County Location',
            'tool_purpose':'Tool & Equipment Purpose Base On',
            'animal_type':'Specify Animal Type To Be Used On',
            'animals_type':'Type Other Animal Type Not In List',
            'machinery_tool_picture':'Machinery, Tool & Equipment Picture'
        }
    def __init__(self,*args,**kwargs,): 
        super(MachineryForm,self).__init__(*args,**kwargs)
        self.fields['tool_purpose'].empty_label='select'




