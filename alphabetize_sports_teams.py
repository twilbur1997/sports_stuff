import pprint


nfl_teams = [
"Arizona Cardinals","Atlanta Falcons","Carolina Panthers","Chicago Bears","Dallas Cowboys","Detroit Lions","Green Bay Packers",
"Los Angeles Rams","Minnesota Vikings","New Orleans Saints","New York Giants","Philadelphia Eagles","San Francisco 49ers",
"Seattle Seahawks","Tampa Bay Buccaneers","Washington Commanders","Baltimore Ravens","Buffalo Bills","Cincinnati Bengals",
"Cleveland Browns","Denver Broncos","Houston Texans","Indianapolis Colts","Jacksonville Jaguars","Kansas City Chiefs",
"Las Vegas Raiders","Los Angeles Chargers","Miami Dolphins","New England Patriots","New York Jets","Pittsburgh Steelers",
"Tennessee Titans"]



def nfl_sort(print_teams=True):
    print("NFL TEAM DATA\n")
    alphabet = []
    for x in range(26):
        letter = 65 + x 
        alphabet.append(chr(letter))

    # print(alphabet)
    # print("\n\n")
    alphabet2 = alphabet[:]
    name_alphabet = alphabet[:]
    loc_alphabet = alphabet[:]

    nfl_team_dict = {}
    nfl_team_loc_dict = {}

    for team in nfl_teams:
        team_name = team.split(" ")[-1]
        team_location = " ".join(team.split(" ")[:-1])

        if team_name[0] not in nfl_team_dict: # Check if first letter already indexed
            nfl_team_dict[team_name[0]] = []
            if team_name[0] in name_alphabet:
                name_alphabet.remove(team_name[0])
            if team_name[0] in alphabet2:
                alphabet2.remove(team_name[0])
        nfl_team_dict[team_name[0]].append(team_name)

        if team_location[0] not in nfl_team_loc_dict: # Check if first letter already indexed
            nfl_team_loc_dict[team_location[0]] = []
            if team_location[0] in loc_alphabet:
                loc_alphabet.remove(team_location[0])
            if team_location[0] in alphabet2:
                alphabet2.remove(team_location[0])
        nfl_team_loc_dict[team_location[0]].append(team_location)

    print("\n\nAlphabets:")
    print(alphabet)
    print("\nLetters not in Names")
    print(name_alphabet)
    print("\nLetters not in Locations")
    print(loc_alphabet)
    print("\nLetters not in Names or Locations")
    print(alphabet2)
    

    pp = pprint.PrettyPrinter(indent=4, compact=True)
    print("\n\nTeam Names\n\n")


       
    pp.pprint(nfl_team_dict)
    print("\n\n")

    for elt in nfl_team_dict.keys():
        nfl_team_dict[elt] = len(nfl_team_dict[elt])
    sorted_nfl_team_dict = sorted(nfl_team_dict.items(), key=lambda x:x[1], reverse=True)
    # nfl_team_dict = dict(sorted_nfl_team_dict)

    pp.pprint(sorted_nfl_team_dict)
    print("\n\n\nTeam Locations\n")


    pp.pprint(nfl_team_loc_dict)
    print("\n\n")

    for elt in nfl_team_loc_dict.keys():
        nfl_team_loc_dict[elt] = len(nfl_team_loc_dict[elt])
    sorted_nfl_team_loc_dict = sorted(nfl_team_loc_dict.items(), key=lambda x:x[1], reverse=True)
    # nfl_team_loc_dict = dict(sorted_nfl_team_loc_dict)

    pp.pprint(sorted_nfl_team_loc_dict)
    print("\n\nNFL TEAM DATA COMPLETED\n\n")
        

def main():
    print("Starting program.\n")
    nfl_sort()
    print("\n\nProgram Complete.")


if __name__ == "__main__":
    main()