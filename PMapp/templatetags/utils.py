from django import template
import math
 
register = template.Library()
 
@register.filter(name="MenuEx1")
def MenuEx1(dist, time):
    return (str(math.floor(time / dist * 100)) + "min" + str(math.floor((time / dist * 100) % 1 * 60)) + "sec")

@register.filter(name="MenuEx2")
def MenuEx2(dist, time):
    return (dist/1000) / (time/60)

@register.filter(name="MenuEx3")
def MenuEx3(dist, time):
    return (str(math.floor(time / dist * 1000)) + "min" + str(math.floor((time / dist * 1000) % 1 * 60)) + "sec")
