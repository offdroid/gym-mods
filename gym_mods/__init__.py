import gym

from gym_mods.wrappers import *


def register_cartpole(max_length: int):
    assert max_length > 0
    gym.envs.registration.register(
        id="CartPole-v3",
        entry_point="gym.envs.classic_control:CartPoleEnv",
        max_episode_steps=int(max_length),
        reward_threshold=float(max_length),
    )


def register_infinite_cartpole():
    gym.envs.registration.register(
        id="CartPole-v4",
        entry_point="gym.envs.classic_control:CartPoleEnv",
        max_episode_steps=None,
        reward_threshold=float("inf"),
    )
