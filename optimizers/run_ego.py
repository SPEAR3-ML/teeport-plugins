import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.algorithms.ego import optimize

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_optimizer(optimize, 'EGO', name='EGO', configs={
    # initialization
    'D': 13,
    'N0': 30,
    'method': 'lhs',
    'vrange': [0, 1],
    'add_center': False,
    # hyper-parameters
    'criterion': 'UCB',
    # termination
    'T': 300
})
print('optimizer is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.optimizer.task)
