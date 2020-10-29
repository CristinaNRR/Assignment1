#Assignment1

The aim of this project is to implement an architecture that simulates the behavior of a pet interacting with a human. The robot has 3 different possible behaviours(sleep, play, normal); the architecture should handle these behaviors and their transitions according to some specification.

Inside the package "beginner_tutorials" we can find the Architecture's and state machine's diagrams.
The architecture is composed by 4 nodes: Perception, behaviour, motion and control. The state machine instead is composed by 3 states and their possible transitions.
The node perception is used to simulate the interaction with a human. Every tot ms it sends a gesture position to the node behaviour, meaning that whenever is possible, the robot should enter in the 'play' state. This transition is possible only when the robot is in the normal state. When it enters the play state the program sends to the node motion the person location(fixed value), the last gesture position received, and  the person location again . When the robot exit the play state it will return to the normal behaviour. 
In the normal behaviour the program just generates 3 random positions that are sent to the motion node. After that the robot can go to each of the 3 states(random choice). 
In the sleep state, the program just send the home position to the block motion(fixed value) and then the robot returns to the normal behaviour.
The node motion, everytime that receives a target position, send a 0 position to the node control(should be a waypoint). 
The node control, when it receives the 0 position, just wait some time and notifies the node motion that the desired position has been reached.
The type of messages the node exchange are array of integers(in case of positions)or strings.

All the source code and tha diagrams are contained inside the package beginner_turorials and the nodes inside the folder script.
When we run the nodes, we can see the interaction between them reading from the terminals. In particular in the node behaviour both the robot state and the sequence of robot positions are displayed.

During the code developing I made some assumption and simplifications. 
I considered the robot moving in a 2D environment of dimention 10x10 and I also simplified something about the robot motion. 
As I said before, in the play state the program send the node motion only 3 position; in the normal state, only 3 random position are generated. As last simplification, I also assumed that when the node Perception generates a gesture position, the play state must be activated. Improving these simplifications shouldn't create any problem except for the last one. In fact, if we want the robot to reach different gesture positions all in the same play state, the code should be changed in a way that might not be straightforward.
Another limitation is the node motion that sends a 'waypoint' anytime it receives a target position. This is a problem because the node control will not be able to process a continous stream of data, therefore it will certainly miss some of them. The solution would be to make the node motion waiting and send the next waypoint only when it receives the message from the node control.
One improvement could also be to use the parameter server to store some data, like the home and person position. However it now was not necessary for this version of the code, since it access them only from 1 class.


Author:Cristina Naso Rappis
email: cri.tennis97@gmail.com
