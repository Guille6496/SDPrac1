from pyactor.context import set_context, create_host, sleep, shutdown

class Peer(object):
    chunks = {}
    _ask=['push']
    _tell=['send']
    def push(self,chunk_id,chunk_data):
        peer = tracker.get_peers('1234')
        
      
    def send(self,msg):
        print msg+'asdasdsadsa'  
if __name__ == "__main__":
    set_context()
    h = create_host('http://127.0.0.1:1680')
    peer = h.spawn('peer',Peer)
    tracker = h.lookup_url('http://127.0.0.1:1277/tracker','Tracker','tracker') 
    while True:
        tracker.announce('12','http://127.0.0.1:1680')
    peer.push(1234,12124)
    shutdown()
  
  
  
  
  
  
  
  
  
  
  
  
  
   
    

