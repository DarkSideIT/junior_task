from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.shortcuts import get_object_or_404
import json
from robots.models import Robot
import datetime



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
                robot = None


            if robot is None:
                robot = Robot(model=model, version=version, created=(datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S'), is_available=False)
                robot.save()
            else:
                return JsonResponse({'message': 'this robot already exists'})

            return JsonResponse({'success': 'Order placed successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'})

@method_decorator(csrf_exempt, name='dispatch')
def update_robot_availability_api(request, robot_id):
    try:
        robot = get_object_or_404(Robot, id=robot_id)
        if request.method == 'POST':
            data = json.loads(request.body)
            is_available = data.get('is_available')
            if is_available is not None:
                robot.is_available = bool(int(is_available))
                robot.save()
                return JsonResponse({'success': 'Availability updated successfully'})
            else:
                return JsonResponse({'error': 'Invalid data. is_available field is required'})
        else:
            return JsonResponse({'error': 'Invalid request method. Use POST to update availability.'})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    except:
        pass
