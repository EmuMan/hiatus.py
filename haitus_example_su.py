import hiatus

hiatus_list = [
    [['Bubble Buddies', '12/02/2013'], ['Serious Steven', '01/13/2014']],
    [["Steven's Lion", '01/27/2014'], ['Arcade Mania', '02/17/2014']],
    [['Onion Trade', '03/17/2014'], ['Steven the Sword Fighter', '04/09/2014']],
    [['Steven the Sword Fighter', '04/09/2014'], ['Lion 2: The Movie', '04/23/2014']],
    [['Beach Party', '04/30/2014'], ["Rose's Room", '05/14/2014']],
    [["Rose's Room", '05/14/2014'], ['Coach Steven', '08/21/2014']],
    [['Lion 3: Straight to Video', '12/04/2014'], ['Warp Tour', '01/08/2015']],
    [['Reformed', '04/30/2015'], ['Sworn to the Sword', '06/15/2015']],
    [['Chille Tid', '06/19/2015'], ['Cry for Help', '07/13/2015']],
    [['Friend Ship', '07/17/2015'], ['Nightmare Hospital', '09/10/2015']],
    [['Too Far', '10/14/2015'], ['The Answer', '01/04/2016']],
    [['Log Date 7 15 2', '01/08/2016'], ['Super Watermelon Island', '05/12/2016']],
    [['Steven Floats', '05/22/2016'], ['Drop Beat Dad', '07/18/2016']],
    [['Onion Gang', '09/15/2016'], ['Gem Harvest', '11/17/2016']],
    [['Three Gems and a Baby', '12/01/2016'], ["Steven's Dream", '01/02/2017']],
    [['Room for Ruby', '03/10/2017'], ['Lion 4: Alternate Ending', '03/30/2017']],
    [['Lion 4: Alternate Ending', '03/30/2017'], ['Doug Out', '05/05/2017']],
    [['Stuck Together', '05/10/2017'], ['The Trial', '05/29/2017']],
    [["Lars' Head", '05/29/2017'], ['Dewey Wins', '11/10/2017']],
    [['Kevin Party', '11/10/2017'], ['Lars of the Stars', '01/05/2018']],
    [['Jungle Moon', '01/05/2018'], ['Your Mother and Mine', '03/26/2018']],
    [['A Single Pale Rose', '05/07/2018'], ["Now We're Only Falling Apart", '07/02/2018']],
    [['Reunited', '07/06/2018'], ['Legs From Here to Homeworld', '07/21/2018 15:30']],
    [['Legs From Here to Homeworld', '07/21/2018 15:30']]
]

def ordinal(n):
    return "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

# create a hiatus group (stores hiatuses) with the list of hiatuses
hiatuses = hiatus.HiatusGroup(hiatus_list)

# print the length of the current hiatus
print("\nCurrent hiatus:")
print(hiatuses.current_hiatus)

# uses custom formatting to print only the days
print("\nCurrent hiatus simpler form:")
print(hiatuses.current_hiatus.format('%d %D in between %1n and %2n'))

# uses sorted() to list all episodes from longest to shortest
print("\nAll hiatuses in order from longest to shortest:")
for h in hiatuses.sorted():
    print(h)

# uses longest() to list the top 5 longest hiatuses
print("\nTop 5 longest hiatuses:")
for h in hiatuses.longest(5):
    print(h)

# uses longest() with no arguments to get the longest hiatus
print("\nLongest hiatus:")
print(hiatuses.longest())

# gets the index of the current hiatus
print("\nThe current hiatus is the %s longest hiatus." % ordinal(hiatuses.current_placement()))

# gets the time until the length of the current haitus surpasses the length of the next
time_until = hiatuses.time_until_next_placement()
if time_until == None:
    print("This hiatus is already the longest hiatus.")
else:
    print("\nThere are %s until this is the %s longest hiatus." % (str(time_until), ordinal(hiatuses.current_placement() - 1)))

