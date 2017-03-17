# Universal Value Function Approximators

This repository contains an implementation of [[1](#1)]

The code is tested on a foor-room gridworld as in the paper. Only the supervised learning and the two-stage architecture is implemented.

Open notebook for explanation, and results.

To generate the dataset for learning the value function in a supervised way, run:
`python lib/data.py [ouput]`

<a name='1'></a> [1] [Schaul, Tom, et al. "Universal value function approximators." Proceedings of the 32nd International Conference on Machine Learning (ICML-15). 2015.](http://jmlr.org/proceedings/papers/v37/schaul15.pdf)
