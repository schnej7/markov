import random

###########################################
# Markov Class Written by Jerry Schneider #
# schnej7@gmail.com                       #
###########################################
class markov:
    def __init__( self ):
        self.hist_probs = dict()
        self.keys = set()

    # record a data point
    def record( self, prev, cur ):
        prev = str( prev )
        if prev not in self.keys:
            self.hist_probs[prev] = dict()
            self.hist_probs[prev][cur] = 1
            self.keys.add( prev )
        elif cur not in self.hist_probs[prev].keys():
            self.hist_probs[prev][cur] = 1
        else:
            self.hist_probs[prev][cur] += 1

    # randomly predict the next value
    def predict( self, cur ):
        cur = str( cur )
        if cur not in self.keys:
            return None
        else:
            total = sum( list( self.hist_probs[cur][key] for key in self.hist_probs[cur].keys() ) )
            choice = random.choice( range( total ) )
            count = 0
            if len( self.hist_probs[cur].keys() ) < 2:
                return None
            for key in self.hist_probs[cur].keys():
                count += self.hist_probs[cur][key]
                if count > choice:
                    return key;
            return None
