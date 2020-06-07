FROM dragas/nikola:latest
COPY . /nikola 
RUN nikola build

FROM nginx:stable-alpine
COPY --from=0 /nikola/output /usr/share/nginx/html
