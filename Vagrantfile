# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Vagrant box from https://atlas.hashicorp.com/centos/boxes/7
  config.vm.box = 'ubuntu/trusty64'

  # Proxy configuration
  if Vagrant.has_plugin?('vagrant-proxyconf')
   config.proxy.http     = 'http://proxy.occ.co.jp:8080'
   config.proxy.https    = 'http://proxy.occ.co.jp:8080'
   config.proxy.no_proxy = 'localhost,127.0.0.1,.es.occ.co.jp'
  end

  # Operation machine
  config.vm.define :worker do |worker|
    worker.vm.hostname = 'worker'
    worker.vm.network :private_network, ip: '192.168.0.20'
    # Sync to /vagrant on guest from current directory.
    worker.vm.synced_folder '.', '/vagrant', type: 'virtualbox'
  end
end
