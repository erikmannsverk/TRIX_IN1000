from person import Person

def hovedprogram():

    mrSmith = Person("Brad Pitt")
    mrsSmith = Person("Angelina Jolie")

    mrSmith.minStatus()

    mrSmith.bryllup(mrsSmith)
    mrsSmith.bryllup(mrSmith)

    mrSmith.minStatus()
    mrsSmith.minStatus()
    
hovedprogram()
