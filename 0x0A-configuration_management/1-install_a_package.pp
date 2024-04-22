# Using Puppet, install flask from pip3

exec { 'flask':
  command => '/usr/bin/pip3 install flask',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => '/usr/bin/pip3 show flask'
}
