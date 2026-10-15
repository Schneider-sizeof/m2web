import re
from django import template
from django.urls import translate_url

register = template.Library()

BASE_CANONICAL_DOMAIN = "https://m2webmaroc.com"

@register.simple_tag(takes_context=True)
def get_canonical_url(context):
    """
    Returns the normalized canonical URL for the current request.
    Always forces https://m2webmaroc.com without query strings.
    """
    request = context.get('request')
    if not request:
        return f"{BASE_CANONICAL_DOMAIN}/fr/"

    path = request.path or '/'
    if not path.startswith('/'):
        path = '/' + path

    # If hitting bare root, canonical points to default language
    if path == '/':
        path = '/fr/'

    return f"{BASE_CANONICAL_DOMAIN}{path}"


@register.simple_tag(takes_context=True)
def get_hreflang_url(context, language_code):
    """
    Returns the valid alternate hreflang URL for a given language code.
    Fixes double-prefix bugs by translating the path or replacing the language code cleanly.
    """
    request = context.get('request')
    if not request:
        return f"{BASE_CANONICAL_DOMAIN}/{language_code}/"

    path = request.path or '/'
    if not path.startswith('/'):
        path = '/' + path

    # Try Django's built-in translate_url
    translated = translate_url(path, language_code)
    if translated and translated != path and translated.startswith(f"/{language_code}/"):
        return f"{BASE_CANONICAL_DOMAIN}{translated}"

    # Robust regex fallback for i18n_patterns with prefix_default_language=True
    if re.match(r"^/(fr|ar|en)(/.*)?$", path):
        translated = re.sub(r"^/(fr|ar|en)", f"/{language_code}", path)
        return f"{BASE_CANONICAL_DOMAIN}{translated}"

    return f"{BASE_CANONICAL_DOMAIN}/{language_code}/"
