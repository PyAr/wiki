FROM tiangolo/uwsgi-nginx-flask:python3.9

COPY requirements.txt /tmp/requirements_wiki.txt
RUN pip install --no-cache-dir -r /tmp/requirements_wiki.txt

COPY ./app /app
RUN mkdir /app/wiki_repo \
	&& git clone https://github.com/PyAr/wiki.git /app/wiki_repo \
	&& cd /app/wiki_repo \
	&& nikola build \
	&& cp -r /app/wiki_repo/output/* /usr/share/nginx/html