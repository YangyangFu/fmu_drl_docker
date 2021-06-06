import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# initial configuration: can be changed when making the environment
config = {
    'm_cart': 10,
    'm_pole': 1,
    'theta_0': 1.48,
    'theta_dot_0': 0,
    'time_step': 0.05,
    'positive_reward': 1,
    'negative_reward': -100,
    'force': 15,
    'log_level': logging.INFO,
    'fmu_result_handling':'memory',
    'fmu_result_ncp':100,
    'filter_flag':True
}

register(
    id='JModelicaCSCartPoleEnv-v0',
    entry_point='gym_cart_jmodelica.envs:JModelicaCSCartPoleEnv',
    kwargs = config
)
