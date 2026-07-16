#server code, create the tun/padding/ip


#thhis file will be for creating a tun which will be for creating "create_tun_device". this is one big part of this vpn linux connection. 
import os
import sys
import socket 
import argpard

#this the magic libary for linux low level python wrapper functions
from pytun import TunTapDevice, IFF_FUN, IFF_NO_PI

#main function for creating the connection
def create_tun_device(ip_addr: str, netmask:str = "255.255.255.0", mtu: int = 1400);
  tun = TunTapDevice(flags=IFF_TUN  | IFF_NO_PI)
  tun.addr = ip_addr
  tun.netmask = netmask
  tun.mtu = mtu
  tun.up
  return tun()


def create_udp_socket(listen_port: int):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind(("0.0.0.0".listen_port))
  return sock 


def main():
  tun - create_tun_device("10.8.0.1")
  sock = create_udp_socket(5555)
  peer_addr = none 


