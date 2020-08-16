#!/usr/bin/env bash
# Configure Nginx so that its HTTP response contains a custom header with Puppet
exec {'header':
command  => 'sudo apt-get -y update &&
             sudo apt-get -y install nginx &&
             sudo sed -i "\$ i \\\tadd_header X-Served-By \$hostname;\n" /etc/nginx/nginx.conf &&
             sudo service nginx restart',
provider => shell,
}
