*NOTE: These images are the result of several configuration changes I made to **tiangolo's images*** [UWSGI-NGINX-DOCKER](https://github.com/tiangolo/uwsgi-nginx-docker) *The changes are described below, and I'm sharing my modified images.*

# Supported tags

  - `python2.7` - robpco/nginx-uwsgi:python2.7
  - `python3.5` - robpco/nginx-uwsgi:python3.5
  - `python3.6` - robpco/nginx-uwsgi:python3.6

# Overview

**Docker** image with **Nginx** and **uWSGI** to allow web applications written in **Python 3.6**, **Python 3.5** and **Python 2.7** to run in a single container.  These images do not have **flask** or **django** installed.  They are base image to allow the addition of a variety of Python web-libraries.

For a detailed description, examples and documentation visit tiangolo's [repo](https://github.com/tiangolo/uwsgi-nginx-docker).

# Changes

These images include the following changes from the original:
- `supervisord.conf` is explicitly referenced via the Dockerfile CMD statement
  - this eliminates a CRIT errors
- `supervisord.conf` includes an explicitly set user-name (root); this can be changed in the `supervisord.conf` file
  - This eliminates a different CRIT error
- Includes an updated version of Nginx (1.13.7)
- Includes updated python revisions for each supported version (2.7, 3.5, and 3.6)
- Adds LISTEN_PORT environment var to allow setting custom ports; via docker run, or docker-compose.
- Adds Alpine Versions submitted by ProgEsteves (not yet tested or published to docker-hub)

# Example `Dockerfile`
The Dockerfile's for each version only differ on the first line, which specifies the version of Python (in the FROM command).  

  - [(pythonx.x/Dockerfile) ](https://hub.docker.com/r/robpco/nginx-uwsgi/~/dockerfile/)

# Docker Hub Repository

A docker-hub [repository](https://hub.docker.com/r/robpco/nginx-uwsgi/) contains pre-built images.  The images can be pulled by using the python version as a tag.

```bash
docker pull robpco/nginx-uwsgi:python2.7
docker pull robpco/nginx-uwsgi:python3.5
docker pull robpco/nginx-uwsgi:python3.6
```

These images to not support the `latest` tag, as it can lead to confusion about the version with potentially catastrophic results.
