# -*- coding: utf-8 -*-

__version__ = "2.3.5"


# fundamental supporting modules
from brainpy import errors, check, tools


#  Part 1: Math Foundation  #
# ------------------------- #

# math foundation
from brainpy import math
from .math import BrainPyObject


#  Part 2: Toolbox  #
# ----------------- #

# modules of toolbox
from brainpy import (
  connect,  # synaptic connection
  initialize,  # weight initialization
  optim,  # gradient descent optimizers
  losses,  # loss functions
  measure,  # methods for data analysis
  inputs,  # methods for generating input currents
  encoding,  # encoding schema
  checkpoints,  # checkpoints
  check,  # error checking
)
from . import algorithms  # online or offline training algorithms

# convenient alias
conn = connect
init = initialize
optimizers = optim

# numerical integrators
from brainpy import integrators
from brainpy.integrators import ode, sde, fde
from brainpy._src.integrators.base import (Integrator as Integrator)
from brainpy._src.integrators.joint_eq import (JointEq as JointEq)
from brainpy._src.integrators.runner import (IntegratorRunner as IntegratorRunner)
from brainpy._src.integrators.ode.generic import (odeint as odeint)
from brainpy._src.integrators.sde.generic import (sdeint as sdeint)
from brainpy._src.integrators.fde.generic import (fdeint as fdeint)


#  Part 3: Models  #
# ---------------- #

from brainpy import (channels,  # channel models
                     layers,  # ANN layers
                     neurons,  # neuron groups
                     rates,  # rate models
                     synapses,  # synaptic dynamics
                     synouts,  # synaptic output
                     synplast,  # synaptic plasticity
                     )
from brainpy._src.dyn.base import (DynamicalSystem as DynamicalSystem,
                                   Container as Container,
                                   Sequential as Sequential,
                                   Network as Network,
                                   NeuGroup as NeuGroup,
                                   SynConn as SynConn,
                                   SynOut as SynOut,
                                   SynSTP as SynSTP,
                                   SynLTP as SynLTP,
                                   TwoEndConn as TwoEndConn,
                                   CondNeuGroup as CondNeuGroup,
                                   Channel as Channel)
from brainpy._src.dyn.base import (DSPartial as DSPartial)
from brainpy._src.dyn.transform import (NoSharedArg as NoSharedArg,  # transformations
                                        LoopOverTime as LoopOverTime,)
from brainpy._src.dyn.runners import (DSRunner as DSRunner)  # runner


#  Part 4: Training  #
# ------------------ #

from . import train
from ._src.train.base import (DSTrainer as DSTrainer)
from ._src.train.back_propagation import (BPTT as BPTT,
                                          BPFF as BPFF,)
from ._src.train.online import (OnlineTrainer as OnlineTrainer,
                                ForceTrainer as ForceTrainer,)
from ._src.train.offline import (OfflineTrainer as OfflineTrainer,
                                 RidgeTrainer as RidgeTrainer,)


#  Part 5: Analysis  #
# ------------------ #

from . import analysis


#  Part 6: Others    #
# ------------------ #

from . import running
from ._src.visualization import (visualize as visualize)
from ._src.running.runner import (Runner as Runner)


#  Part 7: Deprecations  #
# ---------------------- #


integrators.__dict__['Integrator'] = Integrator
integrators.__dict__['odeint'] = odeint
integrators.__dict__['sdeint'] = sdeint
integrators.__dict__['fdeint'] = fdeint
integrators.__dict__['IntegratorRunner'] = IntegratorRunner
integrators.__dict__['JointEq'] = JointEq
ode.__dict__['odeint'] = odeint
sde.__dict__['sdeint'] = sdeint
fde.__dict__['fdeint'] = fdeint


# deprecated
from brainpy._src.math.object_transform.base import (Base as Base,
                                                     ArrayCollector as ArrayCollector,
                                                     Collector as Collector,
                                                     TensorCollector as TensorCollector)

train.__dict__['DSTrainer'] = DSTrainer
train.__dict__['BPTT'] = BPTT
train.__dict__['BPFF'] = BPFF
train.__dict__['OnlineTrainer'] = OnlineTrainer
train.__dict__['ForceTrainer'] = ForceTrainer
train.__dict__['OfflineTrainer'] = OfflineTrainer
train.__dict__['RidgeTrainer'] = RidgeTrainer


