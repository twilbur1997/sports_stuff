import pprint
from datetime import datetime


nfl_teams = [
"Arizona Cardinals","Atlanta Falcons","Carolina Panthers","Chicago Bears","Dallas Cowboys","Detroit Lions","Green Bay Packers",
"Los Angeles Rams","Minnesota Vikings","New Orleans Saints","New York Giants","Philadelphia Eagles","San Francisco 49ers",
"Seattle Seahawks","Tampa Bay Buccaneers","Washington Commanders","Baltimore Ravens","Buffalo Bills","Cincinnati Bengals",
"Cleveland Browns","Denver Broncos","Houston Texans","Indianapolis Colts","Jacksonville Jaguars","Kansas City Chiefs",
"Las Vegas Raiders","Los Angeles Chargers","Miami Dolphins","New England Patriots","New York Jets","Pittsburgh Steelers",
"Tennessee Titans"]

mlb_teams = [
"Chicago White Sox","Cleveland Guardians","Detroit Tigers","Kansas City Royals","Minnesota Twins","Baltimore Orioles",
"Boston Red Sox","New York Yankees","Tampa Bay Rays","Toronto Blue Jays","Houston Astros","Los Angeles Angels",
"Oakland Athletics","Seattle Mariners","Texas Rangers","Chicago Cubs","Cincinnati Reds","Milwaukee Brewers",
"Pittsburgh Pirates","St. Louis Cardinals","Atlanta Braves","Miami Marlins","New York Mets","Philadelphia Phillies",
"Washington Nationals","Arizona Diamondbacks","Colorado Rockies","Los Angeles Dodgers","San Diego Padres",
"San Francisco Giants"]

nhl_teams = [
"Carolina Hurricanes","Columbus Blue Jackets","New Jersey Devils","New York Islanders","New York Rangers",
"Philadelphia Flyers","Pittsburgh Penguins","Washington Capitals","Boston Bruins","Buffalo Sabres","Detroit Red Wings",
"Florida Panthers","Montréal Canadiens","Ottawa Senators","Tampa Bay Lightning","Toronto Maple Leafs","Arizona Coyotes",
"Chicago Blackhawks","Colorado Avalanche","Dallas Stars","Minnesota Wild","Nashville Predators","St. Louis Blues",
"Winnipeg Jets","Anaheim Ducks","Calgary Flames","Edmonton Oilers","Los Angeles Kings","San Jose Sharks","Seattle Kraken",
"Vancouver Canucks","Vegas Golden Knights"]

nba_teams = [
"Boston Celtics","Brooklyn Nets","New York Knicks","Philadelphia 76ers","Toronto Raptors","Chicago Bulls",
"Cleveland Cavaliers","Detroit Pistons","Indiana Pacers","Milwaukee Bucks","Atlanta Hawks","Charlotte Hornets",
"Miami Heat","Orlando Magic","Washington Wizards","Denver Nuggets","Minnesota Timberwolves","Oklahoma City Thunder",
"Portland Trail Blazers","Utah Jazz","Golden State Warriors","LA Clippers","Los Angeles Lakers","Phoenix Suns",
"Sacramento Kings","Dallas Mavericks","Houston Rockets","Memphis Grizzlies","New Orleans Pelicans","San Antonio Spurs"]

# Most common across MLB, NFL, NHL, NBA?
# Giants, Kings, Cardinals, Jets, Panthers, Rangers, 

team_list = nhl_teams
output_file = "nhl_output.txt"
name_exceptions_two_word = ["Sox","Blue Jays","Trail Blazers","Blue Jackets","Red Wings","Maple Leafs","Golden Knights"]

def alphabet():
    alphabet = []
    for x in range(26):
        letter = 65 + x 
        alphabet.append(chr(letter))
    return alphabet


def alphabet_printout(alphabet1,alphabet2,name_alphabet,loc_alphabet, alphabet_print):
    if alphabet_print:
        print("\n\nAlphabets:\n", alphabet1)
        print("\nLetters not in Names\n", name_alphabet)
        print("\nLetters not in Locations\n", loc_alphabet)
        print("\nLetters not in Names or Locations\n", alphabet2)

    with open(output_file, "a") as f:
        f.write("Full Alphabet\n"+ str(alphabet1))
        f.write("\n\nLetters not in Names\n"+ str(name_alphabet))
        f.write("\n\nLetters not in Locations\n"+ str(loc_alphabet))
        f.write("\n\nLetters not in Names or Locations\n"+ str(alphabet2))


def team_name_loc_process(team_list, alphabet_print):    
    alphabet1 = alphabet()
    alphabet2,name_alphabet,loc_alphabet = alphabet1[:],alphabet1[:],alphabet1[:]

    team_name_dict = {}
    team_loc_dict = {}

    for team in team_list:
        team_name = team.split(" ")[-1]
        team_location = " ".join(team.split(" ")[:-1])
        
        if any(exception in team for exception in name_exceptions_two_word):
            team_name = " ".join(team.split(" ")[1:])
            team_location = team.split(" ")[0]

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

    alphabet_printout(alphabet1,alphabet2,name_alphabet,loc_alphabet, alphabet_print)

    return team_name_dict, team_loc_dict


def team_elements_printout(team_name_dict, team_loc_dict):
    pp = pprint.PrettyPrinter(indent=4, compact=True)
    with open(output_file, "a") as f:
        print("\n\nTeam Names\n\n")
        f.write("\n\nTeam Names\n\n")
        pp.pprint(team_name_dict)
        pprint.pprint(team_name_dict, f)
        print("\n\n")
        f.write("\n\n")

        for elt in team_name_dict.keys():
            team_name_dict[elt] = len(team_name_dict[elt])
        sorted_team_name_dict = sorted(team_name_dict.items(), key=lambda x:x[1], reverse=True)
        # team_name_dict = dict(sorted_team_name_dict)

        pp.pprint(sorted_team_name_dict)
        pprint.pprint(sorted_team_name_dict, f)
        print("\n\n\nTeam Locations\n")
        f.write("\n\n\nTeam Locations\n")

        pp.pprint(team_loc_dict)
        pprint.pprint(team_loc_dict, f)
        print("\n\n")
        f.write("\n\n")

        for elt in team_loc_dict.keys():
            team_loc_dict[elt] = len(team_loc_dict[elt])
        sorted_team_loc_dict = sorted(team_loc_dict.items(), key=lambda x:x[1], reverse=True)
        # team_loc_dict = dict(sorted_team_loc_dict)

        pp.pprint(sorted_team_loc_dict)
        pprint.pprint(sorted_team_loc_dict, f)
        return
    

def team_process(team_list, alphabet_print=True):
    team_name_dict,team_loc_dict = team_name_loc_process(team_list, alphabet_print)
    team_elements_printout(team_name_dict, team_loc_dict)
    

def main():
    print("Starting program.\n")
    with open(output_file, "w") as f:
        f.write("Last run: ")
        now = datetime.now()
        current_time = now.strftime("%Y/%m/%d - %H:%M:%S")
        f.write(current_time)
        f.write("\n\n")

    team_process(team_list)
    print("\n\nTEAM DATA COMPLETED")
    print("\n\nProgram Complete.")


if __name__ == "__main__":
    main()



