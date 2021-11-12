FROM tiangolo/uwsgi-nginx-flask:python3.9

COPY requirements.txt /tmp/requirements_wiki.txt
RUN pip install --no-cache-dir -r /tmp/requirements_wiki.txt
RUN mkdir /wiki_repo \
	&& git clone https://github.com/PyAr/wiki.git /wiki_repo

RUN cd /wiki_repo \
	&& nikola build \
	&& cp -r /wiki_repo/output/* /usr/share/nginx/html

COPY ./app /app