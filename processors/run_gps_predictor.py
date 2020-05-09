import nest_asyncio
nest_asyncio.apply()
import asyncio
from functools import partial

from teeport import Teeport
from opt.processors.gps_predictor import process

params = dict(theta=np.array([[0.4]]), var='auto', sigma_n=np.array([[1e-4]]), C=1e9)

teeport = Teeport('ws://lambda-sp3:8090/')
teeport.run_processor(partial(process, params=params), 'GPS Predictor: no opt')
print('processor is running...')

loop = asyncio.get_event_loop()
loop.run_until_complete(teeport.processors[0].task)
