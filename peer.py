from pyactor.context import set_context, create_host, sleep, shutdown, interval, later, serve_forever
from random import randint
import sys
import time
import random
class Peer(object):
    chunks=['_','_','_','_','_','_','_','_','_']
    _tell=['send','init_start','announce','getPeers','gossipCycle','push']
    _ask=['pull','get_state']
    downloaded=False
    def push(self,chunk_id,chunk_data):
        if self.chunks[chunk_id] == '_':
           self.chunks[chunk_id]=chunk_data          
	   print self.chunks
    def pull(self,chunk_id):
        if not self.chunks[chunk_id] == '_':
            return self.chunks[chunk_id]
        else:
	    return None

    def get_state(self):
        return self.downloaded
    def getPeers(self):
        self.peers=tracker.get_peers(file_name)
        
         
    def init_start(self):        
	self.interval_getPeers=interval(self.host,2,self.proxy,"getPeers",)
	self.interval_announce=interval(self.host,10,self.proxy,"announce",)
        self.interval_gossipCycle=interval(self.host,1,self.proxy,"gossipCycle","pull")
    def gossipCycle(self,typ):    
        p=random.sample(self.peers,1)
        p=p[0] 
        if typ == "push":  ## push            
            if p != url and p != url_seed:               #to do: while fins que trobi un peer que no sigui ell ni el seed
	        p=p+'/peer'
                peerid=h.lookup_url(p,'Peer','peer')
	        ran=randint(0,8)
                if not peerid.get_state():
                    if not self.chunks[ran] == '_':
	                peerid.push(ran,self.chunks[ran])
                
        elif not self.downloaded:			#pull
            if p != url:
                p=p+'/peer'
               	peerid=h.lookup_url(p,'Peer','peer')
		ran=randint(0,8)
                chun=peerid.pull(ran) 
                if not chun == None:   
		    self.chunks[ran]=chun
                    print 'Pull from: '+p
                    print self.chunks


        if not '_' in self.chunks:
            self.downloaded=True           
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
    serve_forever()  
  
  
  
  
   
    

