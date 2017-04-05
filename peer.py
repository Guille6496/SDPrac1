from pyactor.context import set_context, create_host, sleep, shutdown, interval, later, serve_forever
from random import randint
from pyactor.exceptions import TimeoutError
import sys
import time
import random
class Peer(object):
    
    _tell=['send','init_start','announce','getPeers','gossipCycle','push','set']
    _ask=['pull','get_state']
    
    def set(self,url):
        self.url=url
        self.downloaded=False
        if self.url=="seed":
            self.chunks=['G','O','T','O','R','R','E','N','T']
            self.downloaded=True
        else:
            self.chunks=['_','_','_','_','_','_','_','_','_']

    def push(self,chunk_id,chunk_data):
        if self.chunks[chunk_id] == '_':
            self.chunks[chunk_id]=chunk_data          
	    #print self.url," ",self.chunks
            

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
	self.interval_announce=interval(self.host,10,self.proxy,"announce",)
	self.interval_getPeers=interval(self.host,2,self.proxy,"getPeers",)
        self.interval_gossipCycle=interval(self.host,1,self.proxy,"gossipCycle","pull")

    def gossipCycle(self,typ):        
        if typ == "push" or typ == "pushpull":  ## push     
            i=0
            found=False
            while i<10 and not found:
                p=random.sample(self.peers,1)
                p=p[0]
                if p != self.url and p != url_seed:
                    found=True
                i+=1
            try:                   
                peerid=h.lookup(p)           
	    except TimeoutError:
                print ""
            i=0
	    found=False;
	    while i<len(self.chunks) and not found:
                ran=randint(0,8)
	        if self.chunks[ran] != '_' :
	      	    found=True             
		    peerid.push(ran,self.chunks[ran])
	        i+=1
        
        if (typ =="pull" or typ=="pushpull") and (not self.downloaded and not self.url=="seed"):			#pull
            found=False
            i=0
            while i<10 and not found:
                p=random.sample(self.peers,1)
                p=p[0]
                if p != self.url:
                    found=True
                    i+=1
            if p != self.url:
               	peerid=h.lookup(p)
		found=False
                chun=None
                while i<len(self.chunks) and not found:
	 	    ran=randint(0,8)
                    if self.chunks[ran] == '_':
                        found=True
                        try:
                            chun=peerid.pull(ran) 
                        except TimeoutError:
                            print ""
                if not chun == None:   
		    self.chunks[ran]=chun
                    


        print self.url," ",self.chunks
        if not '_' in self.chunks and self.url != "seed" and not self.downloaded:
           self.downloaded=True
           print 'File ',self.url," downloaded ",self.chunks



    def announce(self):
        tracker.announce(file_name,self.url)      
        """if not self.downloaded:
            print self.url," status ",self.chunks
            print '-------------------'"""
	

if __name__ == "__main__":
   
    file_name='video'
    #url='http://127.0.0.1:'+str(sys.argv[1])
    url_seed='seed'
    set_context()
    h = create_host('http://127.0.0.1:1990')
    tracker = h.lookup_url('http://127.0.0.1:1277/tracker','Tracker','tracker')

    seed = h.spawn('seed',Peer)
    seed.init_start()
    seed.set('seed')   

    for i in range(0,4):
        peer = h.spawn('peer'+str(i),Peer)
        peer.init_start()
        peer.set('peer'+str(i))
    
    
    """peer2 = h.spawn('peer2',Peer)
    peer2.init_start()
    peer2.set('peer2')
    
    peer3 = h.spawn('peer3',Peer)
    peer3.init_start()
    peer3.set('peer3')

    peer4 = h.spawn('peer4',Peer)
    peer4.init_start()
    peer4.set('peer4')
    
    """
    serve_forever()  
  
  
  
  
   
    

