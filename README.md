**Roulette-simulations**
========================
This code provides simulation of succes rate (and more data) of a roulette *strategy* I heard of once.
Using various parameters such as *starting budget*, *number of simulations (sample size)*, *color (red or black)* and *desired return* to compute the succes rate with the highiest possible precision.

*Strategy*
----------
Strategy is pretty simple. We choose a color we want to bet on. Either black or red (green is forbidden), we bet every round on the same color. Probability of succes is 48.65% per round.  

We bet relatively small amount **bet<sub>0</sub>** *(by defaul is this value set on bet = 1)*. Algorithm is as follows:  
- **i** ∈ N<sub>0</sub> *{0, 1, 2, 3, ...}*
- **i** is number of loses
- We bet: __bet<sub>0</sub>__*2<sup>**i**</sup>
- if we lose **i** += 1; if we win **i** = 0

If we win we bet amount **bet<sub>0</sub>**, if we lose we bet __bet<sub>0</sub>__*2<sup>1</sup> and if we lose again we bet __bet<sub>0</sub>__*2<sup>2</sup> and if we win then we bet again **bet<sub>0</sub>**.
As you can see, win with previous *i* losses; will give us right **bet<sub>0</sub>** (what is amount we would obtain at *i* = 0 losses).

>Lets's say our current balance is 10  
>We bet __bet<sub>0</sub>__ = 1  
>*lose*  
>Balance = 9  
>We bet __bet<sub>0</sub>__*2<sup>1</sup> = 2  
>*win*  
>Our balance is 11 which is amount we would have if we have won initial bet  

We repeat this algorithm either until next bet is greater than our balance or until we achieved our desired return.

*About script*
--------------
### Disclaimer  
I'm not a professional programmer, I can write some code in python. Senior programmers' eyes may bleed.   
**You have been warned**  
___
Whole code is just one big method with 4 parameters - *a, b, c, p*
- ***a*** - budget *(balance)*  
- ***b*** - sample size *(number of simulations)*  
- ***c*** - to choose color  
- ***p*** - desired return in % (0-100)

The script will simulate ***b*** games of rullete using the *strategy*. **Game is over** when your bet amount would be greater than current balance **or** when you reach/exceed __(1 + p/100)*a__, which is initial balance plus desired return.  
Parameter ***c*** actually don't play a role, because at infinite number of games is succes rate *(per round)* the same.  

After ***b*** games script provide chosen data, which is *average number of rounds per game*, *average number of rounds achieving the goal/return (won game)*, *average number of rounds of failed game* and ***succes rate***.









