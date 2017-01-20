#!/bin/sh -

import httplib
import json
 
class StaticFlowPusher(object):
 
    def __init__(self, server):
        self.server = server
 
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
 
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
 
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
 
    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret
 
pusher = StaticFlowPusher('127.0.0.1')

flow1 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_1",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.1",
     "ipv4_dst":"10.0.0.2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "instruction_apply_actions":"push_sdn_tunnel=src_ip:192.168.1.1; dst_ip:192.168.1.2; id_length:3; tun_id1:1; tun_id2:2; tun_id3:3,output=2",
    "hard_timeout":"0"
    }

flow2 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow_mod_2",
    "eth_type":"0x0800",
    "ipv4_src":"192.168.1.1",
     "ipv4_dst":"192.168.1.2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "instruction_apply_actions":"pop_sdn_tunnel,output=1",
    "hard_timeout":"0"
    }

flow3 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow_mod_3",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.1",
     "ipv4_dst":"10.0.0.2",
    "cookie":"0",
    "priority":"32768",
    "active":"true",
    "instruction_apply_actions":"output=1",
    "hard_timeout":"30"
    }

flow4 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_4",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.1",
     "ipv4_dst":"10.0.0.2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "instruction_apply_actions":"push_gre_tunnel=src_ip:192.168.1.1; dst_ip:192.168.1.2,output=2",
    "hard_timeout":"0"
    }

flow5 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow_mod_5",
    "eth_type":"0x0800",
    "ipv4_src":"192.168.1.1",
     "ipv4_dst":"192.168.1.2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "instruction_apply_actions":"pop_gre_tunnel,output=1",
    "hard_timeout":"0"
    }

flow6 = {
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_mod_6",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.1",
     "ipv4_dst":"10.0.0.2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "instruction_apply_actions":"push_vxlan_tunnel=src_ip:192.168.1.1; dst_ip:192.168.1.2; vx_vni:0,output=2",
    "hard_timeout":"0"
    }

flow7 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow_mod_7",
    "eth_type":"0x0800",
    "ipv4_src":"192.168.1.1",
     "ipv4_dst":"192.168.1.2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "instruction_apply_actions":"pop_vxlan_tunnel,output=1",
    "hard_timeout":"0"
    }
 
#pusher.set(flow1)
#pusher.set(flow2)
#pusher.set(flow3)
#pusher.set(flow4)
#pusher.set(flow5)
pusher.set(flow6)
pusher.set(flow7)