from django.test import TestCase
from rtl.loaders import generate_rtl_template_name


class RighToLeftLoader(TestCase):

    def test_generates_correct_rtl_template_name_for_template_with_normal_file_extension(self):
        self.assertEqual('templates/test_rtl.html',
                         generate_rtl_template_name('templates/test.html'))
        self.assertEqual('test.twig_rtl.html',
                         generate_rtl_template_name('test.twig.html'))

    def test_generates_correct_rtl_template_name_for_template_with_no_file_extension(self):
        self.assertEqual('testhtml_rtl',
                         generate_rtl_template_name('testhtml'))
