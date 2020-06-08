"""
   best match for mentors to mentees, mentees win ties
Canterbury Tech, Christchurch, NZ
 Ian Wells, Calvin Giles
takes input from survey monkey to rank mentors and mentees


Based on:
@Author: Ryan Schachte
@Publication-Date: 1/12/17 5:23 PM
@Description:

The stable matching algorithm seeks to solve the problem of finding a stable match between two sets of equal size
given a list of preferences for each element.

We can define "matching" and "stable" by the following definitions.

Matching: Mapping from the elements of one set to the elements of another set
Stable: No element A of the first set that prefers an element B of the second set over its current partner
        such that element B prefers element A over its current partner.
"""
from stable_mentor.data_loader import load_data


def init_free_mentor(preferred_rankings_mentor):
    '''Initialize the arrays of mentee and mentor to represent
        that they're all initially free and not engaged'''

    # mentor who still need to propose and get accepted successfully
    free_mentor = []
    for mentor in preferred_rankings_mentor.keys():
        free_mentor.append(mentor)

    return free_mentor


def begin_matching(preferred_rankings_mentor, preferred_rankings_mentee, free_mentor, tentative_engagements, mentor):
    '''Find the first free mentee available to a mentor at
        any given time'''
    # Keep track of the people that "may" end up together

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
    return tentative_engagements


def stable_matching(preferred_rankings_mentor, preferred_rankings_mentee):
    '''Matching algorithm until stable match terminates'''
    free_mentor = init_free_mentor(preferred_rankings_mentor)
    tentative_engagements = []
    while (len(free_mentor) > 0):
        for mentor in free_mentor:
            tentative_engagements = begin_matching(preferred_rankings_mentor, preferred_rankings_mentee, free_mentor, tentative_engagements, mentor)
    print(free_mentor)
    return tentative_engagements
