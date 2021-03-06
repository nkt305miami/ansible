#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function
__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ["preview"],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_firewall
description:
    - Each network has its own firewall controlling access to and from the instances.
    - All traffic to instances, even from other instances, is blocked by the firewall
      unless firewall rules are created to allow it.
    - The default network has automatically created firewall rules that are shown in default
      firewall rules. No manually created network has automatically created firewall rules
      except for a default "allow" rule for outgoing traffic and a default "deny" for
      incoming traffic. For all networks except the default network, you must create any
      firewall rules you need.
short_description: Creates a GCP Firewall
version_added: 2.6
author: Google Inc. (@googlecloudplatform)
requirements:
    - python >= 2.6
    - requests >= 2.18.4
    - google-auth >= 1.3.0
options:
    state:
        description:
            - Whether the given object should exist in GCP
        choices: ['present', 'absent']
        default: 'present'
    allowed:
        description:
            - The list of ALLOW rules specified by this firewall. Each rule specifies a protocol
              and port-range tuple that describes a permitted connection.
        required: false
        suboptions:
            ip_protocol:
                description:
                    - The IP protocol to which this rule applies. The protocol type is required when creating
                      a firewall rule. This value can either be one of the following well known protocol
                      strings (tcp, udp, icmp, esp, ah, sctp), or the IP protocol number.
                required: true
            ports:
                description:
                    - An optional list of ports to which this rule applies. This field is only applicable
                      for UDP or TCP protocol. Each entry must be either an integer or a range. If not
                      specified, this rule applies to connections through any port.
                    - 'Example inputs include: ["22"], ["80","443"], and ["12345-12349"].'
                required: false
    description:
        description:
            - An optional description of this resource. Provide this property when you create
              the resource.
        required: false
    name:
        description:
            - Name of the resource. Provided by the client when the resource is created. The name
              must be 1-63 characters long, and comply with RFC1035. Specifically, the name must
              be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
              which means the first character must be a lowercase letter, and all following characters
              must be a dash, lowercase letter, or digit, except the last character, which cannot
              be a dash.
        required: false
    network:
        description:
            - 'URL of the network resource for this firewall rule. If not
              specified when creating a firewall rule, the default network is
              used: global/networks/default If you choose to specify this
              property, you can specify the network as a full or partial URL.
              For example, the following are all valid URLs:
              U(https://www.googleapis.com/compute/v1/projects/myproject/global/)
              networks/my-network projects/myproject/global/networks/my-network
              global/networks/default .'
        required: false
    source_ranges:
        description:
            - If source ranges are specified, the firewall will apply only to traffic that has
              source IP address in these ranges. These ranges must be expressed in CIDR format.
              One or both of sourceRanges and sourceTags may be set. If both properties are set,
              the firewall will apply to traffic that has source IP address within sourceRanges
              OR the source IP that belongs to a tag listed in the sourceTags property. The connection
              does not need to match both properties for the firewall to apply. Only IPv4 is supported.
        required: false
    source_tags:
        description:
            - If source tags are specified, the firewall will apply only to traffic with source
              IP that belongs to a tag listed in source tags. Source tags cannot be used to control
              traffic to an instance's external IP address. Because tags are associated with an
              instance, not an IP address. One or both of sourceRanges and sourceTags may be set.
              If both properties are set, the firewall will apply to traffic that has source IP
              address within sourceRanges OR the source IP that belongs to a tag listed in the
              sourceTags property. The connection does not need to match both properties for the
              firewall to apply.
        required: false
    target_tags:
        description:
            - A list of instance tags indicating sets of instances located in the network that
              may make network connections as specified in allowed[].
            - If no targetTags are specified, the firewall rule applies to all instances on the
              specified network.
        required: false
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: create a firewall
  gcp_compute_firewall:
      name: testObject
      allowed:
        - ip_protocol: 'tcp'
          ports:
            - "22"
      target_tags:
        - test-ssh-server
        - staging-ssh-server
      source_tags:
        - test-ssh-clients
      project: testProject
      auth_kind: service_account
      service_account_file: /tmp/auth.pem
      scopes:
        - https://www.googleapis.com/auth/compute
      state: present
'''

RETURN = '''
    allowed:
        description:
            - The list of ALLOW rules specified by this firewall. Each rule specifies a protocol
              and port-range tuple that describes a permitted connection.
        returned: success
        type: complex
        contains:
            ip_protocol:
                description:
                    - The IP protocol to which this rule applies. The protocol type is required when creating
                      a firewall rule. This value can either be one of the following well known protocol
                      strings (tcp, udp, icmp, esp, ah, sctp), or the IP protocol number.
                returned: success
                type: str
            ports:
                description:
                    - An optional list of ports to which this rule applies. This field is only applicable
                      for UDP or TCP protocol. Each entry must be either an integer or a range. If not
                      specified, this rule applies to connections through any port.
                    - 'Example inputs include: ["22"], ["80","443"], and ["12345-12349"].'
                returned: success
                type: list
    creation_timestamp:
        description:
            - Creation timestamp in RFC3339 text format.
        returned: success
        type: str
    description:
        description:
            - An optional description of this resource. Provide this property when you create
              the resource.
        returned: success
        type: str
    id:
        description:
            - The unique identifier for the resource.
        returned: success
        type: int
    name:
        description:
            - Name of the resource. Provided by the client when the resource is created. The name
              must be 1-63 characters long, and comply with RFC1035. Specifically, the name must
              be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
              which means the first character must be a lowercase letter, and all following characters
              must be a dash, lowercase letter, or digit, except the last character, which cannot
              be a dash.
        returned: success
        type: str
    network:
        description:
            - 'URL of the network resource for this firewall rule. If not
              specified when creating a firewall rule, the default network is
              used: global/networks/default If you choose to specify this
              property, you can specify the network as a full or partial URL.
              For example, the following are all valid URLs:
              U(https://www.googleapis.com/compute/v1/projects/myproject/global/)
              networks/my-network projects/myproject/global/networks/my-network
              global/networks/default .'
        returned: success
        type: str
    source_ranges:
        description:
            - If source ranges are specified, the firewall will apply only to traffic that has
              source IP address in these ranges. These ranges must be expressed in CIDR format.
              One or both of sourceRanges and sourceTags may be set. If both properties are set,
              the firewall will apply to traffic that has source IP address within sourceRanges
              OR the source IP that belongs to a tag listed in the sourceTags property. The connection
              does not need to match both properties for the firewall to apply. Only IPv4 is supported.
        returned: success
        type: list
    source_tags:
        description:
            - If source tags are specified, the firewall will apply only to traffic with source
              IP that belongs to a tag listed in source tags. Source tags cannot be used to control
              traffic to an instance's external IP address. Because tags are associated with an
              instance, not an IP address. One or both of sourceRanges and sourceTags may be set.
              If both properties are set, the firewall will apply to traffic that has source IP
              address within sourceRanges OR the source IP that belongs to a tag listed in the
              sourceTags property. The connection does not need to match both properties for the
              firewall to apply.
        returned: success
        type: list
    target_tags:
        description:
            - A list of instance tags indicating sets of instances located in the network that
              may make network connections as specified in allowed[].
            - If no targetTags are specified, the firewall rule applies to all instances on the
              specified network.
        returned: success
        type: list
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            allowed=dict(type='list', elements='dict', options=dict(
                ip_protocol=dict(required=True, type='str'),
                ports=dict(type='list', elements='str')
            )),
            description=dict(type='str'),
            name=dict(type='str'),
            network=dict(type='str'),
            source_ranges=dict(type='list', elements='str'),
            source_tags=dict(type='list', elements='str'),
            target_tags=dict(type='list', elements='str')
        )
    )

    state = module.params['state']
    kind = 'compute#firewall'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                fetch = update(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.put(link, resource_to_request(module)))


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#firewall',
        u'allowed': FirewallAllowedArray(module.params.get('allowed', []), module).to_request(),
        u'description': module.params.get('description'),
        u'name': module.params.get('name'),
        u'network': module.params.get('network'),
        u'sourceRanges': module.params.get('source_ranges'),
        u'sourceTags': module.params.get('source_tags'),
        u'targetTags': module.params.get('target_tags')
    }
    return_vals = {}
    for k, v in request.items():
        if v:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/firewalls/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/global/firewalls".format(**module.params)


