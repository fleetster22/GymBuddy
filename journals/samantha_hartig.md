8/10 created journal pages

8/17 Anaka reminded me to fill this out. I made the exercises endpoints. queries.exercises, routers.exercises and main.py have been updated.

8/22 Working on: create a page to show a way to select exercises with filters of type, muscle, or difficultly. These 3 items can be drop down selections with an "all" option.
Make cards on the page to show 10 exercises with: Name, type, muscle, equipment.
There needs to be an "add to workout" button so the exercises can be added to a specific workout.
The workout with the names of exercises and the order they are in should also be shown on the side.
The Workouts will be stored in a database tied to the user that created the workout.
Maybe later add ability to drag and drop to change the order. Would require { useDrag } from 'react-dnd'

8/24 The first drop down is to select the filter type (hooks state 2). The second drop down (hooks state 3) populates a list based on the specific filter selected. These are used (hooks state 5) to get to the exercises router. Clicking search will pull in the list of 10 exercises. Clicking “add to workout” adds the workout to (hooks state 4) the exercise list which I will work on getting into the database tomorrow. The “add to workout” button also (line 113 in CreateWorkout.js) adds green “Added to workout” text by (line 112) seeing if the workout is included in the exercise list, if it is not (line 114) does nothing.
The workout at the bottom of the page allows the user to see the workout as it is being built. This should move to the side of the page so it is always visible.

8/25 Phil said to make the create a workout page function we'd need to change some things in the migrations 003 create exercises and in the workouts query. He offered to come walk us through it on Monday because others on the team might be using parts of the things that need to change.
The 003_create_exercise table needs contain the same information as the exercise query. This will involve adding the information, dropping, and remigrating the table. We should have this set up before Phil comes to help because it is just set up.
In the workouts router - line 22-26 will be removed. Where did the matching_exercises come from?
In queries- the exercise query file needs to be filled out with at least post an exercise.
In workouts routers- we need to create a list that is equal to what is inside the list of workouts that was posted. Create a variable ExerciseList = workouts.exercises.
For loop over the list to make a new list for just the names of exercises. Put that list back into the workouts.exercises (so you have a list of names without the rest of the data)
For loop over the ExerciseList and post each into exercise database.
The info from the two for loops (id and name) will be used in the new_workout.
