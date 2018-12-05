from mininet.util import dumpNodeConnections
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI

class SingleSwitchTopo(Topo):
	def build(self):
		#build switches and hosts in the net
		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')
		switch3 = self.addSwitch('s3')
		switch4 = self.addSwitch('s4')
		switch5 = self.addSwitch('s5')
		switch6 = self.addSwitch('s6')
		switch7 = self.addSwitch('s7')
		switch8 = self.addSwitch('s8')
		switch9 = self.addSwitch('s9')
		host1 = self.addHost('h1')
		host2 = self.addHost('h2')
		host3 = self.addHost('h3')
		host4 = self.addHost('h4')
		host5 = self.addHost('h5')
		host6 = self.addHost('h6')
		#link them and announce the bandwidth, delay time, loss of each link
		self.addLink(
            host1,
            switch1,
            bw = 12,
            delay = '6ms',
            loss = 2)

		self.addLink(
            switch1,
            switch8,
            bw = 20,
            delay = '7ms',
            loss = 15)

		self.addLink(
            switch6,
			host2,
            bw = 18,
            delay = '2ms',
            loss = 3)

		self.addLink(
            switch4,
			host5,
            bw = 14,
            delay = '5ms',
            loss = 2)

		self.addLink(
            switch8,
            switch4,
            bw = 23,
            delay = '6ms',
            loss = 10)

		self.addLink(
            switch8,
            switch2,
            bw = 25,
            delay = '6ms',
            loss = 14)

		self.addLink(
            switch2,
            switch9,
            bw = 30,
            delay = '3ms',
            loss = 18)

		self.addLink(
            switch8,
            switch6,
            bw = 30,
            delay = '1ms',
            loss = 12)

		self.addLink(
            switch9,
            switch7,
            bw = 33,
            delay = '8ms',
            loss = 10)

		self.addLink(
            switch9,
            switch5,
            bw = 30,
            delay = '3ms',
            loss = 20)

		self.addLink(
            switch3,
            switch9,
            bw = 35,
            delay = '2ms',
            loss = 17)

		self.addLink(
            switch5,
			host6,
            bw = 15,
            delay = '4ms',
            loss = 3)

		self.addLink(
            host3,
            switch7,
            bw = 18,
            delay = '6ms',
            loss = 6)

		self.addLink(
            host4,
            switch3,
            bw = 13,
            delay = '3ms',
            loss = 5)            

def simpleTest():
	#build a topology with SingleSwitchTopo's switches and hosts and links
	topo = SingleSwitchTopo();
	#use TClink as link and OVSController as controller
	net = Mininet(
		topo = topo,
		controller = OVSController,
		link = TCLink)
	#start testing the net
	net.start()
	#to let me know the test is started
	print("Testing network connectivity")
	#ping each hosts
	net.pingAll()
	#start the net
	CLI(net)
	#dumps connections to/from a set of nodes
	dumpNodeConnections(net.hosts)
	dumpNodeConnections(net.switches)

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()
