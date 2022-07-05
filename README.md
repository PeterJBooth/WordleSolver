# W<span style="color: #787c7f">o</span><span style="color: #6ca965">r</span>dl<span style="color: 	#c8b653">e</span> S<span style="color: 	#6ca965">o</span><span style="color: 	#c8b653">l</span><span style="color: 	#787c7f">v</span>e<span style="color: 	#787c7f">r</span>

**Version 1.0**
 

---
### <span style="color:#6ca965">Description</span>

---

This solver provides you with the most **optimal** guess at any stage of the game, to help you solve the daily wordle in as few guesses as possible! 



---
### <span style="color:	#c8b653">How it Works</span> 

---
This Solver works by:
- **Filtering** out five-letter words that cannot be the answer based on previous results (i.e. combinations of <span style="color:#6ca965">greens</span>, 
  <span style="color:#EEA133">oranges</span> and <span style="color: #787c7f">blacks</span>).
- **Ranking** each five-letter word based on how many words they are expected to filter out if used as a guess. 

  
Finding the expected number of words filtered out from a guess involves:

* For each possible combination of greens, oranges and blacks.  
  * The number of words filtered out given that combination was the result.
  * The likelihood of that combination occurring.
* Using weighted a weight mean to find the expected number of words filtered out.
   

&nbsp;

🥇So what is the most optimal first guess? This program says <span style="color:#6ca965">**LARES**</span> 🥇

🤖 However, <span style="color:#6ca965">**LARES**</span> is probably more useful for the program rather than a human 🤖

---
### <span style="color:	#787c7f">Screenshots</span>

---
Starting Screen:

&nbsp;

![screenshot of wordle solver UI](screenshots/Wordle1.png)



&nbsp;

A guess has been inputted. The program has filtered out words and now shows the new best guesses:

&nbsp;

![screenshot of wordle solver UI](screenshots/Wordle2.png)

&nbsp;


---
### <span style="color:#6ca965"> To do</span>

---
* [ ] Improve the UI

* [ ] Incorporate the frequency of word usage in the english language when finding the most optimal word

---
### <span style="color:	#c8b653">License & copyright</span>  

---

© 2022 Peter Booth