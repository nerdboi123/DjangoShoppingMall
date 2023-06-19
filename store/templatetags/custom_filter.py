from django import template

register = template.Library()
#값이 int로 들어오면 str으로 바꿔줌
@register.filter(name='currency')
def currency(number):
    return "$"+str(number)



@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

