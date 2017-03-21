import classes

exam1 = classes.Grade('test1', 90.0, .15)


exercises = classes.Grade('In Class', 100, .05)

proj01 = classes.Grade('proj01', 100, .01)
proj02 = classes.Grade('proj02', 100, .02)
proj03 = classes.Grade('proj03', 100, .03)
proj04 = classes.Grade('proj04', 100, .04)


Camille = classes.Student(1,"Camille","Emig",[exam1, exercises, proj04,proj03,proj02,proj01])
print(Camille)
