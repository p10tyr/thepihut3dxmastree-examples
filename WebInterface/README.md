# The Pi Hut 3D Xmass Tree Examples - WebServer

If you are running your pi headless (no screen no keyboard), you may need a way to shut it down properly ot to switch between scripts.
If you use the lighttpd solution, please keep your raspberry in private network, no protection is assigned to it.
This is not the most modern solution nor the cleaner, but it does the job and is easly deployed.

# Setup WebServer

If you do not have a running web server you can install lighttpd.

	sudo apt-get update && sudo apt-get install lighttpd php-cgi
	sudo lighty-enable-mod fastcgi fastcgi-php
	sudo service lighttpd force-reload

# Prepare sudos
Launch sudos ```sudo visudo```

Add the following line below "pi ALL etc." and exit the visudo editor (```ctrl+x``` then ```yes```)

    www-data ALL = NOPASSWD: /sbin/shutdown
    www-data ALL = NOPASSWD: /usr/bin/python
    www-data ALL = NOPASSWD: /usr/bin/pkill

# Prepare one php file per script
It should kill previous python running tasks and then start the new one.
Create one per script, edit the path accordingly to your website
	sudo nano /var/www/html/cascade-dj.php
	
Edit the path accordingly to where you cloned the repo.

	<?php 
	 system('sudo pkill -9 python');
	 shell_exec('sudo python /home/pi/thepihut3dxmastree-examples/examples/cascade-dj.py >/dev/null 2>&1 &');
	 ?>
	<html><body><a href="index.html">index</a></body></html>

# Create a shutdown page
create the page ```sudo nano /var/www/html/shutdown.php```

	<?php system('sudo /sbin/shutdown -h now'); ?>	
	
# Prepare an index file listing all html page
Make sure you have git installed.
Create the page ```sudo nano /var/www/html/index.html```

List in the file all the php files you just created

	<html><body><a href="shutdown.php">Shutdown NOW</a><br>
		<a href="random.php">random</a><br>
		<a href="pi.php">pi</a><br>
		<a href="dj.php">dj</A><br>
		<a href="kj.php">kjetil</A><br>
		<a href="sp.php">spining</A><br>
	</body>
	</html>

# Connect to the page
Now you can shutdown safely or change the tree script.
If you don't know the ip of your raspberrypi, you can sometime access it via:

	http://raspberrypi.local
	http://raspberrypi/index.html

# Credits
Initial idea for the reboot page was found in the pi forum by user **ednl**

[https://www.raspberrypi.org/forums/viewtopic.php?t=58802](https://www.raspberrypi.org/forums/viewtopic.php?t=58802)
