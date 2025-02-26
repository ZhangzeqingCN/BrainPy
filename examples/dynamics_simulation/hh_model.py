# -*- coding: utf-8 -*-

import brainpy as bp


class HH(bp.CondNeuGroup):
  def __init__(self, size):
    super(HH, self).__init__(size)

    self.INa = bp.channels.INa_HH1952(size, )
    self.IK = bp.channels.IK_HH1952(size, )
    self.IL = bp.channels.IL(size, E=-54.387, g_max=0.03)


hh = HH(1)
I, length = bp.inputs.section_input(values=[0, 5, 0],
                                    durations=[100, 500, 100],
                                    return_length=True)
runner = bp.dyn.DSRunner(
  hh,
  monitors=['V', 'INa.p', 'INa.q', 'IK.p'],
  inputs=[hh.input, I, 'iter'],
)
runner.run(length)

bp.visualize.line_plot(runner.mon.ts, runner.mon.V, show=True)

