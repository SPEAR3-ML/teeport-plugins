import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.algorithms.pso import optimize

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_optimizer(optimize, 'PSO', name='PSO', configs={
    'D': 8,
    'N0': 30,
    'method': 'lhs',
    'Ng': 20
})
print('optimizer is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.optimizer.task)
