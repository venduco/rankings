import pandas


def load_data(data_path):
    return pandas.read_excel(data_path, header=[0, 1])


def parse_data(df):
    preferred_rankings_mentee = {}
    preferred_rankings_mentor = {}

    for i, row in df.iterrows():
        name = row["Select your name"].iloc[0]  # change this for production
        yes_mentee = row["Are you a mentor or mentee?"].iloc[1]
        yes_mentor = row["Are you a mentor or mentee?"].iloc[0]

        if (yes_mentor == "Mentor"):
            print("I am a mentor", name, "\n")
            my_mentees = row["Rank your choices of mentee from 1 ( most preferable) to least"]
            preferred_rankings_mentee[name] = get_sorted_rankings(my_mentees)
            print("my mentees:", i, name, "\n", my_mentees, "\n", preferred_rankings_mentee)
        elif (yes_mentee == "Mentee"):
            print("I am a mentee", name)
            my_mentors = row["Rank your choices of mentor from 1 ( most preferable) to least"]
            my_sorted_mentors = my_mentors.sort_values(ascending=True)
            preferred_rankings_mentor[name] = get_sorted_rankings(my_mentors)

            print("my mentors:", i, name, "\n", my_mentors, "\n", preferred_rankings_mentor)
        else:
            print("error in spreadsheet")

    return preferred_rankings_mentor, preferred_rankings_mentee


def get_sorted_rankings(rankings):
    my_sorted_rankings = rankings.sort_values(ascending=True)
    return [
        person_name
        for person_name, rank
        in my_sorted_rankings.iteritems()
    ]
