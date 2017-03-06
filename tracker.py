from pyactor.context import set_context, create_host, sleep, shutdown
from collections import defaultdict
class Tracker(object):
    _ask = ['announce','get_peers','check_peers']
    _tell = ['announce','get_peers','check_peers', 'get_all_peers', 'timer']
    peers = defaultdict(dict)

    def announce(self,torrent_hash, peer_ref):
        self.peers[torrent_hash][peer_ref] = 0

    def get_peers(self,torrent_hash):
        print self.peers[torrent_hash]

    def timer(self):
        for key in self.peers.keys():
            for peer in self.peers[key].keys():
                self.peers[key][peer] += 1

    def check_peers(self):
        for key in self.peers.keys():
            for peer in self.peers[key].keys():
                if self.peers[key][peer] >= 4:
                    del self.peers[key][peer]
                    print "peer deleted"
                    
    def get_all_peers(self):
         for key in self.peers.keys():
            for peer in self.peers[key].keys():
                print peer
                  
if __name__ == "__main__":
    set_context()
    h = create_host()
    tracker = h.spawn('tracker',Tracker)
    tracker.announce(1234,'peer 1')
    tracker.announce(1234,'peer 2')
    tracker.announce(1235,'peer 3')
    while True:
        tracker.timer()
        #escoltar
        tracker.check_peers()
        tracker.get_all_peers()
        sleep(1)
        
    
    shutdown()
