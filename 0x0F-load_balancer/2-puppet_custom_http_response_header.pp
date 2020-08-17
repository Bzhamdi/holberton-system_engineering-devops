#!/usr/bin/env bash
# ngnix configuration  with puppet

exec {'header':
path     => '/etc/nginx/sites-enabled/default',
command  => ' sudo apt-get -y update && 
             sudo apt-get -y install nginx && 
             sudo sed -i "40i \\\tadd_header X-Served-By \$hostname;\n" &&
             sudo service nginx restart',
provider => shell,
}
