from django import template

register = template.Library()

CENSOR_WORD= ['Спорт', 'темы', 'пломбы']

@register.filter()
def censor(value):
    for word in CENSOR_WORD:
        value.replace(word[1:],'*' *len(word[1:]))
        return value

