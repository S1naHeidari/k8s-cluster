IMAGE_NAME = "hashicorp/bionic64"


Vagrant.configure("2") do |config|
    config.ssh.insert_key = false

    config.vm.provider "virtualbox" do |v|
        v.memory = 4096
        v.cpus = 8
    end
      
    config.vm.define "k8s-master" do |master|
        master.vm.box = IMAGE_NAME
        master.vm.network "private_network", ip: "192.168.56.10"
        master.vm.hostname = "k8s-master"
        master.vm.provision "ansible" do |ansible|
            ansible.playbook = "kubernetes-setup/master-playbook.yml"
            ansible.extra_vars = {
                node_ip: "192.168.56.10",
            }
        end
    end
end







# IMAGE_NAME = "hashicorp/bionic64"


# MASTERS_NUM = 1
# MASTERS_CPU = 8
# MASTERS_MEM = 4096

NODES_NUM_GROUP1 = 6
NODES_CPU_GROUP1 = 2
NODES_MEM_GROUP1 = 8192

NODES_NUM_GROUP2 = 10
NODES_CPU_GROUP2 = 4
NODES_MEM_GROUP2 = 16384

NODES_NUM_GROUP3 = 2
NODES_CPU_GROUP3 = 8
NODES_MEM_GROUP3 = 32768

NODES_NUM_GROUP4 = 1
NODES_CPU_GROUP4 = 8
NODES_MEM_GROUP4 = 4096



IP_BASE = "192.168.56."

Vagrant.configure("2") do |config|
    config.ssh.insert_key = false

    def exclude_vm(vm_name)
        # if vm_name == "k8s-group1-1"
        #     return true
        # elsif vm_name == "k8s-group1-2"
        #     return true
        # elsif vm_name == "k8s-group1-3"
        #     return true
        # elsif vm_name == "k8s-group1-4"
        #     return true
        # elsif vm_name == "k8s-group1-5"
        #     return true
        # elsif vm_name == "k8s-group1-6"
        #     return true
        # elsif vm_name == "k8s-group2-1"
        #     return true
        # elsif vm_name == "k8s-group2-2"
        #     return true
        # elsif vm_name == "k8s-group2-3"
        #     return true
        # elsif vm_name == "k8s-group2-4"
        #     return true
        # elsif vm_name == "k8s-group2-5"
        #     return true
        # elsif vm_name == "k8s-group2-6"
        #     return true
        # elsif vm_name == "k8s-group2-7"
        #     return true
        # elsif vm_name == "k8s-group2-8"
        #     return true
        # elsif vm_name == "k8s-group2-9"
        #     return true
        # elsif vm_name == "k8s-group2-10"
        #     return true
        # elsif vm_name == "k8s-group3-1"
        #     return true
        # elsif vm_name == "k8s-group3-2"
        #     return true
        # elsif vm_name == "k8s-group3-3"
        #     return true
        # elsif vm_name == "k8s-group3-3"
        #     return true
        # else
        #     return false
        # end
        return false
    end    


    (1..3).each do |j|
        unless exclude_vm("k8s-group1-#{j}")
            config.vm.define "k8s-group1-#{j}" do |node|
                node.vm.box = IMAGE_NAME
                node.vm.network "private_network", ip: "192.168.56.#{j + 10}"
                node.vm.hostname = "k8s-group1-#{j}"
                node.vm.provider "virtualbox" do |v|
                    v.memory = NODES_MEM_GROUP1
                    v.cpus = NODES_CPU_GROUP1
                end   
                node.vm.provision "ansible" do |ansible|
                    ansible.playbook = "kubernetes-setup/node-playbook.yml"
                    ansible.extra_vars = {
                        node_ip: "192.168.56.#{j + 10}",
                    }
                end
            end
        end
    end

    (1..5).each do |j|
        unless exclude_vm("k8s-group2-#{j}")
            config.vm.define "k8s-group2-#{j}" do |node|
                node.vm.box = IMAGE_NAME
                node.vm.network "private_network", ip: "192.168.56.#{j + 20}"
                node.vm.hostname = "k8s-group2-#{j}"
                node.vm.provider "virtualbox" do |v|
                    v.memory = NODES_MEM_GROUP2
                    v.cpus = NODES_CPU_GROUP2
                end   
                node.vm.provision "ansible" do |ansible|
                    ansible.playbook = "kubernetes-setup/node-playbook.yml"
                    ansible.extra_vars = {
                        node_ip: "192.168.56.#{j + 20}",
                    }
                end
            end
        end
    end

    (1..2).each do |j|
        unless exclude_vm("k8s-group3-#{j}")
            config.vm.define "k8s-group3-#{j}" do |node|
                node.vm.box = IMAGE_NAME
                node.vm.network "private_network", ip: "192.168.56.#{j + 30}"
                node.vm.hostname = "k8s-group3-#{j}"
                node.vm.provider "virtualbox" do |v|
                    v.memory = NODES_MEM_GROUP3
                    v.cpus = NODES_CPU_GROUP3
                end   
                node.vm.provision "ansible" do |ansible|
                    ansible.playbook = "kubernetes-setup/node-playbook.yml"
                    ansible.extra_vars = {
                        node_ip: "192.168.56.#{j + 30}",
                    }
                end
            end
        end
    end
    (1..NODES_NUM_GROUP4).each do |j|
        unless exclude_vm("k8s-group4-#{j}")
            config.vm.define "k8s-group4-#{j}" do |node|
                node.vm.box = IMAGE_NAME
                node.vm.network "private_network", ip: "192.168.56.#{j + 40}"
                node.vm.hostname = "k8s-group4-#{j}"
                node.vm.provider "virtualbox" do |v|
                    v.memory = NODES_MEM_GROUP4
                    v.cpus = NODES_CPU_GROUP4
                end   
                node.vm.provision "ansible" do |ansible|
                    ansible.playbook = "kubernetes-setup/node-playbook.yml"
                    ansible.extra_vars = {
                        node_ip: "192.168.56.#{j + 40}",
                    }
                end
            end
        end
    end
end
