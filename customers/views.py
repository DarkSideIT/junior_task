from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from robots.models import Robot



@method_decorator(csrf_exempt, name='dispatch')
class OrderRobotView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            model = data.get('model')
            version = data.get('version')

            if not model or not version:
                return JsonResponse({'error': 'Invalid data. Model and version are required'})

            # Проверяем наличие робота по модели и версии
            try:
                robot = Robot.objects.get(model=model, version=version)
            except Robot.DoesNotExist:
                return JsonResponse({'error': 'Robot not found'})

            # Устанавливаем флаг is_available в True
            robot.is_available = True
            robot.save()

            return JsonResponse({'success': 'Order placed successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'})