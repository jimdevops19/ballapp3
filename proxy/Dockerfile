FROM nginx:1.19.2-alpine
RUN mkdir /static
COPY ./static/ /static/
RUN rm -rf /etc/nginx/conf.d/default.conf
COPY conf /etc/nginx/conf.d/default.conf