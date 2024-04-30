from django import template
register = template.Library()
# Dictionary to map programming languages to colors
language_colors = {
    'python': 'pink',
    'java': 'blue',
    'javascript': 'yellow',
    'ruby': 'red',
    'c++': 'purple'
}
@register.filter(name='colorize_language')
def colorize_language(value):
    language = value.lower()
    color = language_colors.get(language, 'black')
    colorize_language = f'<span style="color : {color}">{value}</span>'
    return colorize_language