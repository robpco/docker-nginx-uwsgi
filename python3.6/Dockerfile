FROM python:3.6-stretch

RUN pip install --no-cache-dir --disable-pip-version-check uwsgi

ENV NGINX_VERSION 1.15.7-1~stretch

RUN set -x && \
    curl -O https://nginx.org/keys/nginx_signing.key && apt-key add ./nginx_signing.key; \
    echo "deb http://nginx.org/packages/mainline/debian/ stretch nginx" >> /etc/apt/sources.list \
    && apt-get update && apt-get install -y \
        ca-certificates \
        nginx=${NGINX_VERSION} \
        gettext-base \
        supervisor \
    && rm -rf /var/lib/apt/lists/*

# setup log files
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# setup and copy config files
RUN rm /etc/nginx/conf.d/default.conf && \
    echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# set ENV variables and expose ports
ENV UWSGI_INI /app/uwsgi.ini
# Enable unlimited filesize uploads (restore nginx default by setting to 1m)
ENV NGINX_MAX_UPLOAD 0
# Enable changing default Nginx port
ENV LISTEN_PORT 80
EXPOSE 80 443

# setup entrypoint.sh which generates Nginx configs at runtime
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
