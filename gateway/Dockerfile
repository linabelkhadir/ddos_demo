FROM nginx:alpine

ENV FAKE_IP=0.0.0.0

COPY default.conf /etc/nginx/templates/default.conf.template

CMD sh -c "envsubst '\$FAKE_IP' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"