from __future__ import division
from __future__ import print_function

from graphsage.layers import Layer

import tensorflow as tf
flags = tf.app.flags
FLAGS = flags.FLAGS


"""
Classes that are used to sample node neighborhoods
"""

class UniformNeighborSampler(Layer):
    """
    Uniformly samples neighbors.
    Assumes that adj lists are padded with random re-sampling
    """
    def __init__(self, adj_info, **kwargs):
        super(UniformNeighborSampler, self).__init__(**kwargs)
        self.adj_info = adj_info

    def _call(self, inputs):
        ids, num_samples = inputs
        adj_lists = tf.nn.embedding_lookup(self.adj_info, ids)
        adj_lists = tf.transpose(tf.random_shuffle(tf.transpose(adj_lists)))
        adj_lists = tf.slice(adj_lists, [0,0], [-1, num_samples])
        return adj_lists

class LinearDegreeNeighborSampler(Layer):
    """
    Samples neighbors according to the ranking of degrees.
    Samples the *num_samples* highest degree neighbors.
    This sampler assume that the adj_info is already sorted according to degree ranking
    and padded with random re-sampling if needed.
    """
    def __init__(self, adj_info, **kwargs):
        super(LinearDegreeNeighborSampler, self).__init__(**kwargs)
        self.adj_info = adj_info

    def _call(self, inputs):
        assert FLAGS.sampler == 'lineardegree', 'Wrongly called linear degree sampler'
        ids, num_samples = inputs
        adj_lists = tf.nn.embedding_lookup(self.adj_info, ids)
        adj_lists = tf.transpose(tf.random_shuffle(tf.transpose(adj_lists)))
        adj_lists = tf.slice(adj_lists, [0,0], [-1, num_samples])
        return adj_lists

#class LinearDegreeNeighborSampler(Layer):
#
#    def _call(self, inputs):
#        ids, num_samples = inputs
#        adj_lists = tf.nn.embedding_lookup(self.adj_info, ids)
#        shape = adj_lists.shape
#
#        deg_lists = tf.nn.embedding_lookup(tf.reshape(self.deg_info, [-1]), tf.reshape(adj_lists, [-1]))
#        deg_lists = tf.reshape(deg_lists, shape)
#        deg_lists, indices = tf.nn.top_k(deg_lists, k=num_samples, sorted=True)
#
#        to_add = tf.reshape(tf.range(adj_lists.shape[0]*adj_lists.shape[1], delta=adj_lists.shape[1]), (adj_lists.shape[0], -1))
#        to_add = tf.tile(to_add, (1, indices.shape[1]))
#
#        indices_ = indices + to_add
#
#        adj_lists = tf.gather(tf.reshape(adj_lists, [-1]), tf.reshape(indices_, [-1]))
#        adj_lists = tf.reshape(adj_lists, (shape[0], num_samples))
#        return adj_lists




