# -*- coding: utf-8 -*-

import numpy as np

from npbrain.core.synapse import *

__all__ = [
    'VoltageJumpSynapse',
]


def VoltageJumpSynapse(pre, post, weights, connection, delay=None, var='V', name='VoltageJumpSynapse'):
    """Voltage jump synapses.

    .. math::

        I_{syn} = \sum J \delta(t-t_j)

    Parameters
    ----------
    pre : Neurons
        The pre-synaptic neuron group.
    post : Neurons
        The post-synaptic neuron group.
    weights : dict, np.ndarray, int, float
        The weighted coefficients of synapses.
    connection : tuple
        The connectivity.
    delay : int, float, None
        The delay period (ms).
    name : str
        The name of the synapse.
    var : str
        The variable of the post-synapse going to connect.

    Returns
    -------
    synapse : Synapses
        The constructed ordinary synapses.
    """
    num_pre = pre.num
    num_post = post.num
    var2index = dict()

    pre_ids, post_ids, anchors = connection
    num = len(pre_ids)
    state = initial_syn_state(delay, num_pre, num_post, num)

    try:
        post_varid = post.var2index[var]
    except KeyError:
        raise KeyError("Post synapse doesn't has variable '{}'.".format(var))

    def update_state(syn_state, t, delay_idx):
        # get synapse state
        spike = syn_state[0][-1]
        spike_idx = np.where(spike > 0)[0]
        # get post-synaptic values
        g = np.zeros(num_post)
        for i_ in spike_idx:
            idx = anchors[:, i_]
            post_idx = post_ids[idx[0]: idx[1]]
            g[post_idx] += weights
        syn_state[1][delay_idx] = g

    if hasattr(post, 'ref') and getattr(post, 'ref') > 0.:

        def output_synapse(syn_state, output_idx, post_neu_state):
            g_val = syn_state[1][output_idx]
            for idx in range(num_post):
                val = g_val[idx] * post_neu_state[-5, idx]
                post_neu_state[post_varid, idx] += val
    else:

        def output_synapse(syn_state, output_idx, post_neu_state):
            g_val = syn_state[1][output_idx]
            post_neu_state[post_varid] += g_val

    return Synapses(**locals())
