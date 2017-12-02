# The Pi Hut 3D Xmass Tree Examples

I tried to search for other examples of code but did not find anything relating to this specific The Pi Hut 3D Xmas tree one. 
There is the standard 'twinkle' exmaple provided and then some other buyers posted their code in the review section. Unfortunately 
the code is not indented so would not just run after copy and paste.

I copied all the examples I could find there and added them here, with full credits.

Why not setup a repository isntead!? Lets share examples here and then by next Christmas we will have allot of cool examples to choose from.

# Contributing

Please consider contributing new examples into this repository. Provide some full credits if you found code else where and some basic description

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

# Stop Autostart (or any other forked)

If you want to stop the executing forked python then you can use the following command to list all processes. Find the PID of your process (should be near bottom in the hundreds range) and then sudo kill <pid>

    ps aux
    sudo kill ####
    
