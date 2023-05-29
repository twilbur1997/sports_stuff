
def nfl_sort():
    print("NFL TEAM DATA\n")
    alphabet1 = alphabet()
    alphabet2,name_alphabet,loc_alphabet = alphabet1[:],alphabet1[:],alphabet1[:]

    team_name_dict = {}
    team_loc_dict = {}

    for team in nfl_teams:
        team_name = team.split(" ")[-1]
        team_location = " ".join(team.split(" ")[:-1])

        if team_name[0] not in team_name_dict: # Check if first letter already indexed
            team_name_dict[team_name[0]] = []
            if team_name[0] in name_alphabet:
                name_alphabet.remove(team_name[0])
            if team_name[0] in alphabet2:
                alphabet2.remove(team_name[0])
        team_name_dict[team_name[0]].append(team_name)

        if team_location[0] not in team_loc_dict: # Check if first letter already indexed
            team_loc_dict[team_location[0]] = []
            if team_location[0] in loc_alphabet:
                loc_alphabet.remove(team_location[0])
            if team_location[0] in alphabet2:
                alphabet2.remove(team_location[0])
        team_loc_dict[team_location[0]].append(team_location)

    print("\n\nAlphabets:")
    print(alphabet1)
    print("\nLetters not in Names")
    print(name_alphabet)
    print("\nLetters not in Locations")
    print(loc_alphabet)
    print("\nLetters not in Names or Locations")
    print(alphabet2)
    

    pp = pprint.PrettyPrinter(indent=4, compact=True)
    print("\n\nTeam Names\n\n")
       
    pp.pprint(team_name_dict)
    print("\n\n")

    for elt in team_name_dict.keys():
        team_name_dict[elt] = len(team_name_dict[elt])
    sorted_team_name_dict = sorted(team_name_dict.items(), key=lambda x:x[1], reverse=True)
    # team_name_dict = dict(sorted_team_name_dict)

    pp.pprint(sorted_team_name_dict)
    print("\n\n\nTeam Locations\n")


    pp.pprint(team_loc_dict)
    print("\n\n")

    for elt in team_loc_dict.keys():
        team_loc_dict[elt] = len(team_loc_dict[elt])
    sorted_team_loc_dict = sorted(team_loc_dict.items(), key=lambda x:x[1], reverse=True)
    # team_loc_dict = dict(sorted_team_loc_dict)

    pp.pprint(sorted_team_loc_dict)
    print("\n\nNFL TEAM DATA COMPLETED\n\n")


def main():
    print("Starting program.\n")
    nfl_sort()
    print("\n\nProgram Complete.")


if __name__ == "__main__":
    main()

