from instructors.models import Instructor
from datetime import date, timedelta


def my_scheduled_job_instructor():
    instructor_list = Instructor.objects.filter(premium=True)
    for instructor in instructor_list:
        if instructor.date_off_premium == date.today():
            instructor.premium = False
            instructor.save()
      
                
        