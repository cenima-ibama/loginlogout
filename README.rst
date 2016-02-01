=============================
loginlogout
=============================

View and templates to login and logout.

Quickstart
----------

Install loginlogout::

    pip install git+https://github.com/ibamacsr/loginlogout.git

Add loginlogout package to your INSTALLED_APPS and add also the namespace and name of the url to where you want the users be redirect after the login:

::

    INSTALLED_APPS=[
        ...
        'loginlogout'
        ...
    ]

    URL_AFTER_LOGIN='namespace:url_name'

loginlogout has two important templates:

* **login_page.html** - a bootstrap template with the login form
* **login_menu.html** - adds a login and logout menu to the bootstrap navbar

You can use it by including login_menu.html to your base.html navbar

::

    <div class="collapse navbar-collapse">
      <ul class="nav navbar-nav">
        <li><a href="">NAME</a></li>
      </ul>
      {% include 'loginlogout/login_menu.html' %}
    </div>


Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
