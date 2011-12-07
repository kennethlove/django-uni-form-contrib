=====================================
``django-uni-form`` Contrib Templates
=====================================

What
----

Contributed templates for `Daniel Greenfeld <https://github.com/pydanny>`_ and `Miguel Araujo <https://github.com/maraujop>`_'s 
awesome `django-uni-form <https://github.com/pydanny/django-uni-form>`_ library. Template sets are named for the library they 
relate to.

How
---

Install:::

    pip install -e git://github.com/bmihelac/django-uni-form-contrib.git@make-django-app#egg=uni_form_contrib

Add ``uni_form_contrib.twitter_bootstrap`` application to ``INSTALLED_APPS`` in
settings.py **before** ``uni_form`` so django will pick this templates instead
of default ``uni_form`` templates.

Who
---

Current contributors are:

    * `Kenneth Love <https://github.com/kennethlove>`_

    * `Bojan Mihelac <https://github.com/bmihelac>`_

License
-------

All templates are released under the MIT license.
