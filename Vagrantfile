# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'ubuntu/trusty64'

  config.vm.define :worker do |worker|
    worker.vm.hostname = 'worker'
    worker.vm.network :private_network, ip: '192.168.0.20'
    # Sync to /vagrant on guest from current directory.
    worker.vm.synced_folder '.', '/vagrant', type: 'virtualbox'
  end
end
