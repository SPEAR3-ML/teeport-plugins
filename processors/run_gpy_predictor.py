import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.processors.gpy_predictor import process

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_processor(process, 'GPy-Pred', name='GPy Predictor', configs={
    'theta': None,
    'var': None,
    'sigma_n': None,
    'ret_grad': False
})
print('processor is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.processors[0].task)
