from django.urls import path
from . import views

app_name = 'noteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('note/', views.note, name='note'),
    path('tag/', views.tag, name='tag'),
    path('detail/<int:note_id>/', views.detail, name='detail'),
    path('done/<int:note_id>', views.set_done, name='set_done'),
    path('delete/<int:note_id>', views.delete_note, name='delete'),
    path('edit/<int:note_id>', views.edit_note, name='edit'),
    path('notes/alldone/', views.all_done, name='all_done'),
    path('notes/allnotdone/', views.all_notdone, name='all_notdone'),
    path('notes/all/', views.all_notes, name='all_notes'),
    path('tags/', views.all_tags, name='all_tags'),
    path('tags/<int:tag_id>/edit/', views.edit_tag, name='edit_tag'),
    path('tags/<int:tag_id>/delete/', views.delete_tag, name='delete_tag'),
]
