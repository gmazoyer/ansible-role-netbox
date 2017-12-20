[![Build Status](https://travis-ci.org/respawner/ansible-role-netbox.svg?branch=master)](https://travis-ci.org/respawner/ansible-role-netbox)

# Ansible Role: Netbox

An Ansible Role that installs on Debian/Ubuntu.

This role install all dependencies required by Netbox including the PostgreSQL
database. So it can be used to setup a Netbox appliance including everything in
the same machine.

Web backend and frontend setups can be disabled if you already have your own
way to handle them. The database setup however needs some work to be able to
use a PostgreSQL database located on another machine.

## Dependencies

None.

## Roles Variables

Available variables are listed below, along with default values:

Setup for the PostgreSQL database:

    netbox_database: netbox
    netbox_database_user: netbox
    netbox_database_password: netbox
    netbox_database_host: localhost

Where to get Netbox and which version:

    netbox_version: v2.2.8
    netbox_git_url: https://github.com/digitalocean/netbox.git

Where to install Netbox:

    netbox_install_directory: /opt/netbox

FQDN accepted when trying to reach Netbox, a error 400 will be sent back to
the user if he does not use one of the listed FQDN:

    netbox_config_allowed_hosts: ['localhost', 'netbox.example.com']

A secret key that must be unique to each installation:

    netbox_config_secret_key: TO_CHANGE

Set the timezone to be used (a list of available TZs can be found
[here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)):

    netbox_config_time_zone: UTC

The username and email for the super user. Its password must be set manually
via the manage.py tool of the application:

    netbox_superuser_username: admin
    netbox_superuser_email: admin@example.com

NAPALM integration with username and password to be used when connecting to
devices:

    netbox_use_napalm: false
    netbox_devices_username: ''
    netbox_devices_password: ''

Whether or not to load the initial data of Netbox:

    netbox_load_initial_data: true

Configuration for the backend web servers:

    netbox_setup_web_backend: false
    netbox_gunicorn_address: 127.0.0.1
    netbox_gunicorn_port: 8001
    netbox_gunicorn_workers_number: 3
    netbox_gunicorn_user: root
    netbox_supervisor_user: root

Whether or not to configure the frontend web server:

    netbox_setup_web_frontend: false

## Example Playbook

    - hosts: netboxes
      roles:
        - { role: respawner.netbox }

## License

This Ansible Role is released under the terms of the GNU GPLv3. Please read
the LICENSE file for more information.

## Author Information

This role was created in 2017 by [Guillaume Mazoyer](https://respawner.fr).
