import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_all(host):
    # Check if NetBox has been installed in the right directory
    netbox_install_directory = host.file("/opt/netbox/")

    assert netbox_install_directory.exists
    assert netbox_install_directory.user == "netbox"
    assert netbox_install_directory.group == "netbox"
