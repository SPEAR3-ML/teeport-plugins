import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.evaluators.rosenbrock import evaluate

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_evaluator(evaluate, 'Rosenbrock', name='Rosenbrock', configs={
    'vrange': [-2, 2],
    'wall_time': 1,
    'noise_level': 0,
    'ret_origin': False
})
print('evaluator is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.evaluator.task)
