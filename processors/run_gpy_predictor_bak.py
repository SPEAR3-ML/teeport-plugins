import numpy as np
import nest_asyncio
nest_asyncio.apply()
import asyncio
from functools import partial

from teeport import Teeport
from opt.processors.gpy_predictor import process

configs = dict(theta=np.array([[0.4]]), var='auto', sigma_n=np.array([[1e-4]]))

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_processor(partial(process, configs=configs), 'GPy Predictor: no opt')
print('processor is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.processors[0].task)
