from pyactor.context import set_context, create_host, sleep, shutdown, interval, later, serve_forever
from random import randint

class Peer(object):
    chunks=['_','_','_','_','_','_','_','_','_']
    _tell=['send','tim','init_start','announce','tim','gossipCycle','push']   
    def push(self,chunk_id,chunk_data):
        if self.chunks[chunk_id] == '_':
            self.chunks[chunk_id]=chunk_data
	    print self.chunks

    def tim(self):
        self.peers=tracker.get_peers(file_name)
        
         
    def init_start(self):        
	self.interval_getPeers=interval(self.host,2,self.proxy,"tim",)
        self.interval_announce=interval(self.host,10,self.proxy,"announce",)
        self.interval_gossipCycle=interval(self.host,1,self.proxy,"gossipCycle","push")
  
    def announce(self):
        tracker.announce(file_name,url)
	print 'Announced'

    def gossipCycle(self,style):
        if style == "push":
            for p in self.peers:
                if p != url and p != url_seed:
	            p=p+'/peer'
               	    peerid=h.lookup_url(p,'Peer','peer')
		    ran=randint(0,8)
	            peerid.push(ran,self.chunks[ran])
            
	if not '_' in self.chunks:
            self.interval_getPeers.set()
            self.interval_announce.set()
            self.interval_gossipCycle.set()
            print 'File downloaded'
            print 'Press Ctrl+C to stop'	
	    	
        

 
if __name__ == "__main__":
    file_name='video'
    url='http://127.0.0.1:1680'
    url_seed='http://127.0.0.1:1679'
    set_context()
    h = create_host(url)
    peer = h.spawn('peer',Peer)
    tracker = h.lookup_url('http://127.0.0.1:1277/tracker','Tracker','tracker') 
    peer.init_start()
   
 
   # peer.push(1234,12124)
    serve_forever()
  
  
  
  
  
  
  
  
  
  
  
  
  
   
    

