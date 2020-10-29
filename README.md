# moon-observations

We are attempting to use the [EDA](https://www.mwatelescope.org/telescope/external/eda) radio telescope to detect EME signals on 2m
as a pre-cursor to making QRP transmissions from VK6 to the moon (and back).

Given the location of the antenna and the minimum elevation it can observe, we can calculate
when the moon is visible. If the moon is more than 20 degrees away from the sun and
the galactic centre at that time, we can use this observation window.

# Origins

Based on discussion between Randall and Onno, an initial attempt was made to write this
code. A "Foundations of Amateur Radio" podcast episode ([#186](http://podcasts.itmaze.com.au/foundations/#186)) discussed this project and some
of the issues were described with the then Astropy-based implementation.

Redditor /u/devnulling wrote a [new piece of software](https://www.reddit.com/r/amateurradio/comments/aa7bcu/qrp_eme_project_update_1/ecpuied/) that addressed many of the issues
described in the podcast. That code forms the basis of this tool with the additional
calculations to include the location of the galactic centre which also prevents
useful observations (since it's a really strong radio source like the sun).

In the year between the podcast and publication of this tool the EDA has been
upgraded to be able to observe a larger slice of the sky by changing its minimum
elevation from 70 degrees down to 45 degrees. The code was updated to reflect
that upgrade.


# Authors:
* /u/devnulling
* Onno Benschop (VK6FLAB)
* Randall Wayth (VK6WR)
* and others
