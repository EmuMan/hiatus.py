# hiatus.py, a Python module for tracking hiatuses
## What is it?
As stated above, hiatus.py is a Python module built for the logging, tracking, and analyzing of hiatuses, and is part of a larger project I'm working on.  Although it was built for the purpose of tracking the hiatuses of Steven Universe, it was also made with flexibility in mind. All you have to do is enter the a list of episodes and release dates in the correct format, and it will work for any show. There is an included example file with all of the data for Steven Universe hiatuses entered in already.
## How does it work?
Within the module is a class called `HiatusGroup`, which is the one you want to use. First, as stated before, you need a list of episodes and release dates for it to use, and then when you create the `HiatusGroup` object you need to pass that in.
```
import hiatus

hiatus_list = [...]

hiatuses = hiatus.HiatusGroup(hiatus_list)
```
The hiatus list should follow this format:
```
hiatus_list = [
    [["<name>", "<release_date>"], ["<name>", "<release_date>"]],
    [["<name>", "<release_date>"], ["<name>", "<release_date>"]],
    [["<name>", "<release_date>"], ["<name>", "<release_date>"]],
    [["<latest_ep_name>", "<latest_ep_release_date>"]]
]
```
where each row is a different hiatus, each list in that row is an episode, each `<name>` is the name of that episode, and each `<release_date>` is the release date of that episode.
## What does it do?
The hiatus tracker can do a fair amount of things, and is most likely going to continue to support more. Right now, these are the working variables/functions within each class:
 * **`HiatusGroup`** holds a list of `Hiatus` objects as well as functions for dealing with them
   * **`hiatuses`**: the list of `Hiatus` objects in the original order.
   * **`current_hiatus`**: the `Hiatus` object for the episode that did not have a superseding episode defined, making it the most recent episode.
   * **`sorted()`**: Returns a list of Hiatus objects in order from longest (index 0) to shortest (index -1).
   * **`longest(number=None)`**: Returns the top `<number>` hiatuses, sorted by duration. If no number is provided, it will just return the longest episode.
   * **`current_placement()`**: Returns the placement of the current hiatus relative to all of the others. For example, if the current hiatus is the 4th longest hiatus, it will return 4.
   * **`time_until_next_placement()`**: Returns a `Duration` object for the time until the current hiatus surpasses the next. If the hiatus is already the longest, returns `None`.
 * **`Hiatus`** holds one to two `Episode` objects as well as functions for dealing with them
   * **`episode1`**: the `Episode` object for the episode that marked the beginning of the hiatus.
   * **`episode2`**: the `Episode` object for the episode that marked the end of the hiatus, if such an episode exists. If one was not given, i.e. this is the current episode/hiatus, this variable will be set to `None`.
   * **`format(format='%f in between %e1 and %e2')`**: takes a format string (see below) and returns a formatted string.
   * **`length()`**: returns the `Duration` object for the length of the hiatus. It is a function and not a variable because the length of the current hiatus is always changing.
 * **`Episode`** holds information on an episode.
   * **`name`**: the name of the episode.
   * **`release_date`**: the release date of the episode in the form of a `datetime.datetime` object.
   * **`release_date_string`**: the release date of the episode in the format it was passed into the `HiatusGroup` initialization.
   * **`announcement_date`**: at the moment, doesn't do anything. Don't worry about this.
 * **`Duration`**: holds a length of time.
   * **`days`**, **`hours`**, **`minutes`**, and **`seconds`**: self-explanatory, holds the values corresponding to their names.
   * **`format(format='%d %D, %h %H, %m %M, and %s %S')`**: takes a format string (see below) and returns a formatted string.
   * **`total_seconds()`**: returns the total number of seconds in the duration.
## Format strings
Here is a list of format codes you can use in format strings for `Hiatus` and `Duration` objects:
 * `%d`: the number of days in the duration/hiatus length.
 * `%D`: "day" if the number of days is 1, "days" if it is not.
 * `%h`: the number of hours in the duration/hiatus length.
 * `%H`: "hour" if the number of hours is 1, "hours" if it is not.
 * `%m`: the number of minutes in the duration/hiatus length.
 * `%M`: "minute" if the number of minutes is 1, "minutes" if it is not.
 * `%s`: the number of seconds in the duration/hiatus length.
 * `%S`: "second" if the number of seconds is 1, "seconds" if it is not.
 * `%f`: the associated duration formatted with the default string (`%d %D, %h %H, %m %M, and %s %S`) (only in `Hiatus` objects).
 * `%1n`: the name of the episode before the hiatus (only in `Hiatus` objects).
 * `%2n`: the name of the episode that ended the hiatus (if it does not exist it is replaced with "now") (only in `Hiatus` objects).
 * `%1r`: the release date of the episode before the hiatus (only in `Hiatus` objects).
 * `%2n`: the release date of the episode that ended the hiatus (if it does not exist it is replaced with "sometime in the future") (only in `Hiatus` objects).
## Help.
If something's not working correctly, feel free to open an issue. If it is relatively minor, you can just message me on Discord (@EmuMan#2495).
