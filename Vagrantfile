Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04-arm64"  # 使用適合 ARM64 的 box
  # 不指定版本，讓 Vagrant 自動選擇最新的 不相容在說

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provider "vmware_fusion" do |v|
    v.vmx["memsize"] = "1024"#1g
    v.vmx["numvcpus"] = "2"#2核
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update #安裝pip 跟 venv 
    sudo apt-get install -y python3-venv zip
    touch /home/vagrant/.bash_aliases
    echo "alias python='python3'" >> /home/vagrant/.bash_aliases #把python3 替換成python 
  SHELL
end
