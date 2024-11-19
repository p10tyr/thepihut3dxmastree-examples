#3dxmastree #pihut3dxmastree #thepihut3dxmastree

# 🎄 3D Christmass tree examples 

I tried to search for other examples of code but did not find anything relating to this specific The Pi Hut 3D Xmas tree one.
There is the standard 'twinkle' example provided, and then some other buyers posted their code in the review section. Unfortunately
the code from the reviews section is not indented, so it would not just run after copy and paste.

I copied all the examples I could find there and added them here, with full credits.

Why not setup a repository instead!? Lets share examples here, and then each Christmas we will have a lot of cool examples to choose from.

### Alternatives

https://github.com/davesteele/pihut-xmas-asyncio

https://github.com/rendzina/XmasTree (3D RGB examples)

https://github.com/mcrigby/rgbxmastree (Run using .NET using this Nuget Package)

https://gist.github.com/rbnpi/5f5e9356e627d1cbc52086efbb56456c


## The Pi Hut - 3D Xmas Tree for Raspberry Pi - Examples 

Tested and working sinve 2017

(Pi 1, Pi2, Pi3, Pi Zero, Pi Zero W)

## The Pi Hut - 3D RGB Xmas Tree for Raspberry Pi - Examples 

I guess I gotta buy one. Will upadate with any info 😁

Comment found on PiHut to use esp8233 and Aircookie WLED project (which is an awesome project for everything LED!)
> This has 25 APA102 LEDs which run using SPI, so there are only 4 pins used: 5v, ground, clock and data. I decided not to use a raspiberry pi for this and instead hooked it up to a nodemcu (esp8266) which has integrated wifi. I connected pin 39 from the tree to ground on the nodemcu, pin 2 to 5v, pin 31 to D4 and pin 23 to D3. No external power or level shifter is required.
> 
> I then flashed the excellent WLED by Aircookie - https://github.com/Aircoookie/WLED (make sure you grab the APA102 variant from the available bin files)which has tons of effects and features all easily controlled by the android/ios apps, web page or home assistant etc. You can even sync the effects and colours with other sets of completely independent lights over wifi!
> The end result is fantastic - https://www.dropbox.com/s/33y8pq1oxk8kfd8/20191214_201640.jpg?dl=0
> Image pasted below in case you dont fancy checking drop box links

# Setup

Please make sure to follow the setup instruction as on The Pi Hut site.

If you are having diffculties please look at the FAQ in the Wiki link

You can also run a full LED diagnostic program by running ```python diagnostics.py```

## Running the code

Make sure you have git installed.

If you're logging in with the default `pi` account, enter the following:

```shell
~ $ > git clone https://github.com/p10tyr/thepihut3dxmastree-examples.git
```

This will pull the example code into your home directory `~/thepihut3dxmastree-examples`

You can also run each example manaully, for example:

```shell
~ $ > cd ~/thepihut3dxmastree-examples/examples
~/thepihut3dxmastree-examples/examples $ > python3 thepihut.py
```

Or there is a simple script, `3dxmas.sh`, which will present a menu of examples to run. You will need to install the dialog package, then run the script.

```shell
~/thepihut3dxmastree-examples $ > sudo apt-get install dialog
~/thepihut3dxmastree-examples $ > ./3dxmas.sh
```

Each example will block the console, so if you want you can add & and it fork into a new thread and keep running.

## Autostart

The easiest way I found to get a Python script going was to use  crontab.

Edit the file without sudo to create a a cron tab that will run as your user. (If you have sudo that runs as root and wont work)

`crontab -e`

Add this line which tells cront to run this command once after reboot.

`@reboot python3 ~/thepihut3dxmastree-examples/examples/thepihut.py &`

Change `../thepihut.py` to any file you would like running forked on boot

## Stop Autostart (or any other forked process)

If you want to stop the executing forked Python then you can use the following command to list all processes. Find the PID of your process (should be near bottom in the hundreds range) and then `sudo kill <pid>`

```shell
ps aux
sudo kill ####
```

## Contributing

Please consider contributing new examples into this repository. Provide some full credits if you found code else where and some basic description.

- You can create an issue and label it `more-examples`
- Fork the repository and add your own code and merge back here

Visit [the Wiki](https://github.com/p10tyr/thepihut3dxmastree-examples/wiki) to find more examples.



### Images

Xmas Tree RGB running on esp8266 and WLED
![image](https://github.com/user-attachments/assets/3161544f-5292-4f8e-9b72-27286361ca8d)


## 2024 update
Mainly updated the readme to reflect repo name change and use python3. 
Checked everything out and still seems to work fine.

## 2021 update

Hi there! Andy Piper (@andypiper) adjusted the code in this repo to bring it up-to-date for the latest Raspberry Pi OS distribution (based on Debian Bullseye), and to make it happier running with Python 3, which is now the default.

- corrected typos
- ran the [Python `2to3` program](https://docs.python.org/3/library/2to3.html) over the samples
- ran linters to format things nicely for readability
- re-tested the examples

Note: I'm running an original pre-soldered 3D Xmas Tree (the non-RGB version), on a Pi Zero 1.2 (pre-wireless version), on the Bullseye version on Raspberry Pi OS Lite.
