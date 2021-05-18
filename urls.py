from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns=[
   path('base/',views.home),
   path('home/',views.insert_user_info,name='insert_user_info'),
   path('apartment/',views.insert_Apartment_info,name='insert_Apartment_info'),
   path('flats_info/', views.show_flats,name='show_flats'),
   path('flats_infojson/', views.show_flatsInJson,name='show_flatsInJson')

]


"""

JSON:
QUERY: allapartmentslist = Apartments.obj.get(user_id = id)
[{

"user_id": 1,
"user_name": "Faiyaz",
"user_apartment_list": [flast1,flat2,flat3]


},
{

"user_id": 2,
"user_name": "riad",
"user_apartment_list": [flast1,flat2,flat3]



}
...
..
..
.
.

]


"""