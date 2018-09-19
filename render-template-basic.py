#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")


interface_dict = {
   "name" : "GigabitEthernet0/1",
   "description" : "Server Port",
   "vlan" : 10,
   "uplink" : False
}

class NetworkInterface(object):

   def __init__(self, name, description, vlan, uplink=False):
      self.name = name
      self.description = description
      self.vlan = vlan
      self.uplink = uplink

interface_object = NetworkInterface("GigabitEthernet0/1", "Server Port", 20)

#print(template.render(interface=interface_dict))
print(template.render(interface=interface_object))
