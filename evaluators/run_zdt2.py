import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.evaluators.zdt import evaluate

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_evaluator(evaluate, 'ZDT2', name='ZDT2', configs={
	'prob_id': 2,
    'D': 30,
    'wall_time': 1
})
print('evaluator is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.evaluator.task)
