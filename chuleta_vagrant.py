# Vagrant
    # Inicializar archivo de vagrant
    vagrant init
    #Archivo tipo
    Vagrant.configure("2") do |config|
        config.vm.box = "ubuntu/trusty64"
    end
    # Para subir maquina desde el Vagrantfile
    vagrant up
    # Apagar maquina virtual
    vagrant halt
    # Destruir maquina virtual
    vagrant destroy
    
