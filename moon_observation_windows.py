#!/usr/bin/env python

# Purpose:

# We are attempting to use the EDA to detect EME signals on 2m.

# Given the location of the antenna and the minimum elevation it can hear, we can calculate
# when the moon is visible. If the moon is more than 20 degrees away from the galactic centre
# at that time, we can use this observation window.

# Authors: Onno Benschop (VK6FLAB), Randall Wayth (VK6WR) and others

# This code is based on a Reddit contribution in the /amateurradio sub by /u/devnulling
# source: https://www.reddit.com/r/amateurradio/comments/aa7bcu/qrp_eme_project_update_1/ecpuied/

import ephem
import datetime
import time
import math

degrees_per_radian = 180.0 / math.pi

o = ephem.Observer()

# The location of the antenna - the EDA - https://www.mwatelescope.org/telescope/external/eda
o.lat = '-26.70331940'
o.lon = '116.67081524'
o.elevation = 377.8269
min_elevation = 90 - 45

current_time = datetime.datetime.now(datetime.timezone.utc).replace(minute=0, second=0)

next_year = current_time.year + 1

m = ephem.Moon()
s = ephem.Sun()

# source: https://stackoverflow.com/questions/11169523/how-to-compute-alt-az-for-given-galactic-coordinate-glon-glat-with-pyephem
galactic_center = ephem.Galactic(0, 0)
eq = ephem.Equatorial(galactic_center)
sg = ephem.FixedBody()
sg._ra = eq.ra
sg._dec = eq.dec
sg._epoch = eq.epoch

print("Time\tMoon Alt\tMoon Az\tSun Alt\tSun Az\tSG Alt\tSG Az")
while current_time.year < next_year:
	current_time += datetime.timedelta(hours=1)
	o.date = current_time
	m.compute(o)
	s.compute(o)
	sg.compute(o)
	malt = m.alt*degrees_per_radian
	maz = m.az*degrees_per_radian
	salt = s.alt*degrees_per_radian
	saz = s.az*degrees_per_radian
	sgalt = sg.alt*degrees_per_radian
	sgaz = sg.az*degrees_per_radian

	s_m_diff = abs(malt - salt)
	sg_m_diff = abs(malt - sgalt)
	
	if malt >= min_elevation and s_m_diff > 20 and sg_m_diff > 20:
		print("%s\t%4.1f\t%5.1f\t%4.1f\t%5.1f\t%4.1f\t%5.1f" % (current_time.strftime("%Y-%m-%d %H:%M"), malt, maz, salt, saz, sgalt, sgaz))
