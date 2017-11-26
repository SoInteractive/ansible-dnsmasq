from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_packages(host):
    present = [
        "dnsmasq"
    ]
    if present:
        for package in present:
            p = host.package(package)
            assert p.is_installed


def test_files(host):
    present = [
        "/etc/dnsmasq.conf",
        "/etc/dnsmasq.d/records.conf",
        "/etc/dnsmasq.d/dhcp_mac.conf",
        "/etc/dnsmasq.d/addn_hosts"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_services(host):
    present = [
        "dnsmasq"
    ]
    for service in present:
        s = host.service(service)
        assert s.is_enabled
        assert s.is_running


def test_socket(host):
    present = [
        # "unix:///run/haproxy/admin.sock",
        "tcp://127.0.0.1:53",
        "tcp://127.0.0.1:9153"
    ]
    for socket in present:
        s = host.socket(socket)
        assert s.is_listening
