# puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => template('my_module/ssh_config.erb'),
}

# Specify the private key file
file { '/home/freelance/.ssh/school':
  ensure  => present,
  source  => '/path/to/your/private/key',  # Update this path with the actual path to your private key
  mode    => '0600',
  owner   => 'freelance',
  group   => 'freelance',
}

# Create a template for the SSH client configuration
# Disable password authentication and specify the private key
file { '/etc/puppet/modules/my_module/templates/ssh_config.erb':
  ensure  => present,
  content => <<~CONTENT,
    Host *
      IdentityFile /home/freelance/.ssh/school
      PasswordAuthentication no
  CONTENT
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

