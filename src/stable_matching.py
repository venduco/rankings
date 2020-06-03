'''
 ____  _        _     _      __  __       _       _     _                _    _                  _ _   _               
/ ___|| |_ __ _| |__ | | ___|  \/  | __ _| |_ ___| |__ (_)_ __   __ _   / \  | | __ _  ___  _ __(_) |_| |__  _ __ ___  
\___ \| __/ _` | '_ \| |/ _ \ |\/| |/ _` | __/ __| '_ \| | '_ \ / _` | / _ \ | |/ _` |/ _ \| '__| | __| '_ \| '_ ` _ \ 
 ___) | || (_| | |_) | |  __/ |  | | (_| | || (__| | | | | | | | (_| |/ ___ \| | (_| | (_) | |  | | |_| | | | | | | | |
|____/ \__\__,_|_.__/|_|\___|_|  |_|\__,_|\__\___|_| |_|_|_| |_|\__, /_/   \_\_|\__, |\___/|_|  |_|\__|_| |_|_| |_| |_|
                                                                |___/           |___/                                  

@Author: Ryan Schachte
@Publication-Date: 1/12/17 5:23 PM
@Description: 

The stable matching algorithm seeks to solve the problem of finding a stable match between two sets of equal size
given a list of preferences for each element. 

We can define "matching" and "stable" by the following definitions.

Matching: Mapping from the elements of one set to the elements of another set
Stable: No element A of the first set that prefers an element B of the second set over its current partner
		such that element B prefers element A over its current partner. 
'''
import collections

#The mentee that the mentor prefer
preferred_rankings_mentor = {
	'ryan': 	['lizzy', 'sarah', 'zoey', 'daniella'],
	'josh': 	['sarah', 'lizzy', 'daniella', 'zoey'],
	'blake': 	['sarah', 'daniella', 'zoey', 'lizzy'],
	'connor': 	['lizzy', 'sarah', 'zoey', 'daniella']
}

#The mentor that the mentee prefer
preferred_rankings_mentee = {
	'lizzy': 	['ryan', 'blake', 'josh', 'connor'],
	'sarah': 	['ryan', 'blake', 'connor', 'josh'],
	'zoey':  	['connor', 'josh', 'ryan', 'blake'],
	'daniella':	['ryan', 'josh', 'connor', 'blake'] 
}

#Keep track of the people that "may" end up together
tentative_engagements 	= []

#mentor who still need to propose and get accepted successfully
free_mentor 				= []

def init_free_mentor():
	'''Initialize the arrays of mentee and mentor to represent 
		that they're all initially free and not engaged'''
	for mentor in preferred_rankings_mentor.keys():
		free_mentor.append(mentor)

def begin_matching(mentor):
	'''Find the first free mentee available to a mentor at
		any given time'''

	print("DEALING WITH %s"%(mentor))
	for mentee in preferred_rankings_mentor[mentor]:

		#Boolean for whether mentee is taken or not
		taken_match = [couple for couple in tentative_engagements if mentee in couple]

		if (len(taken_match) == 0):
			#tentatively engage the mentor and mentee
			tentative_engagements.append([mentor, mentee])
			free_mentor.remove(mentor)
			print('%s is no longer a free mentor and is now tentatively engaged to %s'%(mentor, mentee))
			break

		elif (len(taken_match) > 0):
			print('%s is taken already..'%(mentee))

			#Check ranking of the current dude and the ranking of the 'to-be' dude
			current_guy = preferred_rankings_mentee[mentee].index(taken_match[0][0])
			potential_guy = preferred_rankings_mentee[mentee].index(mentor)

			if (current_guy < potential_guy):
				print('She\'s satisfied with %s..'%(taken_match[0][0]))
			else: 
				print('%s is better than %s'%(mentor, taken_match[0][0]))
				print('Making %s free again.. and tentatively engaging %s and %s'%(taken_match[0][0], mentor, mentee))
				
				#The new guy is engaged
				free_mentor.remove(mentor)

				#The old guy is now single
				free_mentor.append(taken_match[0][0])

				#Update the fiance of the mentee (tentatively)
				taken_match[0][0] = mentor
				break

def stable_matching():
	'''Matching algorithm until stable match terminates'''
	while (len(free_mentor) > 0):
		for mentor in free_mentor:
			begin_matching(mentor)


def main():
	init_free_mentor()
	print(free_mentor)
	stable_matching()
	print(tentative_engagements)

main()
