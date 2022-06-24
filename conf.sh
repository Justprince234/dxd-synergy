#!/bin/bash

export DJANGO_SETTINGS_MODULE=config.settings
export  DISABLE_COLLECTSTATIC=1
django-admin runserver


