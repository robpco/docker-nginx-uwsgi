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

# nginx-uwsgi

**Docker** image with **Nginx**, **uWSGI** and **Python** running in a single container to enable running Python Web Apps on NGINX.

*NOTE: This project began as a fork of the repository [tiangolo/UWSGI-NGINX-DOCKER](https://github.com/tiangolo/uwsgi-nginx-docker), due to an urgent need for changes and enhancements.  Most of the original work was by [Sebastián Ramírez](https://github.com/tiangolo).*

## Overview

These Docker images allow the creation/migration of Python Web Apps to run with Nginx and uWSGI in a single container.  They're designed as base images that can be used:
- as base for other images, such as my `nginx-uwsgi-flask` image
- as base for users to add their Python Code and web-framework (such as Flask, Django, etc..).

## Enhancements

The images on this repo includes the following enhancements:
- The addition of an alpine-linux variants
- Ability to change Nginx listen port with the LISTEN_PORT environment variable
- Nginx updated to 1.13.7 on non-alpine variants
- `supervisord` enhancements to reduce CRIT errors
  - `supervisord.conf` is explicitly referenced via the Dockerfile CMD statement
  - `supervisord.conf` includes an explicitly set user-name
- Automatic image republishing with Python image updates

## Information

The Docker-Hub [repository](https://hub.docker.com/r/robpco/nginx-uwsgi/) contains auto-generated images from this repo.  They can be referenced (or pulled) by using the image name `robpco/nginx-uwsgi`, plus a tag for the python version desired (ex: `:python3.6`), and optionally appending `-alpine` to the tag (for alpine variants).

The are two primary ways to use these images:
- Use them as a base image by specifying them in the `FROM` line in your `Dockerfile`
- Run the image and map your code into the container's `/app` directory

**Detailed documentation and examples can be found on [Sebastián Ramírez's repo](https://github.com/tiangolo/uwsgi-nginx-flask-docker).**

## Custom Environment Variables

These images support the following custom environment variables:

- **UWSGI_INI** = the path and file of the configuration info
   - default: `/app/uwsgi.ini`

- **NGINX_MAX_UPLOAD** = the maximum file upload size allowed by Nginx
   - 0 = unlimited (image default)
   - 1m = normal Nginx default

- **LISTEN_PORT** = custom port that Nginx should listen on
   - 80 = Nginx default

### Setting Environment Variables

Environment variables can be set in multiple ways.  The following examples, demonstrate setting the `LISTEN_PORT` environment variable via three different methods.  These methods apply to the other Environment Variables as well.

Environment variables set in a `Dockerfile`:

```dockerfile
# ... (snip) ...

ENV LISTEN_PORT 8080

# ... (snip) ...
```

Environment variables set during [`docker run`](https://docs.docker.com/engine/reference/commandline/run/#options) with the `-e` option:

```shell
docker run -e LISTEN_PORT=8080 -p 8080:8080 myimage
```

Environment variables can be set during `docker-compose up` by using the `environment:` keyword in a `docker-compose` file:

```yml
version: '2.2'

services:
  web:
    image: myapp
  environment:
    LISTEN_PORT: 8080
```


## UPDATES

- 2017-11-29: Added ability to change Nginx listen port by using the environment variable `LISTEN_PORT`.  Thanks to github user [tmshn](https://github.com/tmshn)

- 2017-11-29: Alpine variants added with assistance of github user [ProgEsteves](https://github.com/ProgEsteves)
    - Additional Alpine changes required:
        - Replace default `/etc/nginx/nginx.conf` with an alternate version
        - Added `RUN mkdir -p /run/nginx` to Dockerfile

- 2017-11-29: Added Automatic image republishing when Python image updates

- 2017-11-28: Fixed console errors from supervisor process:
    - Added explicit path reference to `supervisord.conf` in Dockerfile `CMD`
    - Added explicitly set username in `supervisord.conf`

- 2017-11-28: Updated Nginx version
