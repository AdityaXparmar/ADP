from django import template
import re

register = template.Library()

@register.filter(name='highlight')
def highlight(text, query):
    if not query:
        return text

    pattern = re.compile(f'({re.escape(query)})', re.IGNORECASE)
    return pattern.sub(r'<mark>\1</mark>', text)