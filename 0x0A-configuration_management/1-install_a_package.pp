# Using Puppet, install flask from pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  command  => '/usr/bin/python3 -m pip',
}
