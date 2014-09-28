Django Authentication
=====================

A barebones Django app that manages user authentication and related services.

This is app is for user's interested in simple authentication or for user's looking to learn the basics of Django authentication.

Installation
============

* Clone this repo.  Copy the django_authentication folder into your django project.
* Add django_authentication to your installed apps.
* Include the app's urls file with: url(r'^users/', include('django_authentication.urls'))
* Setup a LOGIN_URL and a LOGIN_REDIRECT_URL in your settings.py
* Override the default templates provided (you can delete django_auth.html)

Contributing
============

Pull request, email, smoke-signals are all acceptable forms of getting my attention.  If you want to help, please do!

License
=======
MIT
