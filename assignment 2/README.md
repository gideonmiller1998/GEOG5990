## Planning for Drunks

These files make up the final agent-based model for assignment 2 of GEOG5990 module. The model successfully simulates drunks leaving a pub as the centre of the map and walking around, taking steps in random directions, until they reach their home. The default number of steps taken at each iteration is 5 to decrease time taken to run the model.

The data needed to run the model is:
1. drunk.txt (the environment data)
2. drunk_framework.py (the class code)
3. drunks.py (the main model code)

The `drunk_framework.py` file must be run first followed by `drunks.py`. This will begin the model and it will run until all 25 drunks have returned to their home. A new file called `drunk_density.txt` will also be created and shown following the completion of the model. This file shows how many times each cell has been walked over by the drunks.
