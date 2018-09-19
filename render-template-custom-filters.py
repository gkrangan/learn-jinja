#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

import yaml

def get_interface_speed(interface_name):
   if "gigabit" in interface_name.lower():
      return 1000
   elif "fast" in interface_name.lower():
      return 100

ENV = Environment(loader=FileSystemLoader('.'))
ENV.filters['get_interface_speed'] = get_interface_speed
template = ENV.get_template("template-using-custom-filter.j2")

with open("interface_mixed_data.yml", "r") as f:
   interface_list = yaml.load(f)
   print (interface_list)
   print(template.render(interface_list=interface_list))
