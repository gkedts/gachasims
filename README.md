# gachasims
Simple scripts to simulate and collect data on AvAc's golden capsule pulls. Repository contains the following files:

## goldsim.py
A Python 2.7 implementation of the simulator. Contains framework for running and collecting data on multiple iterations for statistics reasons (think Monte Carlo sim). Also allows for setting runs for specific characters, e.g running 100k strings of attempts to get Rick Jones (last time I did this, though, the sim took over half an hour to run).

TODO: Add some way to easily update list of heroes and chances (current implementation is hard-coded). Could read in csv files with csv package? Also, add way to specify conditions for success, e.g "get Hulk to M5".

## goldsim.js
A "JavaScript" implementation of the simulator, which is actually just a copy and paste of the relevant parts of the Google Apps Scripts implementation attached to the spreadsheet proof-of-concept (found [here](https://docs.google.com/spreadsheets/d/1eD85azNstQWy98AgDPy9-IcpJkOS-ToN1wq3FdUrYlk/edit?usp=drive_web&ouid=108559041921065927514)). Is literal trash, in that it only simulates single pulls, has to sketchily define its own uniform random and weighted random number generators, and did you know that JavaScript is a "classless" language? So it contains a single class-like object.

TODO: Maybe add features? To be fair, a spreadsheet and/or Discord bot don't need the ability to simulate a million pulls.

## Other plans
+ Write a C++ implementation of the simulator, in hopes that it will run faster than the Python version, thereby allowing us to run a million simulations of someone trying to get Rick Jones. Useful for visualizations, I guess, and running a million simulations of someone trying to get Rick Jones. Could also approximate some of the probability combinations in the future, maybe?
+ Do something similar in Julia, reasoning being that Julia is supposed to be good at handling this kind of information.
+ Something to do with matrices, probably.
