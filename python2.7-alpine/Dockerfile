FROM python:2.7-alpine3.7

RUN set -x && \
    apk add --no-cache \
        gcc \
        libc-dev \
        linux-headers \
        bash \
        nginx \
        supervisor \
    # protect against uwsgi compile failing randomly
    && (while true; do pip install --no-cache-dir --disable-pip-version-check uwsgi && break; done)

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

# Replace Nginx configuration on alpine
COPY nginx.main.conf /etc/nginx/nginx.conf
RUN mkdir -p /run/nginx && \
    echo "daemon off;" >> /etc/nginx/nginx.conf

# copy config files
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/

# set ENV variables and expose ports
ENV UWSGI_INI /app/uwsgi.ini
# Enable limiting maximum filesize upload (nginx default is 1m)
ENV NGINX_MAX_UPLOAD 0
# Enable changing default listening port on Nginx
ENV LISTEN_PORT 80
EXPOSE 80 443

# setup entrypoint.sh which generates Nginx configs at runtime
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
