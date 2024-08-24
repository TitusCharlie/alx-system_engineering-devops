# This Puppet manifest automates the fix for Apache returning a 500 Internal Server Error
# by resolving common issues related to permissions and configurations.

file { '/var/www/html/wp-content':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

file { '/var/www/html/wp-content/plugins':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

file { '/var/www/html/wp-content/themes':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

exec { 'fix_permissions':
  command => 'find /var/www/html -type d -exec chmod 755 {} + && find /var/www/html -type f -exec chmod 644 {} +',
  path    => ['/bin', '/usr/bin'],
  user    => 'root',
  group   => 'root',
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => Exec['fix_permissions'],
}
