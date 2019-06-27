#!/bin/bash

export PORT=5000
export APP_CONFIG_FILE="prod.py"

gunicorn -b 0.0.0.0:$PORT --chdir bills_service bills_service:app --log-level=debug