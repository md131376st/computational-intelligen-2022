# computational-intelligen-2022
# Lab 2

## Algorithm description

My algorithm and code are based on the one-max example posted by the professor, fit to our problem and with the changes that follow below.

### Fitness definition
The fitness is define by the length of all the sets in are selected set and unique individual numbers 

### Genetic function changes
The changes we have made in indivual generation are:
- after each 30 steps we have mutation that add a random set form the problem space to one of are population sets 
- A cross-over generation is done frequently than mutation for crass validation I have used two random number to select the length use to add to are new genome


## Results

| N    | Ls   | Fitness      | Bloat | Time(# of fitness call) |
|------|------|--------------|-------|-------------------------|
| 5    | 5    | (5,5)        | 0%    | 100000                  |
| 10   | 10   | (10,10)      | 10%   | 100000                  |
| 20   | 24   | (20,24)      | 20%   | 100000                  | 
| 100  | 185  | (100,185)    | 85%   | 100000                  |
| 500  | 1658 | (500, 1590)  | 218%  | 100000                  |
| 1000 | 3559 | (1000, 3559) | 256%  | 100000                  |