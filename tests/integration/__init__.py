import imp
import pkg_resources
import sys


class MockProvider(pkg_resources.NullProvider):
    def __init__(self, module):
        pkg_resources.NullProvider.__init__(self, module)
        self.module = module

    def _has(self, path):
        return path in self.module._resources

    def _isdir(self, path):
        return False

    def get_resource_stream(self, manager, resource_name):
        return self.module._resources[resource_name]

    def _get(self, path):
        return self.module._resources[path].read()


class MockLoader(object):
    pass


def create_egg(name, resources):
    """
    Creates a mock egg with a list of resources.

    name: The name of the module.
    resources: A dictionary of resources.
    """
    egg = imp.new_module(name)
    egg.__loader__ = MockLoader()
    egg._resources = resources
    sys.modules[name] = egg
