FROM python:3.6-alpine

RUN apk update \
    && apk add --no-cache --virtual build-deps \
	  gcc \
	  libc-dev \
	  linux-headers \
    && apk add --no-cache \
	  bash \
    nginx \
    supervisor \
    && pip install uwsgi \
    && apk del build-deps

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	  && ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 80 443

# Replace Nginx configuration on alpine
RUN rm /etc/nginx/nginx.conf
COPY nginx.main.conf /etc/nginx/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN mkdir -p /run/nginx
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/

ENV UWSGI_INI /app/uwsgi.ini
# Enable unlimited filesize uploads by setting to 0
ENV NGINX_MAX_UPLOAD 1m

# Change default Nginx port
ENV LISTEN_PORT 80

# entrypoint.sh generates additional Nginx configs
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
