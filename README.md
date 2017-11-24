<p><img src="https://upload.wikimedia.org/wikipedia/commons/2/25/Hourglass_2.svg" alt="time logo" title="time" align="right" height="60" /></p>

Ansible Role: NTP sync
======================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-dnsmasq.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-dnsmasq) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.dnsmasq-blue.svg)](https://galaxy.ansible.com/SoInteractive/dnsmasq/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-dnsmasq.svg)](https://github.com/SoInteractive/ansible-dnsmasq/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

dnsmasq configuration role

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.dnsmasq
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