from . import base
base.base.__dict__['BrainPyObject'] = BrainPyObject
base.base.__dict__['Base'] = Base
base.collector.__dict__['Collector'] = Collector
base.collector.__dict__['ArrayCollector'] = ArrayCollector
base.collector.__dict__['TensorCollector'] = TensorCollector
base.function.__dict__['FunAsObject'] = math.FunAsObject
base.function.__dict__['Function'] = math.FunAsObject
base.io.__dict__['save_as_h5'] = checkpoints.io.save_as_h5
base.io.__dict__['save_as_npz'] = checkpoints.io.save_as_npz
base.io.__dict__['save_as_pkl'] = checkpoints.io.save_as_pkl
base.io.__dict__['save_as_mat'] = checkpoints.io.save_as_mat
base.io.__dict__['load_by_h5'] = checkpoints.io.load_by_h5
base.io.__dict__['load_by_npz'] = checkpoints.io.load_by_npz
base.io.__dict__['load_by_pkl'] = checkpoints.io.load_by_pkl
base.io.__dict__['load_by_mat'] = checkpoints.io.load_by_mat
base.naming.__dict__['check_name_uniqueness'] = tools.check_name_uniqueness
base.naming.__dict__['clear_name_cache'] = tools.clear_name_cache
base.naming.__dict__['get_unique_name'] = tools.get_unique_name
base.__dict__['BrainPyObject'] = BrainPyObject
base.__dict__['Base'] = Base
base.__dict__['Collector'] = Collector
base.__dict__['ArrayCollector'] = ArrayCollector
base.__dict__['TensorCollector'] = TensorCollector
base.__dict__['FunAsObject'] = math.FunAsObject
base.__dict__['Function'] = math.FunAsObject
base.__dict__['save_as_h5'] = checkpoints.io.save_as_h5
base.__dict__['save_as_npz'] = checkpoints.io.save_as_npz
base.__dict__['save_as_pkl'] = checkpoints.io.save_as_pkl
base.__dict__['save_as_mat'] = checkpoints.io.save_as_mat
base.__dict__['load_by_h5'] = checkpoints.io.load_by_h5
base.__dict__['load_by_npz'] = checkpoints.io.load_by_npz
base.__dict__['load_by_pkl'] = checkpoints.io.load_by_pkl
base.__dict__['load_by_mat'] = checkpoints.io.load_by_mat
base.__dict__['check_name_uniqueness'] = tools.check_name_uniqueness
base.__dict__['clear_name_cache'] = tools.clear_name_cache
base.__dict__['get_unique_name'] = tools.get_unique_name


from . import modes
modes.__dict__['Mode'] = math.Mode
modes.__dict__['NormalMode'] = math.NonBatchingMode
modes.__dict__['BatchingMode'] = math.BatchingMode
modes.__dict__['TrainingMode'] = math.TrainingMode
modes.__dict__['normal'] = math.nonbatching_mode
modes.__dict__['batching'] = math.batching_mode
modes.__dict__['training'] = math.training_mode
modes.__dict__['check_mode'] = check.is_subclass


from brainpy import dyn
dyn.__dict__['channels'] = channels
dyn.__dict__['neurons'] = neurons
dyn.__dict__['rates'] = rates
dyn.__dict__['synapses'] = synapses
dyn.__dict__['synouts'] = synouts
dyn.__dict__['synplast'] = synplast
dyn.__dict__['DynamicalSystem'] = DynamicalSystem
dyn.__dict__['Container'] = Container
dyn.__dict__['Sequential'] = Sequential
dyn.__dict__['Network'] = Network
dyn.__dict__['NeuGroup'] = NeuGroup
dyn.__dict__['SynConn'] = SynConn
dyn.__dict__['SynOut'] = SynOut
dyn.__dict__['SynSTP'] = SynSTP
dyn.__dict__['SynLTP'] = SynLTP
dyn.__dict__['TwoEndConn'] = TwoEndConn
dyn.__dict__['CondNeuGroup'] = CondNeuGroup
dyn.__dict__['Channel'] = Channel
dyn.__dict__['NoSharedArg'] = NoSharedArg
dyn.__dict__['LoopOverTime'] = LoopOverTime
dyn.__dict__['DSRunner'] = DSRunner

# neurons
dyn.__dict__['HH'] = neurons.HH
dyn.__dict__['MorrisLecar'] = neurons.MorrisLecar
dyn.__dict__['PinskyRinzelModel'] = neurons.PinskyRinzelModel
dyn.__dict__['FractionalFHR'] = neurons.FractionalFHR
dyn.__dict__['FractionalIzhikevich'] = neurons.FractionalIzhikevich
dyn.__dict__['LIF'] = neurons.LIF
dyn.__dict__['ExpIF'] = neurons.ExpIF
dyn.__dict__['AdExIF'] = neurons.AdExIF
dyn.__dict__['QuaIF'] = neurons.QuaIF
dyn.__dict__['AdQuaIF'] = neurons.AdQuaIF
dyn.__dict__['GIF'] = neurons.GIF
dyn.__dict__['Izhikevich'] = neurons.Izhikevich
dyn.__dict__['HindmarshRose'] = neurons.HindmarshRose
dyn.__dict__['FHN'] = neurons.FHN
dyn.__dict__['SpikeTimeGroup'] = neurons.SpikeTimeGroup
dyn.__dict__['PoissonGroup'] = neurons.PoissonGroup
dyn.__dict__['OUProcess'] = neurons.OUProcess

# synapses
from brainpy._src.dyn.synapses import compat
dyn.__dict__['DeltaSynapse'] = compat.DeltaSynapse
dyn.__dict__['ExpCUBA'] = compat.ExpCUBA
dyn.__dict__['ExpCOBA'] = compat.ExpCOBA
dyn.__dict__['DualExpCUBA'] = compat.DualExpCUBA
dyn.__dict__['DualExpCOBA'] = compat.DualExpCOBA
dyn.__dict__['AlphaCUBA'] = compat.AlphaCUBA
dyn.__dict__['AlphaCOBA'] = compat.AlphaCOBA
dyn.__dict__['NMDA'] = compat.NMDA
del compat

