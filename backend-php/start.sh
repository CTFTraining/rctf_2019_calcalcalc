#!/bin/sh

echo $FLAG > /flag
export FLAG=not_flag
FLAG=not_flag

/usr/local/bin/php -S 0.0.0.0:80
