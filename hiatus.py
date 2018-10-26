import datetime
import math

class Episode:

    """A class for storing information about an episode.
    """

    def __init__(self, name, release_date, announcement_date=None):
        self.name = name
        self.release_date_string = release_date
        
        try:
            self.release_date = datetime.datetime.strptime(release_date, '%m/%d/%Y %H:%M')
        except ValueError:
            self.release_date = datetime.datetime.strptime(release_date, '%m/%d/%Y')
        
        if announcement_date != None:
            try:
                self.announcement_date = datetime.datetime.strptime(announcement_date, '%m/%d/%Y %H:%M')
            except ValueError:
                self.announcement_date = datetime.datetime.strptime(announcement_date, '%m/%d/%Y')
        else:
            self.announcement_date = None

class Duration:

    """A class for storing lengths of time.
    """

    def __init__(self, days=0, hours=0, minutes=0, seconds=0):
        self.days, self.hours, self.minutes, self.seconds = simplify(days, hours, minutes, seconds)

    def __add__(self, other):
        total_seconds = self.total_seconds() + other.total_seconds()
        return Duration(*simplify(seconds=total_seconds))

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        total_seconds = self.total_seconds() - other.total_seconds()
        return Duration(*simplify(seconds=total_seconds))

    def __abs__(self):
        return Duration(*simplify(seconds=abs(self.total_seconds)))

    def __str__(self):
        return self.format()

    def __eq__(self, other):
        if type(other) != Duration:
            return False
        return self.total_seconds() == other.total_seconds()
    def __ne__(self, other):
        if type(other) != Duration:
            return False
        return self.total_seconds() != other.total_seconds()
    def __gt__(self, other):
        if type(other) != Duration:
            return False
        return self.total_seconds() > other.total_seconds()
    def __lt__(self, other):
        if type(other) != Duration:
            return False
        return self.total_seconds() < other.total_seconds()
    def __ge__(self, other):
        if type(other) != Duration:
            return False
        return self.total_seconds() >= other.total_seconds()
    def __le__(self, other):
        if type(other) != Duration:
            return False
        return self.total_seconds() <= other.total_seconds()

    def format(self, format='%d %D, %h %H, %m %M, and %s %S'):
        """Turns the duration into a string with a supplied format (see README).
        """
        
        result = format
        
        replacements = [
            ['%d', str(self.days)],
            ['%D', plural('day', self.days)],
            ['%h', str(self.hours)],
            ['%H', plural('hour', self.hours)],
            ['%m', str(self.minutes)],
            ['%M', plural('minute', self.minutes)],
            ['%s', str(self.seconds)],
            ['%S', plural('second', self.seconds)]
        ]

        for replacement in replacements:
            result = result.replace(replacement[0], replacement[1])

        return result

    def total_seconds(self):
        """Returns the total number of seconds in the duration.
        """
        return total_seconds(self.days, self.hours, self.minutes, self.seconds)

