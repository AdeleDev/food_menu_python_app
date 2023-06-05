# Python Foodgram App (Django)

![Workflow](https://github.com/AdeleDev/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

Fullstack service to publish recipes, subscribe to publications of other users, add favorite recipes to the
Favorites list. Has a possibility to download a summary ingredients list, needed for cooking of dishes from chosen list.

Using SQLite as DB, backend based on View-sets approach.
JWT-token for authorization.
DRF for permissions setup

Backend performs next modules:

* Recipe: can create new recipes with images, ingredients, tags, cooking time and text or edit/delete existing ones
* Tag: Colored titles
* Ingredient: Ingredient info, connected to recipe

Pages:

* Main - list of the first six recipes, sorted by publication date (newest to oldest).
  The rest of the recipes are available on the following pages: there is pagination at the bottom of the page.
* Recipe - full description of the recipe. For authorized users - the ability to add a recipe to
  favorites and to the shopping list, the ability to subscribe to the author of the recipe.
* User profile - the username, all recipes published by the user and the ability to subscribe to the user.
* Subscription - subscription to publications is available only to an authorized user. The subscriptions page is only
  available to the owner.
* List of favorites - the list of favorites is available only to an authorized user. The favorites list can only be
  viewed by its owner.
* Shopping list - the shopping list is available to authorized users. The shopping list can only be viewed by its owner.

Roles:

* Anonymous
    * create an account
    * view recipes on homepage
    * view individual recipe pages
    * view user pages
    * filter recipes by tags.
* User (authenticated)
    * log in with your username and password
    * log out of the system (log out)
    * change your password
    * create/edit/delete your own recipes
    * view recipes on homepage
    * view user pages
    * view individual recipe pages
    * filter recipes by tags
    * work with a personal favorites list: add recipes to it or delete them, view your favorite recipes page
    * work with a personal shopping list: add / delete any recipes, upload a file with the number of ingredients needed
      for recipes from the shopping list
    * subscribe to publications of recipe authors and unsubscribe, view your subscription page
* Administrator
    * same rights as authenticated user
    * change the password of any user
    * create/block/delete user accounts
    * edit/delete any recipes
    * add/remove/edit ingredients
    * add/remove/edit tags

### Built With

* [![Python][Python.io]][Python-url]
* [![Django][Django.io]][Django-url]
* [![SqlLite][SqlLite.io]][SqlLite-url]
* [![Nginx][Nginx.io]][Nginx-url]
* [![Unicorn][Unicorn.io]][Unicorn-url]
* [![Docker][Docker.io]][Docker-url]
* [![Javascript][Javascript.io]][Javascript-url]
* [![React][React.io]][React-url]
* [![NodeJs][NodeJs.io]][NodeJs-url]

## Pre-installations

#### Clone the repo:

```sh
git clone https://github.com/AdeleDev/food_menu_python_app.git
```

#### Set .env file:

```
Take infra/.env.example as initial file
Rename ".env.example" to ".env"
Set necessary values in the file
```

## Usage

#### Start docker-compose:

```sh
cd foodgram-project-react/infra
```

```sh
docker compose up
```

#### Do migrations:

```sh
docker-compose exec backend python manage.py makemigrations --noinput  
docker-compose exec backend python manage.py migrate --noinput

```

#### Collect static
```sh
docker-compose exec backend python manage.py collectstatic --no-input 
```

#### Add db initial data:
```sh
sudo docker-compose exec backend python manage.py load_ingredients
```
```sh
sudo docker-compose exec backend python manage.py load_tags
```
#### Create superuser:

```sh
docker-compose exec backend python manage.py createsuperuser
```

#### Open project:

Navigate to http://localhost:8000/

## API example requests:

API documentation:

```
http://127.0.0.1/api/docs/
```

Get JWT-token request:

```
http://127.0.0.1:8000/api/auth/token/login/
```

Get genres request:

```
http://127.0.0.1:8000/api/recipes/
```

Get tags:

```
http://127.0.0.1:8000/api/tags/
```

<!-- MARKDOWN LINKS & IMAGES -->

[Python.io]: https://img.shields.io/badge/-Python-yellow?style=for-the-badge&logo=python

[Python-url]: https://www.python.org/

[Django.io]: https://img.shields.io/badge/-Django-darkgreen?style=for-the-badge&logo=django

[Django-url]: https://www.djangoproject.com/

[SqlLite.io]: https://img.shields.io/badge/-SQLite-blue?style=for-the-badge&logo=sqlite

[SqlLite-url]: https://www.sqlite.org/index.html

[Docker.io]: https://img.shields.io/badge/-Docker-lightblue?style=for-the-badge&logo=docker

[Docker-url]: https://docs.docker.com/

[Nginx.io]: https://img.shields.io/badge/-Nginx-lightgreen?style=for-the-badge&logo=nginx

[Nginx-url]: https://docs.docker.com/

[Unicorn.io]: https://img.shields.io/badge/-Gunicorn-white?style=for-the-badge&logo=gunicorn

[Unicorn-url]: https://docs.docker.com/

[Javascript.io]: https://img.shields.io/badge/-Javascript-lightyellow?style=for-the-badge&logo=javascript

[Javascript-url]: https://www.javascript.com/

[React.io]: https://img.shields.io/badge/React-black?style=for-the-badge&logo=react

[React-url]: https://reactjs.org/

[NodeJs.io]: https://img.shields.io/badge/-Node.js-green?style=for-the-badge&logo=Node.js

[NodeJs-url]: https://nodejs.org/en/
