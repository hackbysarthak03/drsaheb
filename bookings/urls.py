from django.urls import path
from . import views

urlpatterns = [
    path('book/<slug>', views.bookDoctor),
    path('invite/<id>', views.invite),
    path('checkup-done/<id>', views.checkUp),
    path('download/<id>', views.generate_pdf),
]
