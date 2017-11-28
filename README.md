## Supported tags and respective `Dockerfile` links

# nginx-uwsgi

**Docker** image with **Nginx** and **uWSGI** that allow web applications written in **Python 3.6**, **Python 3.5** and **Python 2.7** to run in a single container.

These images are derivatives or **tiangolo's** original [UWSGI-NGINX-DOCKER](https://github.com/tiangolo/uwsgi-nginx-docker)

## Changes

These images include the following enhancements from the original:
- *supervisord* configuration file explicitly referenced
  - eliminates CRIT errors in STY output
- `supervisord.conf` includes an explicit user-name (root)
  - eliminates CRIT errors in STY output
- updated version of Nginx (1.13.7)
- updated python revisions for each version supported (2.7, 3.5, and 3.6)

Full documentation is included in tiangolo's [repo](https://github.com/tiangolo/uwsgi-nginx-docker).

## Docker Hub Repository

The docker-hub repository for these images is [here](https://hub.docker.com/r/robpco/nginx-uwsgi/).

The images can be pulled by using the version of python desired (2.7, 3.5, or 3.6) as a tag.  No short-tags provided to prevent incorrect pulls:

`docker pull robpco/nginx-uwsgi:python2.7`

`docker pull robpco/nginx-uwsgi:python3.5`

`docker pull robpco/nginx-uwsgi:python3.6`
