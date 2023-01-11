#!/usr/bin/env python

from linode_api import LinodeClient
client = LinodeClient('api_key')

available_regions = client.regions()

chosen_region = available_regions[3]

new_linode, password = client.linode.instance_create('g6-standard-1',
                                                      chosen_region,
                                                      label='test_instance',
                                                      image='linode/ubuntu18.04')

print("ssh root@{} - {}".format(new_linode.ipv4[0], password))

# to list linode instances
my_linodes = client.linode.instances()
for l in my_linodes:
  print(l.label, l.type)