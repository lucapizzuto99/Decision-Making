# Decision-Making
Python-based tool to help the user in different decision making situations.

The idea of this project is to create a reliable Decision Making tool, to be used for personal decisions, so not
directly related to your work. The situations can range from deciding what to do during the weekend and deciding
in which direction you want your career to evolve.

The tool is implemented in Python, and is entirely interactive, meaning that it asks questions to the user and creates
files accordingly to its answers. The rationale behind this is being able to simulate as much as possible an inner
discussion, but from an external POV; when we are within a situation, we are emotionally involved, so is difficult to
make logical decisions. By taking the user's through a self discussion, the tool will guide his/her decisions.

Being a decision making tool, there are trade off factors, which are defined in a config script.
In order to be unbiased, these factors are already pre-written before the usage of the tool, and they are to be
intended as the values of the user related to a specific situation.
For example, if the situation is a low importance one (what do I do during the weekend?) the factors might look something
similar to Possibility of having fun, People Involved, Location, Duration, Interference with Other Plans ecc.
If we are dealing with a job decision, they might be Work Place, Payment, Interest in the day to day Tasks,
Perspective of Career and so on.
The weights are attributed by the user, but not during the usage, they are set in the config file.
However, since we can all change idea, before starting the script presents the current list of factors with their
weights, and asks the user if it is okay. If so, then we start, otherwise the user can go and modify the config.

The output will be a table with the factors scores assigned to each option and the final score.

Situations implemented so far:
-) Job/career: you need to evaluate the options at your disposal.
-) Applications to job: you need to evaluate the different open positions.
-) Easy and low impact life decisions: you need to decide what to do during weekend or similar stuff.

There is a total number of points that can be distributed to each factor, which is equal to the number of factors
multiplied by 6. Every factor can get a minimum of 1 and a max of 10.
For example, if there are 10 factors, there are 60 points to be distributed between the factors.
The user can choose to use absolute rating or relative rating.

What would be the point of using this tool instead of taking pen and paper?
-) Time measurement.
-) External POV.
-) Ordinate graphical output and reasoning process. When you are alone with your thoughts they are mostly
   disorganized and chaotic. Here you have structure.

Additional possible features:
-) Time measurements. Sometime the user can be really sure about a score, sometimes it can take a while. So the script
   registers these times and, near the end, tells the user which factor was more difficult to score, which can be a sign
   that further thinking must be done.
