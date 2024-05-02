# Using Puppet, install flask from pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  command  => '/usr/bin/python3.8 -m pip',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  command  => '/usr/bin/python3.8 -m pip',
}
