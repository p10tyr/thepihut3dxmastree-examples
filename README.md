# The Pi Hut 3D Xmass Tree Examples
## thepihut3dxmastree-examples

Info

# Autostart 
The easiest way I found to get a python script going was to use the crontab

Edit the file

    sudo crontab -e

Add this line which tells cront to run this command once after reboot

    @reboot python /home/pi/thepihut3dxmastree-examples/examples/thepihit.py &
