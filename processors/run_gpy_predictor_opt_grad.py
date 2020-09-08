import numpy as np
import nest_asyncio
nest_asyncio.apply()
import asyncio
from functools import partial

from teeport import Teeport
from opt.processors.gpy_predictor import process

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_processor(partial(process, configs={'ret_grad': True}), 'GPy Predictor with Grad')
print('processor is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.processors[0].task)
