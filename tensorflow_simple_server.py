#!env python3

import tensorflow as tf
from sys import argv

def main(port):
    srv = tf.train.Server({'local':['localhost:'+port]},protocol='grpc',config=None,start=True)
    srv.join()

if __name__ == '__main__' :
    main(argv[-1])

