import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_install_directory(host):
    netbox_install_directory = host.file("/opt/netbox/")

    assert netbox_install_directory.exists
    assert netbox_install_directory.user == "netbox"
    assert netbox_install_directory.group == "netbox"


def test_systemd_services(host):
    services = ["netbox.service", "netbox-rqworker.service"]

    for service in services:
        s = host.service(service)
        assert s.is_enabled
        assert s.is_running


def test_http_webserver(host):
    assert host.socket("tcp://0.0.0.0:80")
