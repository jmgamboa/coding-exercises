# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly  steps, for every step it was noted if it was an uphill, , or a downhill,  step. Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

# Example



# The hiker first enters a valley  units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.


hike = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
steps = 8


def countValleys(steps, path):
	sea_level = 0
	former_val = 0
	valleys = 0
	for i in path:
		former_val = sea_level
		if i == 'U':
			sea_level += 1
		else:
			sea_level -= 1

		if (sea_level == 0 and former_val < sea_level):
			valleys += 1
	print(valleys)


countValleys(8, hike)