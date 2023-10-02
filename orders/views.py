from django.shortcuts import render
from django.http import HttpResponse
from openpyxl import Workbook
from datetime import datetime, timedelta
from robots.models import Robot


def download_excel(request):
    end_date = datetime.now()
    start_date = end_date - timedelta(7)


    wb = Workbook()


    robots_data = Robot.objects.filter(created__gte=start_date, created__lte=end_date).values('model').distinct()


    for robot in robots_data:
        model = robot['model']
        ws = wb.create_sheet(title=model)
        ws.append(["Model", "Version", "The Amount Per Week"])


        robot_versions = Robot.objects.filter(model=model, created__gte=start_date, created__lte=end_date, is_available=True).values('version').distinct()


        for robot_version in robot_versions:
            version = robot_version['version']


            weekly_count = Robot.objects.filter(
                model=model,
                version = version,
                created__gte = start_date,
                created__lte = end_date
            ).count()


            ws.append([model, version, weekly_count])
    
    del wb['Sheet']


    response = HttpResponse(content_type = "application/ms-excel")
    response["Content-Disposition"] = "attachment; filename=robot_summary.xlsx"
    wb.save(response)


    return response