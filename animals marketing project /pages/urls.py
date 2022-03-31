from django.urls import path
from .views import (
    HomePageView,
    MainPageView,
    AnimalPageView,
    AnimalfeedPageView,
    AnimalmedicinePageView,
    
    CattleUploadView,
    CattleListView,
    CattleDeleteView,
    CattleUpdateView,
    SearchPageView,

    GoatPageView,
    GoatSearchPageView,
    GoatDeleteView,
    GoatUpdateView,
    GoatUploadView,

    MachineryUploadView,
    MachineryPageView,
    ToolSearchPageView,
    MachineryDeleteView,
    MachineryUpdateView,
)
from django.conf import settings
from django.conf.urls.static import static

# from . import views

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('main',MainPageView.as_view(),name='main'),
    path('animals',AnimalPageView.as_view(),name='animals'),
    path('search',SearchPageView.as_view(),name='search'),
    path('cattle/list/',CattleListView.as_view(), name='cattle_list'),
    path('cattle/upload/',CattleUploadView.as_view(),name='cattle_upload'),
    path('<int:pk>/edit/',CattleUpdateView.as_view(), name='cattle_edit'),
    path('<int:pk>/delete/',CattleDeleteView.as_view(), name='cattle_delete'),

    path('goat/search',GoatSearchPageView.as_view(),name='goat_search'),
    path('goat',GoatPageView.as_view(),name='goat_list'),
    path('goat/upload/',GoatUploadView.as_view(),name='goat_upload'),
    path('<int:pk>/updategoat/',GoatUpdateView.as_view(),name='goat_edit'),
    path('<int:pk>/deletegoat/',GoatDeleteView.as_view(),name='goat_delete'),


    path('tools/search',ToolSearchPageView.as_view(),name='tool_search'),
    path('machinery',MachineryPageView.as_view(),name='machinery'),
    path('machinery/upload/',MachineryUploadView.as_view(),name='machinery_upload'),
    path('<int:pk>/updatemachine/',MachineryUpdateView.as_view(),name='machinery_edit'),
    path('<int:pk>/deletemachine/',MachineryDeleteView.as_view(),name='machinery_delete'),

    path('animalfeed',AnimalfeedPageView.as_view(),name='animalfeed'),
    path('animalmedicine',AnimalmedicinePageView.as_view,name='animalmedicine'),

    #path('<int:pk>/',CattleDetailView.as_view(), name='cattle_detail'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)