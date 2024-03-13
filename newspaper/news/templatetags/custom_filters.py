from django import template

register = template.Library()

CENSOR_WORD= ['Спорт', 'социальных', 'пломбы']

@register.filter()
def censor(value):
    for word in CENSOR_WORD:
        value = value.replace(word[1:],'*' *len(word[1:]))
        return value

