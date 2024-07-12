#!/bin/bash

set -e

pip3 install -e /app/pymec-client

exec "$@"
