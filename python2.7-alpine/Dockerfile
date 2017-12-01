FROM python:2.7-alpine

RUN set -x \
    && \
    apk add --update --no-cache \
        gcc \
        libc-dev \
        linux-headers \
        bash \
        nginx \
        supervisor \
#        uwsgi-python \
    && rm -rf /var/cache/apk/* \
    && pip install uwsgi

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Replace Nginx configuration on alpine
RUN rm /etc/nginx/nginx.conf
COPY nginx.main.conf /etc/nginx/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN mkdir -p /run/nginx

# setup and copy config files
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/

# expose ports and set ENV variables
EXPOSE 80 443
ENV UWSGI_INI /app/uwsgi.ini
# Enable unlimited filesize uploads (restore nginx default by setting to 1m)
ENV NGINX_MAX_UPLOAD 0
# Enable changing default Nginx port
ENV LISTEN_PORT 80

# setup entrypoint.sh which generates Nginx configs at runtime
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
