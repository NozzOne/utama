#!/usr/bin/env bash
#!/bin/bash
#!/bin/sh
#!/bin/sh -
NAME="utama"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-utama.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=nozz
GROUP=nozz
NUM_WORKERS=5
DJANGO_WSGI_MODULE=animefly.wsgi

rm -frv $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR

exec ${DJANGODIR}/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR
