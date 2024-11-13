3dxmastree pihut3dxmastree thepihut3dxmastree

### Alternatives

https://github.com/davesteele/pihut-xmas-asyncio

https://gist.github.com/rbnpi/5f5e9356e627d1cbc52086efbb56456c

# The Pi Hut 3D Xmas Tree Examples

I tried to search for other examples of code but did not find anything relating to this specific The Pi Hut 3D Xmas tree one.
There is the standard 'twinkle' example provided, and then some other buyers posted their code in the review section. Unfortunately
the code from the reviews section is not indented, so it would not just run after copy and paste.

I copied all the examples I could find there and added them here, with full credits.

Why not setup a repository instead!? Lets share examples here, and then each Christmas we will have a lot of cool examples to choose from.

## Contributing

Please consider contributing new examples into this repository. Provide some full credits if you found code else where and some basic description.

- You can create an issue and label it `more-examples`
- Fork the repository and add your own code and merge back here

Visit [the Wiki](https://github.com/p10tyr/thepihut3dxmastree-examples/wiki) to find more examples.

## Setup

Please make sure to follow the setup instruction as on The Pi Hut site.

If you are having diffculties please look at the FAQ in the Wiki link

You can also run a full LED diagnostic program by running ```python diagnostics.py```

## Running the code

Make sure you have git installed.

If you're logging in with the default `pi` account, enter the following:

```shell
git clone https://github.com/p10tyr/thepihut3dxmastree-examples.git
```

This will pull the example code into the directory `/home/pi/thepihut3dxmastree-examples/examples`. If you use another account, the home directory name will change.

There is a simple script, `3dxmas.sh`, which will present a menu of examples to run. You will need to install the dialog package, then run the script.

```shell
sudo apt install dialog
./3dxmas.sh
```

You can also run each example manaully, for example:

```shell
cd /home/pi/thepihut3dxmastree-examples/examples
python thepihut.py
```

Each example will block the console, so if you want you can add & and it fork into a new thread and keep running.

## Autostart

The easiest way I found to get a Python script going was to use  crontab.

Edit the file

`sudo crontab -e`

Add this line which tells cront to run this command once after reboot

`@reboot python /home/pi/thepihut3dxmastree-examples/examples/thepihut.py &`

## Stop Autostart (or any other forked process)

If you want to stop the executing forked Python then you can use the following command to list all processes. Find the PID of your process (should be near bottom in the hundreds range) and then `sudo kill <pid>`

```shell
ps aux
sudo kill ####
```

## 2021 update

Hi there! Andy Piper (@andypiper) adjusted the code in this repo to bring it up-to-date for the latest Raspberry Pi OS distribution (based on Debian Bullseye), and to make it happier running with Python 3, which is now the default.

- corrected typos
- ran the [Python `2to3` program](https://docs.python.org/3/library/2to3.html) over the samples
- ran linters to format things nicely for readability
- re-tested the examples

Note: I'm running an original pre-soldered 3D Xmas Tree (the non-RGB version), on a Pi Zero 1.2 (pre-wireless version), on the Bullseye version on Raspberry Pi OS Lite.
