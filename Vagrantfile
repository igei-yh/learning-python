# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Vagrant box from https://atlas.hashicorp.com/centos/boxes/7
  config.vm.box = 'ubuntu/trusty64'

  # Operation machine
  config.vm.define :worker do |worker|
    worker.vm.hostname = 'worker'
    worker.vm.network :private_network, ip: '192.168.0.20'
    # Sync to /vagrant on guest from current directory.
    worker.vm.synced_folder '.', '/vagrant', type: 'virtualbox'
  end
end
