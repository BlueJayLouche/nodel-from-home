# Copyright (c) 2014 Museum Victoria
# This software is released under the MIT license (see license.txt for details)

'''Moxa UDP Controller for Denon DN-700AV.'''

import socket

# Functions used by this node
def send_udp_string(msg):
  #open socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    sock.sendto(msg, (param_ipAddress, param_port))
  except socket.error, msg:
    print "error: %s\n" % msg
    local_event_Error.emit(msg)
  finally:
    if sock:
      sock.close()

# Local actions this Node provides
def local_action_MuteOn(arg = None):
  """{"title":"Mute on","desc":"Mutes this node.","group":"General"}"""
  print 'Action MuteOn requested - '+str(arg)
  send_udp_string('MUON\r')
  
def local_action_MuteOff(arg = None):
  """{"title":"Mute Off","desc":"Unmutes this node.","group":"General"}"""
  print 'Action MuteOff requested - '+str(arg)
  send_udp_string('MUOFF\r')

# Local events this Node provides
local_event_Error = LocalEvent('{"title":"Error","desc":"An error has occured while communicating with the device.","group":"General"}')
# local_event_Error.emit(arg)

# Parameters used by this Node
param_ipAddress = Parameter('{"desc":"The IP address to connect to.","schema":{"type":"string"},"value":"192.168.100.1"}')

param_port = Parameter('{"desc":"The Port to connect to.","schema":{"type":"integer"},"value":"4001"}')

def main(arg = None):
  # Start your script here.
  print 'Nodel script started.'
