#!/usr/bin/env bash
pip install -r backend/requirements.txt
export ADMIN_PASSWORD=${ADMIN_PASSWORD:-changeme}
export MAIL_USERNAME=${MAIL_USERNAME:-some@email.dk}
export MAIL_PASSWORD=${MAIL_PASSWORD:-some password}
export MAIL_RECIPIENT=${MAIL_RECIPIENT:-some@email.dk}
gunicorn backend.app:app $@
