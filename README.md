# gachasims
Simple scripts to simulate and collect data on AvAc's golden capsule pulls. Repository contains the following files:

## capsule_math.py
Using convolution, returns the probability distribution for N shards of a character. Much faster than goldsim.py and its many variations, but the input probability distribution is currently hard-coded, so it only works for finding the number of pulls required to get Dr. Strange from the Strange capsule.

TODO: ~~allow user to input a probability distribution as a dictionary, and return numbers from that. Or add all probability distributions we currently have access to, and allow user to choose which one to use.~~

## goldsim.py
A Python 2.7 implementation of the simulator. Contains framework for running and collecting data on multiple iterations for statistics reasons (think Monte Carlo sim). Also allows for setting runs for specific characters, e.g running 100k strings of attempts to get Rick Jones (last time I did this, though, the sim took over half an hour to run all 100k iterations). As of most recent update, also allows for setting desired rarity, e.g running strings of attempts at getting any character to M5.

TODO: Add some way to easily update list of heroes and chances (current implementation is hard-coded). Could read in csv files with csv package?

## goldsim.js
A "JavaScript" implementation of the simulator, which is actually just a copy and paste of the relevant parts of the Google Apps Scripts implementation attached to the spreadsheet proof-of-concept (found [here](https://docs.google.com/spreadsheets/d/1eD85azNstQWy98AgDPy9-IcpJkOS-ToN1wq3FdUrYlk/edit?usp=drive_web&ouid=108559041921065927514)). Is literal trash, in that it only simulates single pulls, has to sketchily define its own uniform random and weighted random number generators, and did you know that JavaScript is a "classless" language? So it contains a single class-like object.

TODO: Maybe add features? To be fair, a spreadsheet and/or Discord bot don't need the ability to simulate a million pulls.

## Other plans
+ Write a C++ implementation of the simulator, in hopes that it will run faster than the Python version, thereby allowing us to run a million simulations of someone trying to get Rick Jones. Useful for visualizations, I guess, and running a million simulations of someone trying to get Rick Jones. Could also approximate some of the probability combinations in the future, maybe?
+ Do something similar in Julia, reasoning being that Julia is supposed to be good at handling this kind of information.
+ ~~Something to do with matrices, probably.~~
