# session failure chane user limit from 4 and 5 to 1000 and the max is 65535                                                            
exec {'hard':
path     => ['/usr/bin/'],
command  => "sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 1000/g' /etc/security/limits.conf",
provider => 'shell',
}
exec {'soft':
path     => ['/usr/bin/'],
command  => "sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 1000/g' /etc/security/limits.conf",
provider => 'shell',
}
