#change the ssh configuration file
#Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
#Your SSH client configuration must be configured to refuse to authenticate using a password
exec {'/etc/ssh/ssh_config':
command  => 'echo "    IdentityFile ~/.ssh/holberton\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
path     => '/bin',
}
