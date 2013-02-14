"""
Wrapper class that takes a list of template loaders as an argument and attempts
to load alternative templates from them in order.
"""

import hashlib
import re

from django.template.base import TemplateDoesNotExist
from django.template.loader import BaseLoader, find_template_loader, make_origin
from django.utils.translation import get_language_info, get_language

def generate_rtl_template_name(template_name):
    """
    Generates an alternative template name by appending
    _rtl to the file name before the extension.
    
    Note, this assumes the template name has at least one dot.
    
    Example: 
        >>> generate_rtl_template_name('test.html')
        'test_rtl.html;
    """
    regex = re.compile(r'(.*)\.+(.*)')
    return regex.sub(r'\1_rtl.\2', template_name)


class Loader(BaseLoader):
    is_usable = True

    def __init__(self, loaders):
        self._loaders = []
        for loader in loaders:
            self._loaders.append(find_template_loader(loader))

    def load_template(self, template_name, template_dirs=None):
        language_info = get_language_info(get_language())
        if language_info['bidi']:
            return self.load_rtl_template(template_name, template_dirs)
        
        for loader in self._loaders:
            try:
                template, display_name = loader(template_name, template_dirs)
                return (template, make_origin(display_name, loader, template_name, template_dirs))
            except TemplateDoesNotExist:
                pass
        raise TemplateDoesNotExist(template_name)

    def load_rtl_template(self, template_name, template_dirs=None):
        rtl_template_name = generate_rtl_template_name(template_name)
        for loader in self._loaders:
            try:
                template, display_name = loader(rtl_template_name, template_dirs)
                return (template, make_origin(display_name, loader, rtl_template_name, template_dirs))
            except TemplateDoesNotExist:
                try:
                    template, display_name = loader(template_name, template_dirs)
                    return (template, make_origin(display_name, loader, template_name, template_dirs))
                except TemplateDoesNotExist:
                    pass
        raise TemplateDoesNotExist(template_name)