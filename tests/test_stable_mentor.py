import stable_mentor


def test_stable_matching():
    preferred_rankings_mentor = {'daniella': ['ryan', 'josh', 'connor', 'blake'], 'zoey': ['connor', 'josh', 'ryan', 'blake'], 'sarah': ['ryan', 'blake', 'connor', 'josh'], 'lizzy': ['ryan', 'blake', 'josh', 'connor']}
    preferred_rankings_mentee = {'connor': ['lizzy', 'sarah', 'zoey', 'daniella'], 'blake': ['sarah', 'daniella', 'zoey', 'lizzy'], 'josh': ['sarah', 'lizzy', 'daniella', 'zoey'], 'ryan': ['lizzy', 'sarah', 'zoey', 'daniella']}
    tentative_engagements = stable_mentor.stable_matching(preferred_rankings_mentor, preferred_rankings_mentee)
    assert tentative_engagements == [['lizzy', 'ryan'], ['daniella', 'josh'], ['zoey', 'connor'], ['sarah', 'blake']]
