## A minimal django server
A sample for Django framework
It includes a basic project structure following MVT pattern of Django

The template has been set up for use with Python >= 3.10 and [Docker](https://www.docker.com/).

## Running locally

To run the basic server, you'll need to install a few requirements. To do this, run:

```bash
pip install -r requirements.txt
```

This will install only the dependencies required to run the server. To boot up the 
default server, you can run:

```bash
bash run.sh
```

This will start a [Gunicorn](https://gunicorn.org/) server that wraps the Django app 
defined in `app/app.py`. Note that [this is one of the recommended ways of deploying a
Django app 'in production']. 

The server shipped with Django is [intended for development
purposes only].  

You should now be able to send:

```bash
curl localhost:8000/health
```

And receive the response `OK` and status code `200`.

## Running with `docker`

Unsurprisingly, you'll need [Docker](https://www.docker.com/products/docker-desktop) 
installed to run this project with Docker. To build a containerised version of the API, 
run:

```bash
docker build . -t django-app
```

To launch the containerised app, run:

```bash
docker run -p 8000:8000 django-app
```

You should see your server boot up, and should be accessible as before.