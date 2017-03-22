from pyactor.context import set_context, create_host, sleep, shutdown, interval, later
from collections import defaultdict
class Tracker(object):
    _ask = ['get_peers']
    _tell = ['announce','check_peers', 'get_all_peers','init_start','stop_interval','tim']
    _ref = []
    peers = defaultdict(dict)

    def announce(self,torrent_hash, peer_ref):
        self.peers[torrent_hash][peer_ref] = 0

    def get_peers(self,torrent_hash):
        return self.peers[torrent_hash].keys()
     
        
    def init_start(self):
        self.interval1=interval(self.host,1,self.proxy,"tim","aa")
        #later(5, self.proxy, "stop_interval")
        
    def tim(self,param):
        for key in self.peers.keys():
            for peer in self.peers[key].keys():
                self.peers[key][peer] += 1
        self.check_peers()
        self.get_all_peers()
                
    def stop_interval(self):
        self.interval1.set()
        
    def check_peers(self):
        for key in self.peers.keys():
            for peer in self.peers[key].keys():
                if self.peers[key][peer] >= 10:
                    del self.peers[key][peer]
                    print "peer deleted"
                    
    def get_all_peers(self):
         for key in self.peers.keys():
            for peer in self.peers[key].keys():
                print peer
                  
if __name__ == "__main__":
    set_context()
    h = create_host('http://127.0.0.1:1277')
    tracker = h.spawn('tracker',Tracker)
    tracker.init_start()
    tracker.announce('1235','peer 3')
    while True:
    	tracker.announce('1234','peer 1')
    	tracker.announce('1234','peer 2') 	
	sleep(4)
        print tracker.get_peers('1234')
        
        
    
    serve_forever()
