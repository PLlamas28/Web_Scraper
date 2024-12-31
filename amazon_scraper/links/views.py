from django.shortcuts import render, redirect
from .forms import AddLinkForm
from .models import Link
from django.http import HttpResponseRedirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# Create your views here.

def home_view(request):
    num_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)
    
    if request.method =='POST':
        try:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('home-view'))
        except AttributeError:
            error = "Couldn't get name or price"
        except:
            error = "An error occurred"

    form = AddLinkForm()


    qs = Link.objects.all()
    items_num = qs.count()
    if items_num > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            num_discounted = len(discount_list)


    context = {
        'qs' : qs,
        'items_num':items_num,
        'num_discounted' : num_discounted,
        'form' : form,
        'error' : error,

    }

    return render(request, 'links/templates/main.html', context)
    

class LinkDeleteView(DeleteView):
    model = Link
    template_name = "links/templates/conf_del.html"
    success_url = reverse_lazy('home_view')


def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home_view')
