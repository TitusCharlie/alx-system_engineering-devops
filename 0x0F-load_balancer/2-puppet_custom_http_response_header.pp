# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Get the hostname of the server
$hostname = $facts['hostname']

# Configure Nginx with a custom HTTP response header
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                server_name _;

                add_header X-Served-By $hostname;

                location / {
                    # Your existing Nginx configuration goes here
                }
            }",
  notify  => Service['nginx'],
}

# Enable Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure => running,
  enable => true,
}

