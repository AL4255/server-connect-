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
  peer_addr = None

  try: 
    while True:
      ready, _, _ = select.select([tun,sock], [], [])

      if tun in ready:
          packet = os.read(tun.fileno(), tun.mtu + 100)
          print(f"Got {len(packet)} bytes from TUN")
          if peer_addr:
            sock.sendto(packet, peer_addr)

      if socl in ready:
          data, addr = sock.recvfrom(tun.mtu + 100)
          if peer_addr is None:
              print(f"Client connecte from {addr}")
          peer_addr = addr
          os.write(tun.fileno(), data)


  finally:
    tun.down()
    sock.close()
if __name__ == "__main__"
    main()


