FROM php:7.3-alpine

COPY src /var/www/html

RUN docker-php-source extract && \
    wget http://pecl.php.net/get/mongodb-1.5.3.tgz && \
    tar -zxf mongodb-1.5.3.tgz --exclude package.xml && \
    mv mongodb-1.5.3 /usr/src/php/ext/mongodb && \
    docker-php-ext-install mongodb && \
    rm mongodb-1.5.3.tgz && \
    docker-php-source delete && \
    \
    mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini" && \
    mv /var/www/html/limit.ini "$PHP_INI_DIR/conf.d/" && \
    \
    chmod 0500 /var/www/html && \
    chmod 0500 /tmp

WORKDIR /var/www/html

CMD ["/usr/local/bin/php","-S","0.0.0.0:80"]