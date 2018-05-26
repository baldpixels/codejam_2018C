# codejam_2018C
Google's Code Jam, Kickstart Round C (2018)

__problems to solve...__<br />
A) [Planet Distance](https://codejam.withgoogle.com/codejam/contest/4384486/dashboard)<br />
B) [Fairies and Witches](https://codejam.withgoogle.com/codejam/contest/dashboard?c=4384486#s=p1)<br />
C) [Kickstart Alarm](https://codejam.withgoogle.com/codejam/contest/dashboard?c=4384486#s=p2)<br />

I'm probably going to write most of this in Python.

### problem descriptions:
#### A) Planet Distance

There are N planets in the universe, and Google's Space division has installed N vacuum tubes through which you can travel from one planet to another. The tubes are bidirectional; travelers may use a tube between two planets to travel from either of those planets to the other. Each vacuum tube connects two planets and no two vacuum tubes connect the same pair of planets. These tubes connect the planets such that it is possible to travel from any planet to any other planet using one or more of them. Some of these tubes are connected such that there exists exactly one cycle in the universe. Google has hidden gifts in all the planets that are part of this cycle. Now, Google wants to know how far away each of the planets in the universe is from the gifts.

Your task is to find the minimum distance (in terms of the number of vacuum tubes) between each planet and a planet that is part of the cycle. Planets that are part of the cycle are assumed to be at distance 0.

Input
The first line contains an integer T, the number of test cases. T test cases follow. The first line of each test case contains an integer N, the number of planets and vacuum tubes. The planets are numbered from 1 to N.
N lines follow, the i-th of these lines contains two integers xi and yi, indicating that the i-th vacuum tube connects planet xi and planet yi.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a list of N space-separated values in which the i-th value represents the minimum distance between the i-th planet and a planet in the cycle.

Limits
1 ≤ T ≤ 100.
1 ≤ xi ≤ N, for all i.
1 ≤ yi ≤ N, for all i.
xi ≠ yi, for all i.
(xi, yi) ≠ (xj, yj), for all i ≠ j.
The graph in which planets are nodes and tubes are edges is connected and has exactly one cycle.
Small dataset
3 ≤ N ≤ 30.
Large dataset
3 ≤ N ≤ 1000.


#### B) Fairies and Witches


#### C) Kickstart Alarm


# coded by
Connor Rudmann a.k.a. "Vlad Pixels"
