# 0-strace_is_your_friend.pp

exec { 'fix-apache':
  command => '/usr/sbin/service apache2 restart',
  onlyif  => 'test -f /etc/apache2/sites-enabled/000-default.conf',
}

file { '/etc/apache2/sites-enabled/000-default.conf':
  ensure  => 'present',
  source  => '/etc/apache2/sites-available/000-default.conf',
  notify  => Exec['fix-apache'],
}

exec { 'fix-wordpress':
  command => '/usr/sbin/service apache2 restart',
  onlyif  => 'grep -q "Error log" /var/log/apache2/error.log',
}

