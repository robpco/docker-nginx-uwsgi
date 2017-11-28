# Supported tags

  - `python2.7` - robpco/nginx-uwsgi:python2.7
  - `python3.5` - robpco/nginx-uwsgi:python3.5
  - `python3.6` - robpco/nginx-uwsgi:python3.6

# NGINX-UWSGI

**Docker** image with **Nginx** and **uWSGI** to allow web applications written in **Python 3.6**, **Python 3.5** and **Python 2.7** to run in a single container.

These images do not have **flask** or **django** installed.  They are base image to allow the addition of a variety of Python web-libraries.

*NOTE: They are updated derivatives of **tiangolo's** original images [UWSGI-NGINX-DOCKER](https://github.com/tiangolo/uwsgi-nginx-docker), which are licensed under Apache 2.*

## Enhancements

These images include the following changes from the original:
- the **supervisord** configuration file is explicitly referenced
  - eliminates CRIT errors
- `supervisord.conf` includes an explicit user-name (root)
  - eliminates CRIT errors
- updated version of Nginx (1.13.7)
- updated python revisions for each version supported (2.7, 3.5, and 3.6)

Full documentation is included in tiangolo's [repo](https://github.com/tiangolo/uwsgi-nginx-docker).

## Example `Dockerfile`
The Dockerfile's for each version only differ on the first line, which specifies the version of Python (in the FROM command).  

  - [(pythonx.x/Dockerfile) ](https://hub.docker.com/r/robpco/nginx-uwsgi/~/dockerfile/)

## Docker Hub Repository

A docker-hub [ repository](https://hub.docker.com/r/robpco/nginx-uwsgi/) contains pre-built images.  The images can be pulled by using the python version as a tag.

```
docker pull robpco/nginx-uwsgi:python2.7
docker pull robpco/nginx-uwsgi:python3.5
docker pull robpco/nginx-uwsgi:python3.6
```

A `latest` tag is not supported as it can lead to pulling the wrong python version with catastrophic results.
