FROM python:3.5

RUN pip install uwsgi

ENV NGINX_VERSION 1.13.7-1~jessie

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y ca-certificates nginx=${NGINX_VERSION} gettext-base \
	&& rm -rf /var/lib/apt/lists/*
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 80 443

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
COPY uwsgi.ini /etc/uwsgi/

RUN apt-get update && apt-get install -y supervisor \
&& rm -rf /var/lib/apt/lists/*
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV UWSGI_INI /app/uwsgi.ini

# ENV NGINX_MAX_UPLOAD 0   # Enables unlimited size uploads
ENV NGINX_MAX_UPLOAD 1m

# entrypoint.sh generates additional Nginx configs
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

COPY ./app /app
WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
