# OLA_OSC_converter
receive DMX data with OLA and send out custom OSC messages

This is a example based on  
https://www.openlighting.org/ola/developer-documentation/python-api/#Receiving_DMX  
and  
https://pypi.python.org/pypi/python-osc#simple-client  
http://stackoverflow.com/a/22152877/574981

some other resources that where useful
--
http://stackoverflow.com/questions/22135511/a-plethora-of-python-osc-modules-which-one-to-use

pyOSC  
https://pypi.python.org/pypi/pyOSC (python2)   
https://trac.v2.nl/wiki/pyOSC

python-osc  
https://pypi.python.org/pypi/python-osc (python3)

i used this script to test basic osc communication (uses pyOSC)  
https://gist.github.com/MCDELTAT/9811174#file-osctest-py


installation / use
--

installed and running ola (https://www.openlighting.org/ola/)  
installed python-osc (https://pypi.python.org/pypi/python-osc)  
for me this worked on kubuntu 16.04:
with use of python 2.7.12
```
$ sudo -H pip2 install pyOSC
```
run with
```
$ python2 ola_osc_converter.py
```

you could try with python3  
(for this you have to change the script - comment out the pyOSC things and uncomment the python-osc lines..)
```
$ sudo -H pip3 install python-osc
```
```
$ python3 ola_osc_converter.py
```
or
