*NOTE: These images are derivatives of **tiangolo's images** [UWSGI-NGINX-DOCKER](https://github.com/tiangolo/uwsgi-nginx-docker)* *which are released under Apache 2.  These variants are the result of configuration changes I required for a few projects, so I'm sharing my modifications.*

# Supported tags

  - `python2.7` - robpco/nginx-uwsgi:python2.7
  - `python3.5` - robpco/nginx-uwsgi:python3.5
  - `python3.6` - robpco/nginx-uwsgi:python3.6

# NGINX-UWSGI

**Docker** image with **Nginx** and **uWSGI** to allow web applications written in **Python 3.6**, **Python 3.5** and **Python 2.7** to run in a single container.  These images do not have **flask** or **django** installed.  They are base image to allow the addition of a variety of Python web-libraries.

## Changes

These images include the following differences from the original:
- `supervisord.conf` is explicitly referenced in the CMD statement in the Dockerfile
  - this eliminates CRIT errors
- `supervisord.conf` includes an explicit user-name (root), can also be set to an alternate username in the file
  - This eliminates another different CRIT error
- Includes updated version of Nginx (1.13.7)
- Includes updated python revisions for each supported version (2.7, 3.5, and 3.6)

For documentation please visit tiangolo's [repo](https://github.com/tiangolo/uwsgi-nginx-docker).

## Example `Dockerfile`
The Dockerfile's for each version only differ on the first line, which specifies the version of Python (in the FROM command).  

  - [(pythonx.x/Dockerfile) ](https://hub.docker.com/r/robpco/nginx-uwsgi/~/dockerfile/)

## Docker Hub Repository

A docker-hub [repository](https://hub.docker.com/r/robpco/nginx-uwsgi/) contains pre-built images.  The images can be pulled by using the python version as a tag.

```bash
docker pull robpco/nginx-uwsgi:python2.7
docker pull robpco/nginx-uwsgi:python3.5
docker pull robpco/nginx-uwsgi:python3.6
```

I have not added support for the `latest` tag, as it can lead to pulling the wrong python version and catastrophic results.
