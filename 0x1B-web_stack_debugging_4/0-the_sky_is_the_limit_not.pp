# solve failed requests ngnix by change ulimit (max open file) from 15 to 4096
exec {'change ulimit':
    path     => ['/usr/bin'],
    command  => "sudo sed -i 's/15/4096/g' /etc/default/nginx; sudo service nginx restart",
    provider => 'shell',
}
