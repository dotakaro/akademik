Cara isntall odoo dengan singkat (untuk keperluan development)

ini cara teringkat :)

STEP1 :

Pastikan kita bekerja dengan mode user root

$ sudo su -

STEP2 :

Update sistem
# apt-get update && apt-get upgrade

STEP3 :

Buat user dan password odoo, kemudian berikan hak sudo

# useradd -m -g sudo -s /bin/bash odoo
# passwd odoo
# adduser odoo sudo


STEP4 :

Login user odoo dengan putty pada window baru

STEP 5 :

$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install git
$ sudo apt-get install npm
$ sudo ln -s /usr/bin/nodejs /usr/bin/node
$ sudo npm install -g less less-plugin-clean-css

STEP 6 :

$ mkdir ~/odoo-dev
$ cd ~/odoo-dev
$ git clone https://github.com/odoo/odoo.git -b 10.0 --depth=1

STEP 7 :

$ ./odoo/setup/setup_dev.py setup_deps
$ ./odoo/setup/setup_dev.py setup_pg

STEP 8 :

Jalankan odoo

$ ~/odoo-dev/odoo/odoo-bin

atau

$./odoo-bin

pada folder odoo-dev


untuk mengakses odoo arahken ke ip masing-masing container
