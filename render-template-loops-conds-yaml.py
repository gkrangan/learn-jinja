#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

import yaml

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template-loops.j2")

with open("interface_data.yml", "r") as f:
   interface_list = yaml.load(f)
   print (interface_list)
   print(template.render(interface_list=interface_list))
