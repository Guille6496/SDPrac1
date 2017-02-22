from pyactor.context import set_context, create_host, sleep, shutdown

class Tracker(object):
	_ask = ['announce','get_peers']
	_tell = ['announce','get_peers']
    peers=[]
    def announce(self,torrent_hash, peer_ref):
		self.peers[torrent_hash] = peer_ref
	
	def get_peers(self,torrent_hash):
		print self.peers[torrent_hash]
		
if __name__ == "__main__":
    set_context()
    h = create_host()
    tracker = h.spawn('tracker',Tracker)
    tracker.announce(1234,12345)
    tracker.get_peers(1234)
    shutdown()
