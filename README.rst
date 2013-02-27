
=====================
django-right-to-left
=====================

-------
Summary
-------
A Django template loader that looks for an alternative right to left version of a template file if the activated language is a right to left language such as Arabic or Hebrew. 

This provides a clean and easy way to customise the markup in your templates without having to place conditional logic in your templates.

The most common use case for this would be a Django website that supports both a left to right and right to left language, such as English and Arabic.

-------
Example
-------
Suppose you had the following Django template:

homepage.html
    {% extends "layout.html" %}
    
    {% block content %}
    
    <div id="main_content">...</div>

    <div id="side_promo">...</div>
    
    {% endblock %}

To swap the content around when the activated language is Arabic, an IF statement would have to be wrapped around the div tags. This may be a feasible solution for small templates but for most templates this will make the template very hard to read and messy. 

Using the django-right-to-left template loader makes this process a lot cleaner by allowing you to create an alternative template with the same name but with "_rtl" appended to the file name. In this example, a file called "homepage_rtl.html" will be picked up as the alternative.

Now when a template is rendered, regardless of whether it is rendered by a Django view or by extending another template using the "extends" block or included using the "include" block, the django-right-to-left template loader will look to see if an alternative template suffixed with "_rtl" exists. If it doesn't exist it will load the standard version of the template.

------------
Installation
------------

You can install django-right-to-left using pip:

    $ pip install django-right-to-left

or easy_install

    $ easy_install django-right-to-left

------------
Instructions
------------

django-right-to-left works in exactly the same way as the Django `cached template loader <https://docs.djangoproject.com/en/dev/ref/templates/api/#django.template.loaders.cached.Loader>`_.
The django-right-to-left template loader is a class-based loader that you configure with a list of other loaders that it should wrap.

Simply wrap the template loaders defined in your settings file with the django-right-to-left-loader.

For example, if you are currently using the filesystem loader and app_directories loader, change the **TEMPLATE_LOADERS** settings from:

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',

        'django.template.loaders.app_directories.Loader',

    )

to this:

    TEMPLATE_LOADERS = (
        ('rtl.loaders.Loader', (

            'django.template.loaders.filesystem.Loader',

            'django.template.loaders.app_directories.Loader',

        )),

    )

That's all there is to it. All you have to do now is create your alternative templates, ensuring that the string "_rtl" is appended to the filename. So the alternative template for "homepage.html" will be "homepage_rtl.html".

------------------
Running the tests
------------------

django-right-to-left has a small but extensive test suite. You can run the tests by running the following commands, assuming you have `virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_ installed. 

    $ git clone git@github.com:abbas123456/django-right-to-left.git

    $ cd django-right-to-left

    $ mkvirtualenv django-right-to-left

    $ pip install -r requirements.txt

    $ ./runtests.py