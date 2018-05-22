# gachasims
Simple scripts to simulate and collect data on AvAc's golden capsule pulls. Repository contains the following files:

## capsule_math.py
Using convolution, returns the probability distribution for N shards of a character. Much faster than goldsim.py and its many variations, but the input probability distribution is currently hard-coded, ~~so it only works for finding the number of pulls required to get Dr. Strange from the Strange capsule.~~ so will need to be manually updated every time a new capsule comes out.

To run:

1. Make sure you have the Python 2.7 and the numpy package installed.
2. Run the script as usual, so `python capsule_math.py` in your command line if you're running bash.
3. At some point, the script will prompt you to give it a file name. The file will automatically be a .csv, so just give it a name, i.e entering "herpderp" will give you a file named "herpderp.csv", while entering "herpderp.csv" will give you a file named "herpderp.csv.csv" (so don't do this!).
4. After the script is finished running, check the folder where you ran the script for your newly-generated .csv!

TODO: ~~allow user to input a probability distribution as a dictionary, and return numbers from that. Or add all probability distributions we currently have access to, and allow user to choose which one to use.~~

## convolve.js
An implementation of the convolution operator in JS. Takes two arrays as an input, and returns their convolution as another array. Can be used to calculate the probability distribution for a specific character's shards from opening two or more of the same capsule. 

To use:

1. Your input arrays should include all drop rates for the relevant character's shards, up to the maximum possible, even if zero, e.g for Strange's shards dropping from Strange's capsules: `[0.34, 0.32, 0, 0.26, 0, 0.08]`. (Note that the chance of getting 0 Strange shards from a single Strange capsule is 34%, and the chance of getting 2 or 4 shards is 0%.)
2. The function will return an array `conv` where the index of each value corresponds to the number of shards for that probability, e.g `conv[2]` is the probability that you will get two shards.
3. The probability distribution for opening two capsules is `b = convolve(a,a)`, where `a` is the initial probability distribution array. The probability distribution for opening three capsules is `c = convolve(b,a)`, where `b` is the probability distribution for opening two capsules. Basically, for each additional capsule you want to open, you convolve the current probability distribution array one more time with the initial probability distribution array.

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
