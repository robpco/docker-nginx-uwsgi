FROM python:2.7-alpine

# alpine installs NGINX_VERSION 1.10.3 via apk
ENV NGINX_VERSION 1.12.2-r1

RUN apk update \
    && apk add --no-cache --virtual .build-deps \
	  gcc \
	  libc-dev \
	  linux-headers \
	  bash \
    nginx \
    supervisor
    # nginx=${NGINX_VERSION} \

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	  && ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 80 443

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# Remove default configuration from Nginx - doesnt exist on alpine
# RUN rm /etc/nginx/conf.d/default.conf
# Required on alpine
RUN mkdir -p /run/nginx
COPY nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/

RUN pip install uwsgi
# Custom Supervisord config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV UWSGI_INI /app/uwsgi.ini
# ENV NGINX_MAX_UPLOAD 0   # Enables unlimited size uploads
ENV NGINX_MAX_UPLOAD 1m

# By default, Nginx listens on port 80.
# To modify this, change LISTEN_PORT environment variable.
# (in a Dockerfile or with an option for `docker run`)
# ENV LISTEN_PORT 80

# Copy the entrypoint that will generate Nginx additional configs
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Add demo app
COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
# CMD ["/usr/bin/supervisord"]
