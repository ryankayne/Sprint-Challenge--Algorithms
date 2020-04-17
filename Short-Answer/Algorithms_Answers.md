#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
Time: O(n)
Space: O(1)

As n increases, the amount of time to do operations also increase, but by a steady amount. For every 1 integer you increase, the steps involved increase by 2. That's linear.

And space is constant because there is no increase in space depending on how big the number is, it just uses one slot of memory.


b)
Time: O(n^2)
Space: O(1)

As n increases, the time for operations also increases, but not in a consistent fashion. Regardless, time is increasing the time needed to process in an exponential fashion in relation to n, not to the previous time which I was at first thinking. The space is constant though, since every iteration takes up the same amount of space for variables i, sum, j, and n.


c)
Time: O(n)
Space: O(n)

As n increases, the time increase in a linear fashion. As n increases by an integer, an additional 4 steps are added to the process. In terms of space, the stack grows at a consistent rate during calculations as n increases so that relationship is also linear.

## Exercise II

The way to understand this problem is to consider all the variables involved, namely gravity, the eggs, and the fact that building floors have a tall height. In order to test this, you would implement a linear approach. Start on floor = 0, the ground floor, throw the egg (drop_egg function), see if it breaks(if egg_break == True, then return f, else f + 1 drop_egg()). If it breaks, record the floor you are on and then you are done. If it doesn't break, go to the next floor and do it again until the egg breaks.

The runtime complexity I believe is O(n), because if we pretend that eggs wouldn't break immediately from dropping it at arms level, we can assume that travelling up to each floor would take the same amount of time. So if ground floor took 1 second, then the second floor took 30 seconds (to do stairs and then drop the egg) and so on, every floor is adding the same increment of time, therefore as n (or f) increases, so does the time at a consistent level.

(but maybe I'm wrong in this and I'm thinking of space complexity. It's hard to know in the real world example. The egg dropping process (the act of walking up stairs and dropping the egg) takes the same amount of time after the intial case, so that could be considered constant O(1), but if it's in respect to n (f), it would take you longer to climb the stairs to floor 10, than floor 2, so maybe it is O(n)... haha) 

Also, I don't know how crazy this is going to be, but if you are also being picky and considering real world physics (in which the egg breaks immediately and this thought experiment is pointless), every floor you go up will add wind resistance to the egg causing it to take longer to drop until you hit a floor where the egg had enough time to reach terminal velocity. After that point, the time the egg needs to hit the ground will increase at a constant rate after the terminal velocity floor is reached.

Probably overthinking it but just in case haha.
