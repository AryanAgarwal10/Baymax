from django.urls import path
from .views import AIView


urlpatterns = [
    path('', AIView.as_view())
    # path('<int:id>', ContactDetailView.as_view(),name='get_contact'),
    # path('search/name/<str:name>', ContactNameSearchView.as_view()),
    # path('search/phone/<int:phone>', ContactPhoneSearchView.as_view()),
]
