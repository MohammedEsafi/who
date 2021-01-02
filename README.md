# Who's

Python script to find devices connected to your network ‒ supported only Linux

## Installation

Install the required Python dependencies using ```pip3```:

```
$ pip3 install python-nmap
```

## Running

run the script using

```
$ sudo python3 .
```

the result will be shown like below

```
+ ----- + ------------- + -------------------- + ------------- +
| No.   + Devices       + MAC Address          + IP Address    |
+ ----- + ------------- + -------------------- + ------------- +
| 0     + ROUTER        + KO:98:02:YO:HH:00    + 192.168.1.1   |
+ ----- + ------------- + -------------------- + ------------- +
| 1     + README S0     + F8:O9:P2:I2:89:20    + 192.168.1.20  |
+ ----- + ------------- + -------------------- + ------------- +
| 2     + Apple V0      + UI:OK:96:20:30:00    + 192.168.1.40  |
+ ----- + ------------- + -------------------- + ------------- +
```