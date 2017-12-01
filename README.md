# The Pi Hut 3D Xmass Tree Examples
## thepihut3dxmastree-examples

# Setup

Please make sure to follow the setup instruction as on The Pi Hut site.

# Pulling the code

Make sure you have git installed.

Then if you logging in with the default pi account you type in the following

    git pull https://github.com/ppumkin/thepihut3dxmastree-examples.git

That will pull the example code into the directory /home/pi/thepihut3dxmastree-examples/examples
Obviosly if you use another account the home directory name will change

You can then either set the autostart or run each example manaully, for example

    cd /home/pi/thepihut3dxmastree-examples/examples
    python thepihut.py

That will block the console so if you want you can add & and it fork into a new thread and keep running

# Autostart 
The easiest way I found to get a python script going was to use the crontab

Edit the file

    sudo crontab -e

Add this line which tells cront to run this command once after reboot

    @reboot python /home/pi/thepihut3dxmastree-examples/examples/thepihit.py &
