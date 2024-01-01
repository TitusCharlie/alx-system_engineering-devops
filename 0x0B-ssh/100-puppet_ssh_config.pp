# puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => epp('my_module/ssh_config.erb'),
}

file { '/home/freelance/.ssh/school':
  ensure  => present,
  source  => '/path/to/your/private/key',  # Update this path with the actual path to your private key
  mode    => '0600',
  owner   => 'freelance',
  group   => 'freelance',
}

# Create a template for the SSH client configuration
# Disable password authentication and specify the private key
epp { '/etc/puppet/modules/my_module/templates/ssh_config.erb':
  ensure  => present,
  source  => 'puppet/ssh_config.erb',
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