def return_if_object(module, response, kind):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))
    if result['kind'] != kind:
        module.fail_json(msg="Incorrect result: {kind}".format(**result))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'allowed': FirewallAllowedArray(response.get(u'allowed', []), module).from_response(),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'id': response.get(u'id'),
        u'name': response.get(u'name'),
        u'network': response.get(u'network'),
        u'sourceRanges': response.get(u'sourceRanges'),
        u'sourceTags': response.get(u'sourceTags'),
        u'targetTags': response.get(u'targetTags')
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/global/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return None
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#firewall')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], 'message')
        time.sleep(1.0)
        if status not in ['PENDING', 'RUNNING', 'DONE']:
            module.fail_json(msg="Invalid result %s" % status)
        op_result = fetch_resource(module, op_uri, 'compute#operation')
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class FirewallAllowedArray(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = []

    def to_request(self):
        items = []
        for item in self.request:
            items.append(self._request_for_item(item))
        return items

    def from_response(self):
        items = []
        for item in self.request:
            items.append(self._response_from_item(item))
        return items

    def _request_for_item(self, item):
        return remove_nones_from_dict({
            u'IPProtocol': item.get('ip_protocol'),
            u'ports': item.get('ports')
        })

    def _response_from_item(self, item):
        return remove_nones_from_dict({
            u'IPProtocol': item.get(u'ip_protocol'),
            u'ports': item.get(u'ports')
        })


if __name__ == '__main__':
    main()
