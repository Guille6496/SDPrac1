from pyactor.context import set_context, create_host, sleep, shutdown, interval, later, serve_forever
from random import randint
import random
class Peer(object):
    chunks=['G','O','T','O','R','R','E','N','T']
    _ask=['pull']
    _tell=['send','tim','init_start','announce','getPeers','gossipCycle']
 
    def getPeers(self):
        self.peers=tracker.get_peers(file_name)
        
    def pull(self,chunk_id):
        if not self.chunks[chunk_id] == '_':
            return self.chunks[chunk_id]
        else:
	    return None
     
    def init_start(self):        
	self.interval_getPeers=interval(self.host,2,self.proxy,"getPeers",)
	self.interval_announce=interval(self.host,10,self.proxy,"announce",)
        self.interval_gossipCycle=interval(self.host,1,self.proxy,"gossipCycle","pull")
  
    def announce(self):
        tracker.announce(file_name,url)
	print 'Announced'

    
    def gossipCycle(self,typ):     
        if typ == "push":  ## push
            self.p=random.sample(self.peers,1)
            if self.p != url and self.p != url_seed:
	        self.p=self.p+'/peer'
                peerid=h.lookup_url(self.p,'Peer','peer')
	        ran=randint(0,8)
                if not self.chunks[ran] == '_':
	            peerid.push(ran,self.chunks[ran])
                
        else:			#pull
            if self.p != url:
                self.p=self.p+'/peer'
               	peerid=h.lookup_url(self.p,'Peer','peer')
		ran=randint(0,8)
                chun=peerid.pull(ran) 
                if not chun == None:   
		    self.chunks[ran]=chun
                    print self.chunks


        if not '_' in self.chunks:
            self.interval_getPeers.set()
            self.interval_announce.set()
            self.interval_gossipCycle.set()              
	    print 'File downloaded'
	    print 'Press Ctrl+C to stop'
            
		
	    	
        

 
if __name__ == "__main__":
    file_name='video'
    url='http://127.0.0.1:1679'
    url_seed='http://127.0.0.1:1679'
    set_context()
    h = create_host(url)
    peer = h.spawn('peer',Peer)
    tracker = h.lookup_url('http://127.0.0.1:1277/tracker','Tracker','tracker') 
    peer.init_start()
   
    peer.gossipCycle("push")
 
    serve_forever()
  
  
  
  
  
  
  
  
  
  
  
  
  
   
    

