from django.template.defaultfilters import register

@register.filter(name='get_key')
def dict_key(dictionary, key):
    '''Returns the given key from a dictionary.'''
    return dictionary[key]