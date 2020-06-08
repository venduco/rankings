from stable_mentor import stable_matching
from stable_mentor.data_loader import load_data, parse_data


def main():
    df = load_data("../data/testdata9.xlsx")
    preferred_rankings_mentor, preferred_rankings_mentee = parse_data(df)

    tentative_engagements = stable_matching(preferred_rankings_mentor, preferred_rankings_mentee)
    print("BEST MATCHES" , tentative_engagements)


if __name__ == "__main__":
    main()
