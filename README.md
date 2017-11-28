*NOTE: These images are a fork or the repository [tiangolo/UWSGI-NGINX-DOCKER](https://github.com/tiangolo/uwsgi-nginx-docker).  This fork was necessary because of an urgent need for changes and modifications, which are described below.*

# Supported tags and `Dockerfile` links

  - [`python2.7` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python2.7/Dockerfile)
  - [`python2.7-alpine` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python2.7-alpine/Dockerfile)
  - [`python3.5` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.5/Dockerfile)
  - [`python3.5-alpine` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.5-alpine/Dockerfile)
  - [`python3.6` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.6/Dockerfile)
  - [`python3.6-alpine` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.6-alpine/Dockerfile)

# Overview

**Docker** image with **Nginx**, **uWSGI** and **Python** running in a single container that enables easy migration of Python Web Apps to production on NGINX.  They are designed as a base image, and do not have web-frameworks pre-installed.  To use them, just add your web-framework of choice (Flask, Django, etc..) and python application.

**For detailed information, examples and documentation visit tiangolo's [repo](https://github.com/tiangolo/uwsgi-nginx-docker).**

# Changes

These images include the following changes from the original repo:
- The addition of alpine-linux variants that are much smaller in size.
- `supervisord` enhancement to reduce CRIT errors
  - `supervisord.conf` is explicitly referenced via the Dockerfile CMD statement
  - `supervisord.conf` includes an explicitly set user-name (root) (which can be changed).
- Includes an updated version of Nginx (1.13.7) on non-alpine variants
- Includes updated python revisions for each supported version (2.7, 3.5, and 3.6)
- Adds LISTEN_PORT environment var to allow setting custom ports; via docker run, or docker-compose.

# Docker Hub Repository

The docker-hub [repository](https://hub.docker.com/r/robpco/nginx-uwsgi/) contains pre-built images.  The images can be pulled by using the python version as a tag (or python version + "-alpine").

```bash
docker pull robpco/nginx-uwsgi:python3.6-alpine
```

NOTE:  They do NOT not support a `latest` tag, because they are different variants, not incremental versions.  Using a `latest` tag with images of this sort can lead to potentially catastrophic results.
