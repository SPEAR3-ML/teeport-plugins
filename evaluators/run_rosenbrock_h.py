import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.evaluators.rosenbrock import evaluator_generator

teeport = Teeport('ws://lambda-sp3:8090/')
evaluate = evaluator_generator((-1, 2), 1)
teeport.run_evaluator(evaluate, 'Rosenbrock H')
print('evaluator is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.evaluator.task)
