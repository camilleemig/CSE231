import classes

mpl = classes.Grade('MPL', 100, .1)
exam1 = classes.Grade('exam1', 72, .1)
exam2 = classes.Grade('exam2', 63.33, .15)
proj01 = classes.Grade('proj01', 93.33, .015)
proj02 = classes.Grade('proj02', 90, .02)
proj03 = classes.Grade('proj03', 65, .02)
proj04 = classes.Grade('proj04', 92.5, .04)
proj05 = classes.Grade('proj05', 95.56, .045)
proj06 = classes.Grade('proj06', 100, .045)
proj07 = classes.Grade('proj07', 100, .05)
proj08 = classes.Grade('proj08', 88, .055)
proj09 = classes.Grade('proj09', 50, .055)
proj10 = classes.Grade('proj10', 80, .055)
proj11 = classes.Grade('proj11', 90, .055)
exam3 = classes.Grade('exam3', 70, .2)

#rest_of_grade = classes.Grade('rest_of_grade', 87.5, .1)


Elizabeth = classes.Student(1,"Elizabeth","Schester",[mpl, exam1,exam2,proj01, proj02,proj03,proj04,proj05,proj06,proj07,proj08,proj09,proj10, proj11, exam3])
print(Elizabeth)
