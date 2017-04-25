from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import inspection, inspectionItemStatus, inspectionItemDetail, priorityLevel, restaurant
from .forms import searchForm, inspectionForm, inspectionItemStatusForm, inspectionItemDetailForm, priorityLevelForm, restaurantForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
import operator

# def results(request):
#     if request.method == 'GET':
#         if request.GET.get('searchQuery'):
#             message = 'You submitted: %r' % request.GET['searchQuery']
#         else:
#             message = 'You submitted nothing!'
#         return HttpResponse(message)
def results(request):
    if restaurant.objects.filter(name__icontains='Mar'):
        print("There is at least one Entry with the headline Test")
    restaurants = restaurant.objects.get(name__icontains='Mar')
    print("There is at least one Entry with the headline Testgagagasgjaslkdfjaklsdjfklasjdf")
    return render(request, 'results.html', {'restaurants': restaurants})

def index(request):
    current_restaurant_list = restaurant.objects.order_by('-name')[:5]
    template = loader.get_template('fvi/index.html')
    context = {
        'current_restaurant_list': current_restaurant_list,
    }
    # if request.method == 'GET':
    #     if 'searchQuery' in request.GET:
    #         message = 'You submitted: %r' % request.GET['']
    #     else:
    #         message = 'You submitted nothing!'
    #
    #     return HttpResponse(message)
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     print("hello")
    mySearchForm = searchForm()
    return render(request, 'fvi/index.html', {'form': mySearchForm})
    # return HttpResponse(template.render(context, request))
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
class inspectionListView(ListView):
    model = inspection
class inspectionCreateView(CreateView):
    model = inspection
    form_class = inspectionForm
class inspectionDetailView(DetailView):
    model = inspection
class inspectionUpdateView(UpdateView):
    model = inspection
    form_class = inspectionForm
class inspectionItemStatusListView(ListView):
    model = inspectionItemStatus
class inspectionItemStatusCreateView(CreateView):
    model = inspectionItemStatus
    form_class = inspectionItemStatusForm
class inspectionItemStatusDetailView(DetailView):
    model = inspectionItemStatus
class inspectionItemStatusUpdateView(UpdateView):
    model = inspectionItemStatus
    form_class = inspectionItemStatusForm
class inspectionItemDetailListView(ListView):
    model = inspectionItemDetail
class inspectionItemDetailCreateView(CreateView):
    model = inspectionItemDetail
    form_class = inspectionItemDetailForm
class inspectionItemDetailDetailView(DetailView):
    model = inspectionItemDetail
class inspectionItemDetailUpdateView(UpdateView):
    model = inspectionItemDetail
    form_class = inspectionItemDetailForm
class priorityLevelListView(ListView):
    model = priorityLevel
class priorityLevelCreateView(CreateView):
    model = priorityLevel
    form_class = priorityLevelForm
class priorityLevelDetailView(DetailView):
    model = priorityLevel
class priorityLevelUpdateView(UpdateView):
    model = priorityLevel
    form_class = priorityLevelForm
class restaurantListView(ListView):
    model = restaurant
    template_name = 'fvi/restaurant_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'restaurants'  # Default: object_list
    paginate_by = 3
    queryset = restaurant.objects.all()  # Default: Model.objects.all()
class restaurantCreateView(CreateView):
    model = restaurant
    form_class = restaurantForm
class restaurantDetailView(DetailView):
    model = restaurant
class restaurantUpdateView(UpdateView):
    model = restaurant
    form_class = restaurantForm
