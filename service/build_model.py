from filenames import *
from preprocess import *
from prof_training_service import *
from course_training_service import *

def build_model(depart):

	preprocess(depart)
	prof_train(depart, mnprof)
	course_train(depart, mncourse)


if __name__ == "__main__":
	make_data(depart)
