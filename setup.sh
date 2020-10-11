## Step1 - change kernel to 5.0.0-23-generic and install andd update linux-headers-5.0.0-23-generic

# installing and setting up GO
wget https://dl.google.com/go/go1.14.4.linux-amd64.tar.gz
y
sudo tar -C /usr/local -zxvf go1.14.4.linux-amd64.tar.gzmkdir -p ~/go/{bin,pkg,src}
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export GOROOT=/usr/local/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin:$GOROOT/bin' >> ~/.bashrc
source ~/.bashrc

# installing mongo db
sudo apt -y update
sudo apt -y install mongodb wget git
y
sudo systemctl start mongodb

#installing other packages
sudo apt -y update
sudo apt -y install git gcc cmake autoconf libtool pkg-config libmnl-dev libyaml-dev
go get -u github.com/sirupsen/logrus

#network settings

sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o enf0s3 -j MASQUERADE
sudo systemctl stop ufw

#cloning and setting up the free5gc repo
cd ~
git clone --recursive -b v3.0.4 -j `nproc` https://github.com/free5gc/free5gc.git
y
cd free5gc
go mod download
make all

cd
git clone -b v0.2.0 https://github.com/PrinzOwO/gtp5g.git
y
cd gtp5g
make
sudo make install

sudo snap install code --classic

sudo apt install wireshark-qt
