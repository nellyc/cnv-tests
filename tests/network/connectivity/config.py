from tests.network.config import *  # noqa: F403

#  GENERAL
SVC_CMD = "oc create serviceaccount privileged-test-user -n {ns}".format(ns=NETWORK_NS)  # noqa: F405
SVC_DELETE_CMD = "oc delete serviceaccount privileged-test-user -n {ns}".format(ns=NETWORK_NS)  # noqa: F405
ADM_CMD = "oc adm policy add-scc-to-user privileged -z privileged-test-user"
IP_ADDR_ADD = "ip addr add {ip} dev {dev}"
CREATED_BRIDGES = set()
IP_LINK_SHOW_BETH_CMD = 'bash -c "ip -o link show type veth | wc -l"'

#  VMS
VMS = {
    "vm-fedora-1": {
        "pod_ip": None,
        "ovs_ip": "192.168.0.1",
        "bond_ip": "192.168.1.1"
    },
    "vm-fedora-2": {
        "pod_ip": None,
        "ovs_ip": "192.168.0.2",
        "bond_ip": "192.168.1.2"
    }
}
VMS_LIST = list(VMS.keys())
VM_YAML_TEMPLATE = "tests/manifests/network/vm-template-fedora-multus.yaml"

#  PODS
PRIVILEGED_PODS = []
PRIVILEGED_DAEMONSET_YAML = "tests/manifests/privileged-pod.yml"

#  NODES
OVS_NODES_IPS = ["192.168.0.3", "192.168.0.4"]
IP_LINK_VETH_CMD = "bash -c 'ip -o link show type veth | wc -l'"
GET_NICS_CMD = "bash -c 'ls -l /sys/class/net/ | grep -v virtual | grep net | rev | cut -d '/' -f 1 | rev'"
GET_NIC_STATE_CMD = "cat /sys/class/net/{nic}/operstate"
GET_DEFAULT_GW_CMD = "ip route show default"

#  OVS
OVS_VLAN_YAML = "tests/manifests/network/ovs-vlan-net.yml"
OVS_NO_VLAN_PORT = "ovs_novlan_port"
OVS_VSCTL_ADD_BR = "ovs-vsctl add-br {bridge}"
OVS_VSCTL_ADD_PORT = "ovs-vsctl add-port {bridge} {interface}"
OVS_VSCTL_DEL_BR = "ovs-vsctl del-br {bridge}"

#  VXLAN
BRIDGE_NAME_VXLAN = "br1_for_vxlan"
OVS_VSCTL_ADD_VXLAN = "ovs-vsctl add-port {bridge} vxlan -- set Interface vxlan type=vxlan options:remote_ip={ip}"
OVS_VSCTL_ADD_PORT_VXLAN = "ovs-vsctl add-port {bridge} {port_1} -- set Interface {port_2} type=internal"

# BOND
BOND_SUPPORT_ENV = None
OVS_BOND_YAML = "tests/manifests/network/ovs-net-bond.yml"
BOND_NAME = "bond1"
BOND_BRIDGE = "br1_for_bond"
IP_LINK_ADD_BOND = "ip link add {bond} type bond".format(bond=BOND_NAME)
IP_LINK_SET_BOND_PARAMS = "ip link set {bond} type bond miimon 100 mode active-backup".format(bond=BOND_NAME)
IP_LINK_DEL_BOND = "ip link del {bond}".format(bond=BOND_NAME)
IP_LINK_INTERFACE_DOWN = "ip link set {interface} down"
IP_LINK_SET_INTERFACE_MASTER = "ip link set {interface} master {bond}"
IP_LINK_INTERFACE_UP = "ip link set {interface} up"
IP_LINK_SHOW = "ip link show {interface}"

# REAL NICS
REAL_NICS_ENV = None
CHECK_NIC_DRIVER_CMD = "bash -c 'basename $(readlink -f /sys/class/net/{nic}/device/driver/module/)'"
BRIDGE_NAME_REAL_NICS = "br1_real_nics"


ALL_BRIDGES = [BRIDGE_NAME_REAL_NICS, BRIDGE_NAME_VXLAN, BOND_BRIDGE]
