from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from . models import User, Apartments
from .serializers import showApartmentDetails
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


def home(request):
    return render(request, 'ourproject/home.html')


def insert_user_info(request):
  #  AppartmentId=User(request.GET['apartment_id'])
    UserInfo = User(first_name=request.POST.get('FirstName'), last_name=request.POST.get(
        'LastName'), phone_number=request.POST.get('PhoneNumber'), user_type=request.POST.get('UserType'))
    UserInfo.save()

    return HttpResponse("Congratulations!You are successfully registered to Nagorik Seba")


def insert_Apartment_info(request):
  if request.method == 'POST':
    ApartmentInfo = Apartments(flat_number=request.POST.get('FlatNumber'), building_name=request.POST.get('BuildingName'), building_number=request.POST.get('BuildingNumber'), building_address=request.POST.get('BuildingAddress'), flat_size=request.POST.get(
    'FlatSize'), num_of_beds=request.POST.get('NumOfBeds'), num_of_toilet=request.POST.get('NumOfToilet'), num_of_balcony=request.POST.get('NumOfBalcony'), map_address=request.POST.get('MapAddress'), location=request.POST.get('Location'))
    ApartmentInfo.save()
    return HttpResponse("Your Apartment Profile is updated")
  else:
    return render(request, 'ourproject/apartment.html')

def show_flats(request):
  if request.method=='POST':
      # location_search=request.POST.get('location')
      # ampobj=Apartments.objects.filter(location=request.post.get('location')
      location=Apartments.objects.filter(location=request.POST['location'])
      contxt = { 'Flats' : location } 
      return render(request,'flats_info.html', contxt)
  else:
      flats_info=Apartments.objects.all()
      print=flats_info
      return render(request, "ourproject/flats_info.html", {'Flats': flats_info})

@api_view(['POST'])
def show_flatsInJson(request):
  allapartments=Apartments.objects.all()
  serializer = showApartmentDetails(allapartments, many=True)
  return JsonResponse(serializer.data, safe=False)


"""def search_by_location(request):
  
  else:
    location=Apartments.objects.filter(location=request.post.get('location'))
    contxt = { 'location_search' : location }
    return render(request,'flats_info.html', contxt)"""



