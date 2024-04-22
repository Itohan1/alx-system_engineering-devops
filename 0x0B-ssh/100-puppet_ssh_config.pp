# Client configuration file (w/ Puppet)

file { '/home/itohan/.ssh/config':
  ensure  => 'file',
  content => template('/home/itohan/.ssh/2-ssh_config.erb'),
  notify  => Service['sshd'],
}

service { 'sshd':
  ensure => running,
  enable => true,
}