class Hiatus:

    """A class for storing and handling the information of a hiatus.
    """
    
    def __init__(self, episode1, episode2=None):
        self.episode1 = episode1
        self.episode2 = episode2

    def __eq__(self, other):
        if type(other) != Hiatus:
            return False
        return self.length() == other.length()
    def __ne__(self, other):
        if type(other) != Hiatus:
            return False
        return self.length() != other.length()
    def __gt__(self, other):
        if type(other) != Hiatus:
            return False
        return self.length() > other.length()
    def __gt__(self, other):
        if type(other) != Hiatus:
            return False
        return self.length() < other.length()
    def __le__(self, other):
        if type(other) != Hiatus:
            return False
        return self.length() >= other.length()
    def __le__(self, other):
        if type(other) != Hiatus:
            return False
        return self.length() <= other.length()

    def __str__(self):
        if self.episode2 == None:
            return self.format("%f in between %1n and %2n")
        else:
            return self.format("%d %D in between %1n and %2n")

    def format(self, format='%f in between %e1 and %e2'):
        """Turns the hiatus into a string with a supplied format (see README).
        """
        result = format
        
        replacements = [
            ['%d', str(self.length().days)],
            ['%D', plural('day', self.length().days)],
            ['%h', str(self.length().hours)],
            ['%H', plural('hour', self.length().hours)],
            ['%m', str(self.length().minutes)],
            ['%M', plural('minute', self.length().minutes)],
            ['%s', str(self.length().seconds)],
            ['%S', plural('second', self.length().seconds)],
            ['%f', self.length().format()],
            ['%1n', self.episode1.name],
            ['%1r', self.episode1.release_date_string]
        ]
        if self.episode2 == None:
            replacements.append(['%2n', "now"])
            replacements.append(['%2r', 'sometime in the future'])
        else:
            replacements.append(['%2n', self.episode2.name])
            replacements.append(['%2r', self.episode2.release_date_string])

        for replacement in replacements:
            result = result.replace(replacement[0], replacement[1])

        return result

    def length(self):
        """Returns the length of the hiatus as a Duration object.
        """
        if self.episode2 == None:
            hiatus_delta = abs(datetime.datetime.now() - self.episode1.release_date)
        else:
            hiatus_delta = abs(self.episode2.release_date - self.episode1.release_date)
        return Duration(seconds=round(hiatus_delta.total_seconds()))
            
class HiatusGroup:

    """A class for storing multiple Hiatus objects, also including functions for dealing with them.
    """
    
    def __init__(self, hiatus_list=[]):
        self.hiatuses = list()
        
        for hiatus in hiatus_list:
            episode1 = Episode(*(hiatus[0]))
            if len(hiatus) == 1:
                self.current_hiatus = Hiatus(episode1)
                self.hiatuses.append(self.current_hiatus)
            elif len(hiatus) == 2:
                episode2 = Episode(*(hiatus[1]))
                self.hiatuses.append(Hiatus(episode1, episode2))

    def sorted(self):
        """Returns a list of Hiatus objects in order from longest (index 0) to shortest (index -1).
        """
        sorted = self.hiatuses[:]
        sorted.sort()
        return sorted

    def longest(self, number=None):
        """Returns the top <number> hiatuses, sorted by duration. If no number is provided, it will just return the longest episode.
        """
        if number == None:
            return self.sorted()[0]
        return self.sorted()[:number]

    def current_placement(self):
        """Returns the placement of the current hiatus relative to all of the others. For example, if the current hiatus is the 4th longest hiatus, it will return 4.
        """
        return self.sorted().index(self.current_hiatus) + 1

    def time_until_next_placement(self):
        """Returns a `Duration` object for the time until the current hiatus surpasses the next. If the hiatus is already the longest, returns `None`.
        """
        current_placement = self.current_placement()
        if current_placement == 1:
            return None
        return self.sorted()[current_placement - 2].length() - self.current_hiatus.length()
        

def simplify(days=0, hours=0, minutes=0, seconds=0):
    """Puts these four values into the simplest version, e.g. 73 seconds -> 1 minute 13 seconds.
    """

    neg = False
    seconds = total_seconds(days, hours, minutes, seconds)
    if seconds < 0:
        neg = True
    seconds = abs(seconds)
    days, hours, minutes = 0, 0, 0
    
    minutes += math.floor(seconds/60)
    seconds %= 60
    
    hours += math.floor(minutes/60)
    minutes %= 60

    days += math.floor(hours/24)
    hours %= 24

    if neg:
        return -days, -hours, -minutes, -seconds
    else:
        return days, hours, minutes, seconds

def total_seconds(days=0, hours=0, minutes=0, seconds=0):
    """Turns days, hours, minutes, and seconds into just seconds
    """
    return (((((days * 24) + hours) * 60) + minutes) * 60) + seconds

def plural(word, number=2):
    """Adds an 's' to the word if the number is greater than 1
    """
    if number == 1:
        return word
    else:
        return word + 's'
