from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from DurgaTemp_Calculator.models import History


# Create your views here.

@login_required(login_url='account/login/')
def temperature_converter(request):
    return render(request, 'home/index.html')

def my_404_view(request, exception):
    return render(request, 'home/404.html')

@login_required(login_url='account/login/')
def convert_temperature(request):
    temperature = request.GET.get('temperature', '0')
    from_unit = request.GET.get('from_unit')
    to_unit = request.GET.get('to_unit')

    try:
        temperature = float(temperature)
    except ValueError:
        return JsonResponse({'error': 'Invalid temperature value'})

    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            converted = (temperature * 9/5) + 32
        elif to_unit == 'kelvin':
            converted = temperature + 273.15
        else:
            converted = temperature
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            converted = (temperature - 32) * 5/9
        elif to_unit == 'kelvin':
            converted = (temperature + 459.67) * 5 / 9
        else:
            converted = temperature
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            converted = temperature - 273.15
        elif to_unit == 'fahrenheit':
            converted = (temperature * 1.8) - 459.67
        else:
           converted = temperature
    else:
        return JsonResponse({'error': 'Invalid source unit'})

    conversion_history_result = History(
        User = request.user,
        temperature = temperature,
        from_unit = from_unit,
        to_unit = to_unit,
        converted = converted
    )
    conversion_history_result.save()

    return JsonResponse({'converted': round(converted, 0)})

@login_required(login_url='account/login/')
def conversion_history(request):
    conversion_history_results = History.objects.all()

    conversion_history_results = History.objects.filter(
        User = request.user,
        temperature__isnull=False,
        from_unit__isnull=False,
        to_unit__isnull=False,
    )

    for conversion_history_result in conversion_history_results:
        existing_conversion_history_results = History.objects.filter(
            User=conversion_history_result.User,
            temperature=conversion_history_result.temperature,
            from_unit=conversion_history_result.from_unit,
            to_unit=conversion_history_result.to_unit
        )

        if len(existing_conversion_history_results) > 1:
            conversion_history_result.delete()
            return redirect('home:history')

    return render(request, 'home/history.html', {
        'conversion_history_results': conversion_history_results
    })

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        if password2 == password:
            new_user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            new_user.save()
            return redirect('home:login')

    if request.user.is_authenticated:
        return redirect('home:temperature_converter')    

    return render(request, 'account/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect('home:temperature_converter')

    if request.user.is_authenticated:
        return redirect('home:temperature_converter')

    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('home:login')

@login_required(login_url='account/login/')
def delete(request, id):
    remove_item = History.objects.get(id=id, User=request.user)  
    if request.method == 'POST':
        remove_item.delete()
        return redirect('home:history')    
    else:
        return render(request, 'home/delete.html', {'remove_item': remove_item})

  

@login_required(login_url='account/login/')
def delete_all(request):
    if request.method == 'GET':  
        history = History.objects.all()
        conversion_history = history.filter(User=request.user)
        if conversion_history:
            conversion_history.delete()
            return redirect('home:history')    
        return render(request, 'home/delete_all.html', {'history':history, 'conversion_history':conversion_history})
