import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.algorithms.ego import optimize as optimize_ego

async def optimize(evaluate):
    params = {
        # initialization
        'D': 8,
        'N0': 30,
        'method': 'lhs',
        'vrange': (0.25, 0.75),
        'add_center': False,
        # hyper-parameters
        'criterion': 'UCB',
        # termination
        'T': 300
    }
    
    await optimize_ego(evaluate, params)

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_optimizer(optimize, 'EGO-UCB 8D')
print('optimizer is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.optimizer.task)
