# Linear algebra

I'm refreshing my understanding of linear algebra, working through online lectures (e.g. [Gilbert Strang's lectures](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8)), and writing simple implementations of some of the ideas in Python to help to consolidate what I'm learning.

## Resources

- Gilbert Strang:
  - [2005 MIT course in Linear Algebra](https://www.youtube.com/playlist?list=PLE7DDD91010BC51F8)
  - [2018 MIT course in Matrix Methods for ML / signal processing](https://www.youtube.com/playlist?list=PLUl4u3cNGP63oMNUHXqIUcrkS2PivhN3k)

## Developing
### Setup

I'm using Visual Studio Code, and trialing using a containerised dev environment (via these [instructions](https://code.visualstudio.com/docs/remote/containers)).

### Scripts

- Start a jupyter server with the ```scripts/start_jupyter.sh``` script; the token for access is 'the_token'.

## TODO

- Split ```requirements.txt``` according to whether they're required for interactive, dev, or package usage.
- Split up the docker image into a base python dev environment, and project specific layers
- Add nbextension for setting up common first cells (as in [this Stack Overflow answer](https://stackoverflow.com/a/43156449))