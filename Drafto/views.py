from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def temperature_converter(request):
    return render(request, 'home/index.html')

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

    return JsonResponse({'converted': round(converted, 2)})