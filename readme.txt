配置文件是etc/srun.conf，修改username和server，不要改动格式。先运行fuck.py文件，会生成fuck.txt文件，里面包含加密后的用户名，在路由器中选择pppoe，填入这个用户名和你的密码(密码并没有加密)

路由器root后用winscp登陆，根目录覆盖文件，putty ssh到路由器 opkg update && opkg install python，如果出现错误看一下路由器的内核

如果是pandorabox的内核(极路由之类)
cd /tmp 

wget http://downloads.openwrt.org.cn/PandoraBox/ralink/mt7620_old/packages/python_2.7.3-2_ralink.ipk

opkg install python_2.7.3-2_ralink.ipk

重启路由器