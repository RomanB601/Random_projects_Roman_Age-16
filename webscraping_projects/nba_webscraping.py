from bs4 import BeautifulSoup
import requests
# could have a bug if you searching for people with the same or similar names as other nba players


def main():
    print("What NBA Player do you want stats on?")
    player = str(input(">"))
    player_new,let = player_algo(player) #makes the input the html requirement
    html_text = requests.get(f"https://www.basketball-reference.com/players/{let}/{player_new}.html").text
    soup = BeautifulSoup(html_text, "html5lib")
    stats = soup.find_all("div", class_="stats_pullout")
    stats1 , stats2 = get_stats(stats) # assigns stats1 as the dictorary for stats1 and stats2 as the dict for stats2
    print(split_dict_print(stats1, stats2, player)) #prints everything out

def get_stats(stats_html): #gets the stats using Beautiful Soup
    my_dict1 = {} # Makes a dict to store p1 of the stats and part 2 for dict2 
    my_dict2 = {}
    for stat in stats_html: 
        inner_stats_p1 = stat.find_all("div", class_ = "p1")
        inner_stats_p2 = stat.find_all("div", class_ = "p2")
        for p1 in inner_stats_p1: # gets stats for part 1
            p1 = p1.find_all("p")
            my_dict1["Games"] = p1[1].text.strip()
            my_dict1["Pts"] = p1[3].text.strip()
            my_dict1["TRB"] = p1[5].text.strip()
            my_dict1["AST"] = p1[7].text.strip()
        for p2 in inner_stats_p2: # gets stats from part 2
            p2 = p2.find_all("p")
            my_dict2["FG%"] = p2[1].text.strip()
            my_dict2["FG3%"] = p2[3].text.strip()
            my_dict2["FGT%"] = p2[5].text.strip()
    return my_dict1, my_dict2

def split_dict_print(dict1, dict2,player): # prints out the stats, basically a to string
    print (f'\n{player} has had {dict1["Games"]} Games, a average of {dict1["Pts"]} Points per Game, {dict1["TRB"]} Rebounds per Game, {dict1["AST"]} Assists per Game')
    return f'{player} has had a {dict2["FG%"]} Shot%, {dict2["FG3%"]} 3-Point %, {dict2["FGT%"]} FreeThrow%'

def player_algo(player): # makes the player name the link required name and gets the first letter of the last name
    try:
        if player.replace(" ","") != player:
            first, last = player.split(" ")
            letter = last[0]
            if len(last) >= 6: # if last name is smaller than 6 than don't get rid of letters
                newlast = last[:len(last)-1] + last[len(last):]
                newfirst = first[:2]
                newname = newlast + newfirst + "01"
                return newname, letter
            else:
                newfirst = first[:2]
                newname = last + newfirst + "01"
                return newname, letter
        else:
            raise TypeError
    except ValueError:
        print("Enter a Real NBA Player\n")
        main()
    except TypeError:
        print("Please put spaces between the first and last name\n")
        main()
if __name__ == "__main__":
    main()