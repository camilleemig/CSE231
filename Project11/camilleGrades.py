import classes

participation = classes.Grade('Participation', 95, .2)

quiz01 = classes.Grade('quiz01', 95, .1)
quiz02 = classes.Grade('quiz02', 95, .1)
quiz03 = classes.Grade('quiz03', 100, .1)
essay01 = classes.Grade('essay01', 87.5, .1)
essay02 = classes.Grade('essay02', 81.25, .1)
essay03 = classes.Grade('essay03', 100, .1)

Camille = classes.Student(1,"Camille","Emig",[participation, quiz03,quiz02,quiz01, essay03,essay02,essay01])
print(Camille)
