import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_all(host):
    # Check if NetBox has been installed in the right directory
    f = host.file("/opt/netbox/")

    assert f.exists
    assert f.user == "netbox"
    assert f.group == "netbox"
