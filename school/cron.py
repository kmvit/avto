from school.models import School
from datetime import date, timedelta


def my_scheduled_job():
    school_list = School.objects.filter(premium=True)
    for school in school_list:
        if school.date_off_premium == date.today():
            school.premium = False
            school.save()
      
                
        