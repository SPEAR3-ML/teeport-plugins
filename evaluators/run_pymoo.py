import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.evaluators.prob_pymoo import evaluate

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_evaluator(evaluate, 'pymoo', name='pymoo Test Suite', configs={
    'prob_id': 'zdt1',
    'vrange': [0, 1],
    'wall_time': 1
})
print('evaluator is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.evaluator.task)
