# Linear algebra practice

I'm refreshing my understanding of linear algebra, working through [Gilbert Strang's lectures](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8), and writing simple implementations of some of the ideas in Python to help to consolidate it.

## Setup

I'm using Visual Studio Code, and trialing using a containerised dev environment (via these [instructions](https://code.visualstudio.com/docs/remote/containers)).

## Scripts

- Start a jupyter server with the ```scripts/start_jupyter.sh``` script; the token for access is 'the_token'.

## TODO

- Split ```requirements.txt``` according to whether they're required for interactive, dev, or package usage.
- Split up the docker image into a base python dev environment, and project specific layers