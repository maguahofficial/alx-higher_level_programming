#!/bin/bash
# This sends a request to a url passed as an argument and shows only the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
