# Using Puppet, create a manifest that kills a process named killmenow

exec { 'kill_process':
  command     => 'pkill killmenow',
  path        => ['/bash', '/bin/bash'],
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
