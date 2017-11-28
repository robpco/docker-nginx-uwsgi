# Supported tags and `Dockerfile` links

  - [`python2.7` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python2.7/Dockerfile)
  - [`python2.7-alpine` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python2.7-alpine/Dockerfile)
  - [`python3.5` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.5/Dockerfile)
  - [`python3.5-alpine` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.5-alpine/Dockerfile)
  - [`python3.6` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.6/Dockerfile)
  - [`python3.6-alpine` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.6-alpine/Dockerfile)

**These images require explicitly specifying a tag listed as the `latest` tag is not supported.**
- This implementation is so users are aware of the exact version they are importing (or pulling).
- This is necessary because the tags on these images represent different variants, not incremental versions.  


# Overview

**Docker** image with **Nginx**, **uWSGI** and **Python** running in a single container that enables easy migration of Python Web Apps to production on NGINX.  They are designed as a base image, and do not have web-frameworks pre-installed.  To use them, add your web-framework of choice (Flask, Django, etc..) and python application.

*NOTE: This project began as a fork of the repository [tiangolo/UWSGI-NGINX-DOCKER](https://github.com/tiangolo/uwsgi-nginx-docker), due to an urgent need for changes and enhancements described below.*

**For detailed information, examples and documentation visit tiangolo's [repo](https://github.com/tiangolo/uwsgi-nginx-docker).**

# Enhancements

These images includes the following enhancements:
- The addition of an alpine-linux variant for each supported python version.
- `supervisord` enhancements to reduce CRIT errors
  - `supervisord.conf` is explicitly referenced via the Dockerfile CMD statement
  - `supervisord.conf` includes an explicitly set user-name (root) (which can be changed).
- Updated version of Nginx (1.13.7) on non-alpine variants
- Updated python revisions for each supported version (2.7, 3.5, and 3.6)
- Adds LISTEN_PORT environment var to allow setting custom ports; via docker run, or docker-compose.

# Docker Hub Repository

The docker-hub [repository](https://hub.docker.com/r/robpco/nginx-uwsgi/) contains auto-generated images.  They can be pulled (or referenced) by using the image name `robpco/nginx-uwsgi` plus a tag containing the python version desired (optionally appending "-alpine", for alpine variants).

This example pulls the python3.6 alpine variant.
```bash
docker pull robpco/nginx-uwsgi:python3.6-alpine
```
