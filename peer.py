from pyactor.context import set_context, create_host, sleep, shutdown, interval, later, serve_forever
from random import randint
import sys
import time
import random
class Peer(object):
    chunks=['_','_','_','_','_','_','_','_','_']
    _tell=['send','init_start','announce','getPeers','gossipCycle','push']
    _ask=['pull']
    def push(self,chunk_id,chunk_data):
        if self.chunks[chunk_id] == '_':
           self.chunks[chunk_id]=chunk_data
	   print self.chunks
    def pull(self,chunk_id):
        if not self.chunks[chunk_id] == '_':
            return self.chunks[chunk_id]
        else:
	    return None

 
    def getPeers(self):
        self.peers=tracker.get_peers(file_name)
        
         
    def init_start(self):        
	self.interval_getPeers=interval(self.host,2,self.proxy,"getPeers",)
	self.interval_announce=interval(self.host,10,self.proxy,"announce",)
        #self.interval_gossipCycle=interval(self.host,4,self.proxy,"gossipCycle","push")
    def gossipCycle(self,typ):     
        if typ == "push":  ## push
            p=random.sample(self.peers,1)
            if p != url and p != url_seed:
	        p=p+'/peer'
                peerid=h.lookup_url(p,'Peer','peer')
	        ran=randint(0,8)
                if not self.chunks[ran] == '_':
	            peerid.push(ran,self.chunks[ran])
                
        else:			#pull
            if p != url:
                p=p+'/peer'
               	peerid=h.lookup_url(p,'Peer','peer')
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
    def announce(self):
        tracker.announce(file_name,url)
	print 'Announced'

if __name__ == "__main__":
   
    file_name='video'
    url='http://127.0.0.1:'+str(sys.argv[1])
    url_seed='http://127.0.0.1:1679'
    set_context()
    h = create_host(url)
    peer = h.spawn('peer',Peer)
    tracker = h.lookup_url('http://127.0.0.1:1277/tracker','Tracker','tracker') 
    peer.init_start()
   # sleep(3)
   # peer.gossipCycle("push") 
        



















    serve_forever()
  
  
  
  
  
  
  
  
  
  
  
  
  
   
    

