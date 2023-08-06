from django.urls import path
from . import  views
urlpatterns=[
    path('',views.home,name='home'),
    path('linear_search',views.linear_search,name='linear_search'),
    path('binary_search',views.binary_search,name='binary_search'),
    path('insertion_sort',views.insertion_sort,name='insertion_sort'),
    path('bubble_sort',views.bubble_sort,name='bubble_sort'),
    path('merge_sort',views.merge_sort,name='merge_sort'),
    path('selection_sort',views.selection_sort,name='selection_sort'),
    path('quick_sort',views.quick_sort,name='quick_sort'),
    path('heap_sort',views.heap_sort,name='heap_sort'),
    path('merge_vis', views.merge_vis, name='merge_vis'),
    path('selection_vis', views.selection_vis, name='selection_vis'),
    path('bubble_vis', views.bubble_vis, name='bubble_vis'),
    path('quick_vis', views.quick_vis, name='quick_vis'),
]

 