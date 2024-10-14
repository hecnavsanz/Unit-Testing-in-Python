#!/usr/bin/env bash

sudo cp /solutions/mod-08/config/labs-io-ssl.conf /etc/apache2/sites-available/labs-io-ssl.conf
sudo cp /solutions/mod-08/config/ssl/labs-io-ssl.crt /etc/ssl/certs/labs-io-ssl.crt
sudo cp /solutions/mod-08/config/ssl/labs-io-ssl.key /etc/ssl/private/labs-io-ssl.key
sudo a2enmod ssl
sudo a2ensite labs-io-ssl
sudo systemctl restart apache2
