from filenames import *
from preprocess import *
from prof_training_service import *
from course_training_service import *

preprocess('COMS')
prof_train(depart,mnprof)
course_train(depart,mncourse)