import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.algorithms.nsgaii import optimize

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_optimizer(optimize, 'NSGA-II', name='NSGA-II', configs={
    'D': 8,
    'N0': 80,
    'seed': None,
    'Ng': 30
})
print('optimizer is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.optimizer.task)
