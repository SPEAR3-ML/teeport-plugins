import nest_asyncio
nest_asyncio.apply()
import asyncio

from teeport import Teeport
from opt.evaluators.lossrate_sim import evaluator_generator

teeport = Teeport('ws://lambda-sp3:8090/')
evaluate = evaluator_generator('/home/jupyter-zhezhang/loss_rate_model.json', (-20, 20), 0, 0.5)
teeport.run_evaluator(evaluate, 'Lossrate NN')
print('evaluator is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.evaluator.task)
