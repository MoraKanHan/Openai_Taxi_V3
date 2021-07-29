# Openai_Taxi_V3
Solving  The Taxi Problem     from "Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition"     by Tom Dietterich
</br>
<h1> Description:</h1>
    There are four designated locations in the grid world indicated by R(ed), G(reen), Y(ellow), and B(lue). When the episode starts, the taxi starts off at a random square and the passenger is at a random location. The taxi drives to the passenger's location, picks up the passenger, drives to the passenger's destination (another one of the four specified locations), and then drops off the passenger. Once the passenger is dropped off, the episode ends.
</br>
</br>
<h1> Observations:</h1>
    There are 500 discrete states since there are 25 taxi positions, 5 possible locations of the passenger (including the case when the passenger is in the taxi), and 4 destination locations.
</br>
<h1> Passenger locations:</h1>
<ul> <li> 0: R(ed)
    <li> 1: G(reen)
    <li> 2: Y(ellow)
    <li> 3: B(lue)
    <li> 4: in taxi
    </ul>
</br>
<h1> Destinations:</h1>
 <ul> <li> 0: R(ed)
    <li> 1: G(reen)
    <li> 2: Y(ellow)
    <li> 3: B(lue)
 </ul>
</br>
<h1> Actions: </h1>There are 6 discrete deterministic actions:
 <ul> <li> 0: move south
    <li> 1: move north
    <li> 2: move east
    <li> 3: move west
    <li> 4: pickup passenger
    <li> 5: drop off passenger
     </ul>
</br>
<h1> Rewards:</h1>
<ul> <li> There is a default per-step reward of -1,
    <li> except for delivering the passenger, which is +20,
    <li> or executing "pickup" and "drop-off" actions illegally, which is -10.
    </ul>
   
