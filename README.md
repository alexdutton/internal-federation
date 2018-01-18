# internal-federation

A Very Small Thing to manage SAML federation metadata.

## What it does

Not much at all yet, but it does at least verify that uploaded XML fragments
are valid `md:EntityDescriptor` elements for transcluding into a combined
metadata file — see `infed/validators.py`.

## Running

Assuming you're using virtualenvwrapper:

    $ createdb infed
    $ export DJANGO_SECRET_KEY=$(pwgen 32 1)  # But you want to keep the same key
    $ mkvirtualenv infed
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py runserver

Then point your browser at http://localhost:8000/.

