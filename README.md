# Supported tags and `Dockerfile` links

- `py2.7`, `python2.7` [_(python2.7/Dockerfile)_](https://github.com/robpco/docker-nginx-uwsgi/blob/master/python2.7/Dockerfile)
- `py2.7-A`, `py2.7-alpine`, `python2.7-alpine` [_(python2.7-alpine/Dockerfile)_](https://github.com/robpco/docker-nginx-uwsgi/blob/master/python2.7-alpine/Dockerfile)
- `py3.6`, `python3.6` [_(python3.6/Dockerfile)_](https://github.com/robpco/docker-nginx-uwsgi/blob/master/python3.6/Dockerfile)
- `py3.6-A`, `py3.6-alpine`, `python3.6-alpine` [_(python3.6-alpine/Dockerfile)_](https://github.com/robpco/docker-nginx-uwsgi/blob/master/python3.6-alpine/Dockerfile)

**You must explicitly use one of the tags above.**  The `latest` tag is not assigned since each tag represents a different variant, not an incremental version.

## NGINX-UWSGI

**Docker** image with **Nginx**, **uWSGI** and **Python** running in a single container to enable running Python Web Apps on NGINX.

**GitHub Repo**: <https://github.com/robpco/docker-nginx-uwsgi>

**Docker Hub Images**: <https://hub.docker.com/r/robpco/nginx-uwsgi/>

## Overview

This Docker image allow the creation/migration of Python Web Apps to run on Nginx and uWSGI in a single container.  It's designed for use as base image for:

- Other images - such as a pre-built image for running Flask Apps [nginx-uwsgi-flask](https://github.com/robpco/docker-nginx-uwsgi-flask) .
- A development image that can be customized with your unique web-framework, Python libraries and code.

This repo auto-generates images to [Docker-Hub](https://hub.docker.com/r/robpco/nginx-uwsgi/).  It includes standard and alpine-based variants for each supported Python version (2.7, 3.6).

## Usage

The Docker-Hub [repository](https://hub.docker.com/r/robpco/nginx-uwsgi/) contains auto-generated images from this repo.  They can be referenced (or pulled) by using the image name `robpco/nginx-uwsgi`, plus a tag for the python version desired (ex: `:python3.6`), and optionally appending `-alpine` to the tag (for alpine variants).

## Custom Environment Variables

This image supports the following custom environment variables:

- **UWSGI_INI** - the path and file of the configuration info
  - default: `/app/uwsgi.ini`
- **NGINX_MAX_UPLOAD** - the maximum file upload size allowed by Nginx
  - 0 = unlimited (image default)
  - 1m = normal Nginx default
- **LISTEN_PORT** - custom port that Nginx should listen on
  - 80 = Nginx default

## Setting Environment Variables

Environment variables can be set in multiple ways.  The following examples, demonstrate setting the `LISTEN_PORT` environment variable via three different methods.  These methods apply to the other Environment Variables as well.

### Setting in a `Dockerfile`

```dockerfile
# ... (snip) ...
ENV LISTEN_PORT 8080
# ... (snip) ...
```

### Setting during [`docker run`](https://docs.docker.com/engine/reference/commandline/run/#options) with the `-e` option

```shell
docker run -e LISTEN_PORT=8080 -p 8080:8080 myimage
```

### Setting in `docker-compose` file using the `environment:` keyword in a `docker-compose` file

```yml
version: '2.2'
services:
  web:
    image: myapp
  environment:
    LISTEN_PORT: 8080
```

## UPDATES

- 2017-12-11: Added multiple tags per variant: `py3.6` is the same as `python3.6`, and so forth...
- 2017-11-29: Added ability to change port Nginx listens on with new environment variable `LISTEN_PORT`.
  - Thanks to github user [tmshn](https://github.com/tmshn)
- 2017-11-29: Alpine variants added
  - Thanks to github user [ProgEsteves](https://github.com/ProgEsteves)
- 2017-11-29: Automatic image re-build when Python updates
- 2017-11-28: Updated Nginx version installed on non-Alpine images
- 2018-05-04: Updated non alpine version to use `pythonx.x-stretch` as base & Nginx 1.13.12-1
- 2018-05-04: Update Alpine versions to use `pythonx.x-alpine3.7` as base
- 2018-05-04: Removed `python3.5` support due to lack of use and base on stretch and alpine3.7
- 2018-06-10: Updated non alpine versions to Nginx 1.15.0-1

## CHANGELOG

- 2017-12-15: Fix to avoid duplicate listen entries in nginx.conf
- 2017-11-30: Alpine images - eliminated uWSGI random build failures
- 2017-11-30: Non-Alpine images - limit build failures caused by GPG key validation failing
- 2017-11-29: Alpine required additional changes:
  - Replace default `/etc/nginx/nginx.conf` with an alternate version
  - Create `/run/nginx` directory to stop immediate Nginx crash
- 2017-11-28: Fixed console errors from supervisor process:
  - Added explicit path reference to `supervisord.conf` in Dockerfile `CMD` statement
  - Added explicitly set username in `supervisord.conf`
