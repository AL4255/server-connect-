#thhis file will be for creating a tun which will be for creating "create_tun_device". this is one big part of this vpn linux connection. 
import os
import sys
import socket 
import argpard

#this the magic libary for linux low level python wrapper functions
from pytun import TunTapDevice, IFF_FUN, IFF_NO_PI
