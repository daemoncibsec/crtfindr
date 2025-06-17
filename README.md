<h1 align="center">
  <img src="https://github.com/daemoncibsec/crtfindr/blob/main/crtfindr-logo.png" alt="crtfindr" width="1000px">
  <br>
</h1>

Crtfindr is a tool that allows the user to obtain any information regarding the certificates about any given webpage. It's written in Python and shines specially in Bug Bounty, where any information related to the target is extremely important.

## Installation

```bash
git clone https://github.com/daemoncibsec/crtfindr.git
pip install simplejson 
pip install argparse
pip install requests
cd crtfindr
```

Additionally, you can make it a binary in Linux systems using these "cython" library, so you don't have to move between folders, and have it implemented in your system as well as with other commands.

```bash
pip install cython
python3 -m cython crtfindr.py --embed
gcc -Os $(python3-config --includes) crtfindr.c -o crtfindr $(python3-config --ldflags --embed)
sudo cp crtfindr /usr/bin/
```
## Usage/Examples

```bash
python3 crtfindr.py -h
```

In case you have the script compiled with cython and gcc:

```bash
crtfindr -h
```
## Authors

- [@daemoncibsec](https://www.github.com/daemoncibsec)
