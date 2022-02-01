import gym

from gym_mods.wrappers import *


def register_cartpole(max_length: int = 3000, name: str = "CartPole-v2"):
    assert max_length > 0
    gym.envs.registration.register(
        id=name,
        entry_point="gym.envs.classic_control:CartPoleEnv",
        max_episode_steps=int(max_length),
        reward_threshold=float(max_length),
    )


def register_infinite_cartpole(name: str = "CartPole-v3"):
    gym.envs.registration.register(
        id=name,
        entry_point="gym.envs.classic_control:CartPoleEnv",
        max_episode_steps=None,
        reward_threshold=float("inf"),
    )
