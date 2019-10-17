# Montehelfer

Montehelfer (dj_montedb) is a school and kindergarten management software. It is built with [Python][0]
using the [Django Web Framework][1] and based on [edge v2.2][2].

## Installation

Clone the project:

    git clone git@github.com:oliverbienert/dj_montedb.git
    cd dj_montedb
    mkdir logs
    mkdir media
    cp src/config/settings/local.sample.env src/config/settings/local.env
    
### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    python3 -m venv ~/.venvs/dj_montedb
    ~/.venvs/dj_montedb/bin/activate

Install all dependencies:

    pip install -r requirements.txt
    
On some Linux systems like Ubuntu, Pillow will not install unless you install a C compiler and dependencies:

    sudo apt-get install python3-dev python3-setuptools libjpeg-dev zlib1g-dev

Run migrations:

    cd src
    ./manage.py migrate
    ./manage.py createsuperuser

Run the development server:

    ./manage.py runserver
    

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://github.com/arocks/edge
