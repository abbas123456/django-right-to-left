import os
import pkg_resources
import sys

from StringIO import StringIO
from django.conf import settings
from django.shortcuts import render_to_response
from django.test import TestCase
from django.template import loader
from django.utils import translation

from tests.integration import MockProvider, MockLoader, create_egg


class LoaderTest(TestCase):

    def tearDown(self):
        loader.template_source_loaders = None


class AppDirectoriesLoader(LoaderTest):

    def setUp(self):
        settings.INSTALLED_APPS = ['tests.test_app']
        settings.TEMPLATE_LOADERS = (
            ('rtl.loaders.RightToLeftLoader', (
                'django.template.loaders.app_directories.Loader',
            )),
        )

    def test_is_wrapped_correctly_by_right_to_left_loader(self):

        translation.activate("en")
        self.assertNotContains(render_to_response('test.html', {}),
                               'app directory right to left')
        translation.activate("ar")
        self.assertContains(render_to_response('test.html', {}),
                            'app directory right to left')


class CachedLoader(LoaderTest):

    def setUp(self):
        settings.TEMPLATE_LOADERS = (
            ('rtl.loaders.RightToLeftLoader', (
                ('django.template.loaders.cached.Loader', (
                    'django.template.loaders.filesystem.Loader',
                )),
            )),
        )

    def test_is_wrapped_correctly_by_right_to_left_loader(self):
        translation.activate("en")
        self.assertNotContains(render_to_response('test.html', {}),
                               'file system right to left')
        translation.activate("ar")
        self.assertContains(render_to_response('test.html', {}),
                            'file system right to left')


class EggLoader(LoaderTest):

    def setUp(self):
        settings.TEMPLATE_LOADERS = (
            ('rtl.loaders.RightToLeftLoader', (
                'django.template.loaders.eggs.Loader',
            )),
        )
        pkg_resources._provider_factories[MockLoader] = MockProvider
        create_egg("egg_app", {
            os.path.normcase('templates/test.html'): StringIO("egg loader left to right"),
            os.path.normcase('templates/test_rtl.html'): StringIO("egg loader right to left"),
        })
        settings.INSTALLED_APPS = ['egg_app']

    def test_is_wrapped_correctly_by_right_to_left_loader(self):
        translation.activate("en")
        self.assertNotContains(render_to_response('test.html', {}),
                               'egg loader right to left')
        translation.activate("ar")
        self.assertContains(render_to_response('test.html', {}),
                            'egg loader right to left')


class FileSystemLoader(LoaderTest):

    def setUp(self):
        settings.TEMPLATE_LOADERS = (
            ('rtl.loaders.RightToLeftLoader', (
                'django.template.loaders.filesystem.Loader',
            )),
        )

    def test_is_wrapped_correctly_by_right_to_left_loader(self):
        translation.activate("en")
        self.assertNotContains(render_to_response('test.html', {}),
                               'file system right to left')
        translation.activate("ar")
        self.assertContains(render_to_response('test.html', {}),
                            'file system right to left')
