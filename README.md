[![CI](https://github.com/gmazoyer/ansible-role-netbox/workflows/CI/badge.svg?event=push)](https://github.com/gmazoyer/ansible-role-netbox/actions?query=workflow%3ACI)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-netbox-blue.svg)](https://galaxy.ansible.com/gmazoyer/netbox)

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

```
netbox_database: netbox
netbox_database_user: netbox
netbox_database_password: netbox
netbox_database_host: localhost # This will force PostgreSQL to be setup
```

Where to get NetBox and which version:

```
netbox_version: latest
netbox_git_url: https://github.com/netbox-community/netbox.git
```

By default, it will always get the latest stable version. A specific version
can be enforced by using, `v3.5.1` for example.

Where to install NetBox:

```
netbox_install_directory: /opt/netbox
```

The username, password and email for the super user.

```
netbox_superuser_username: admin
netbox_superuser_password: admin
netbox_superuser_email: admin@example.com
```

LDAP can be used as authentication mechanism. It must be enabled, and the whole
LDAP configuration has to be provided in the following variables (see NetBox
[documentation](https://netbox.readthedocs.io/en/stable/installation/6-ldap/)):

```
netbox_setup_ldap_auth: false
netbox_ldap_config: ""
```

Other Python packages can be installed using `local_requirements.txt`, this is
useful to install packages such as NAPALM or plugins:

```
netbox_local_requirements:
  - napalm
  …
```

The configuration for NetBox must be given as `key: value` pairs like the
following, please note that the secret key does not need to be given as it will
be generated automatically:

```
netbox_config:
  ALLOWED_HOSTS:
    - localhost
    - 127.0.0.1
  TIME_ZONE: "Europe/Paris"
  …
```

The housekeeping command is run using a systemd timer configured at 4:30AM UTC
every day. You can use `on_unit_active_sec: 12h` instead of `on_calendar` to
run the housekeeping command every 12 hours (for example).

```
netbox_systemd_timers:
  netbox-housekeeping:
    enabled: true
    command: "{{ netbox_virtualenv_path }}/bin/python {{ netbox_install_directory }}/netbox/manage.py housekeeping"
    on_calendar: "*-*-* 4:30:00 UTC"
```

Configuration for the backend web server and systemd:

```
netbox_setup_systemd: false
netbox_gunicorn_address: 127.0.0.1
netbox_gunicorn_port: 8001
netbox_gunicorn_workers_number: 5
```

Whether or not to configure the frontend web server:

```
netbox_setup_web_frontend: false
```

SSL/TLS configuration for the frontend web server:
...
netbox_web_tls: false
netbox_web_tls_port: 443
# netbox_web_tls_crt: /etc/pki/server.crt
# netbox_web_tls_key: /etc/pki/server.key
# netbox_web_tls_chain:
netbox_web_tls_redirect: false
...

## Example Playbook

```
- hosts: netboxes
  roles:
    - { role: gmazoyer.netbox }
```

## License

This Ansible Role is released under the terms of the GNU GPLv3. Please read
the `LICENSE` file for more information.

Portions of this role include MIT-licensed code (see `7c400dd`) and are
demarcated in the header. See `LICENSE-MIT` for more information.

## Author Information

This role was created in 2017 by [Guillaume Mazoyer](https://mazoyer.eu).
