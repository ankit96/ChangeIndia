'''
1)storing pickle files
'''
__author__ = 'ankit'
import cPickle
from listtodict import cluster
base='/home/ankit/tweeter/corpus/clusters/goverment/'

cPickle.dump(cluster, open(base+'cluster.p', 'wb')) 

