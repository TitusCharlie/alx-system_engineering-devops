# puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "#!/usr/bin/env bash\n
# SSH client configuration\n\n
Host *\n
        PasswordAuthentication no\n
        IdentityFile ~/.ssh/school\n
        SendEnv LANG LC_*\n
        HashKnownHosts yes\n
        GSSAPIAuthentication yes\n
        GSSAPIDelegateCredentials no\n",
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}

