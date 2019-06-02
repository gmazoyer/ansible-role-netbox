[![Build Status](https://travis-ci.org/respawner/ansible-role-netbox.svg?branch=master)](https://travis-ci.org/respawner/ansible-role-netbox)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-netbox-blue.svg)](https://galaxy.ansible.com/respawner/netbox)

# Ansible Role: NetBox

An Ansible Role that installs on Debian/Ubuntu.

This role install all dependencies required by NetBox including the PostgreSQL
database. So it can be used to setup a NetBox appliance including everything in
the same machine.

Web backend and frontend setups can be disabled if you already have your own
way to handle them.

## Dependencies

None.

## Roles Variables

Available variables are listed below, along with default values:

Setup for the PostgreSQL database:

    netbox_database: netbox
    netbox_database_user: netbox
    netbox_database_password: netbox
    netbox_database_host: localhost # This will force PostgreSQL to be setup

Where to get NetBox and which version:

    netbox_version: v2.5.13
    netbox_git_url: https://github.com/digitalocean/netbox.git

Where to install NetBox:

    netbox_install_directory: /opt/netbox

The username, password and email for the super user.

    netbox_superuser_username: admin
    netbox_superuser_password: admin
    netbox_superuser_email: admin@example.com

LDAP can be used as authentication mechanism. It must be enabled, and the whole
LDAP configuration has to be provided in the following variables (see NetBox
[documentation](http://netbox.readthedocs.io/en/latest/installation/ldap/)):

    netbox_setup_ldap_auth: false
    netbox_ldap_config: ""

NAPALM integration, please note that you must set the username and password for
NAPALM in the configuration otherwise it will not be enabled:

    netbox_use_napalm: false

Redis integration, this is used for enabling webhooks and requires
configuration settings to be set to:

    netbox_use_webhooks: false

Whether or not to load the initial data of NetBox:

    netbox_load_initial_data: true

The configuration for NetBox must be given as `key: value` pairs like the
following, please note that the secret key does not need to be given as it will
be generated automatically:

    netbox_config:
      ALLOWED_HOSTS:
        - localhost
        - 127.0.0.1
      TIME_ZONE: "Europe/Paris"
      …

Configuration for the backend web servers:

    netbox_setup_web_backend: false
    netbox_gunicorn_address: 127.0.0.1
    netbox_gunicorn_port: 8001
    netbox_gunicorn_workers_number: 4

Whether or not to configure the frontend web server:

    netbox_setup_web_frontend: false

## Example Playbook

    - hosts: netboxes
      roles:
        - { role: respawner.netbox }

## License

This Ansible Role is released under the terms of the GNU GPLv3. Please read
the `LICENSE` file for more information.

Portions of this role include MIT-licensed code (see `7c400dd`) and are
demarcated in the header. See `LICENSE-MIT` for more information.

## Author Information

This role was created in 2017 by [Guillaume Mazoyer](https://respawner.fr).
