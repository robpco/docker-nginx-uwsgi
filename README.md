# Supported tags and `Dockerfile` links

  - [`python2.7` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python2.7/Dockerfile)
  - [`python2.7-alpine` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python2.7-alpine/Dockerfile)
  - [`python3.5` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.5/Dockerfile)
  - [`python3.5-alpine` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.5-alpine/Dockerfile)
  - [`python3.6` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.6/Dockerfile)
  - [`python3.6-alpine` _(Dockerfile)_](https://github.com/robertpeteuil/docker-nginx-uwsgi/blob/master/python3.6-alpine/Dockerfile)

**The `latest` tag is not supported - one of the tags above must be explicitly specified.**
- This is necessary because the tags represent different variants, not incremental versions.
- This eliminates importing or pulling an unexpected version   


# Overview

**Docker** image with **Nginx**, **uWSGI** and **Python** running in a single container to simplify deploying pure Python Web Apps on NGINX.  They are designed for use as a base image, with the user adding Python Application Code and a web-framework (Flask, Django, etc..) to them.

*NOTE: This project began as a fork of the repository [tiangolo/UWSGI-NGINX-DOCKER](https://github.com/tiangolo/uwsgi-nginx-docker), due to an urgent need for changes and enhancements.*

**For detailed instructions, examples and documentation visit tiangolo's [repo](https://github.com/tiangolo/uwsgi-nginx-flask-docker).**

# Enhancements

These images includes the following enhancements:
- The addition of an alpine-linux variants
- `supervisord` enhancements to reduce CRIT errors
  - `supervisord.conf` is explicitly referenced via the Dockerfile CMD statement
  - `supervisord.conf` includes an explicitly set user-name
- Automatic image republishing for Python image updates
- Nginx updated to 1.13.7 on non-alpine variants
- Adds LISTEN_PORT environment var to allow setting custom ports

# Docker Hub Repository

The docker-hub [repository](https://hub.docker.com/r/robpco/nginx-uwsgi/) contains auto-generated images.  They can be pulled (or referenced) by using the image name `robpco/nginx-uwsgi` plus a tag containing the python version, and optionally appending "-alpine" (for alpine variants).

This example pulls the python3.6 alpine variant.
```bash
docker pull robpco/nginx-uwsgi:python3.6-alpine
```
