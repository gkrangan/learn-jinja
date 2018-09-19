#!/usr/bin/env python

import yaml

with open("interface_data.yml", "r") as f:
#    print(f.read())
     result = yaml.load(f)
     print(result)
