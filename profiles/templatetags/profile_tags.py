from django import template
from django_geoip.models import IpRange
from profiles.models import Social
from city.models import Town
import codecs

register = template.Library()
@register.inclusion_tag('city.html', takes_context=True)
def city_name(context):
    request = context['request']
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        geoip_record = IpRange.objects.by_ip(ip)
        city = geoip_record.city
        country = geoip_record.country
        context_dict = {'city':city, 'city_id': city.id}
        return context_dict
    except IpRange.DoesNotExist:
        context_dict = {'ip':ip }
        return context_dict
        

@register.inclusion_tag('city_id.html', takes_context=True)
def city_id(context):
    request = context['request']
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        geoip_record = IpRange.objects.by_ip(ip)
        city = geoip_record.city
        city = str(city)
        city=codecs.decode(city, 'utf-8')
        for item in Town.objects.all():
            if city == item.title:
                context_dict = {'city':city, 'city_id': item.id}
                return context_dict
    except IpRange.DoesNotExist:
        context_dict = {'ip':ip }
        return context_dict
        
@register.inclusion_tag('profiles/social_links.html', takes_context=True)
def social_links(context):
    request = context['request']
    social = Social.objects.all()
    context_dict = {'social':social}
    return context_dict
    