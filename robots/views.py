from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Robot


@method_decorator(csrf_exempt, name='dispatch')
class CreateRobotView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            model = data.get('model')
            version = data.get('version')
            created = data.get('created')


            if not model or not version or not created:
                return JsonResponse({'error': 'Invalid data. All fields are required'})
            

            serial = f"{model}-{version}"
            

            robot = Robot(serial = serial,
                        model = model,
                          version = version,
                          created = created)
            robot.save()


            return JsonResponse({'success': 'Robot created successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'})

# Create your views here.
