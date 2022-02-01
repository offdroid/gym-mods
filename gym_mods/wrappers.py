import gym


class CartPoleAbsDistFromOpt(gym.Wrapper):
    def __init__(self, env: gym.Env):
        """
        Reward wrapper for CartPole-like environments, where the reward is the sum of the distance from the optimal x-position and angle.

        Args:
            env (gym.Env): CartPole environment
        """
        assert isinstance(env, gym.envs.classic_control.CartPoleEnv)
        super().__init__(env)
        self.env = env

    def step(self, action):
        next_state, reward, done, info = self.env.step(action)
        reward = -abs(next_state[0] / 2.4) - abs(next_state[2] / 0.209)
        return next_state, reward, done, info


class PassiveWrapper(gym.Wrapper):
    def __init__(self, env: gym.Env):
        """
        Wrapper that forbids runnning the wrapped env.
        This useful when the environment is NOT supposed to produce (training) data, but 'meta'-data, such as its action- and observation space are needed.

        Could be used for an implementation of `Fujimoto, Scott & Meger, David & Precup, Doina. (2018). Off-Policy Deep Reinforcement Learning without Exploration`.

        Args:
            env (gym.Env): Environment to block step and reset calls on
        """
        super().__init__(env)
        self.env = env

    def reset(self, **_):
        raise RuntimeError("Illegal operation")

    def step(self, _):
        raise RuntimeError("Illegal operation")
