import re
import sys
import pickle
import pprint

def review_course(l_name, f_name, course):
    data = pickle.load(open("../data/culpa.p", "rb"))
    return_list = list()
    course_name = ''
    course_num = ''
    review_num = 0
    for i in range(len(data)):
        p_name = data[i][0]
        c_num = data[i][2]
        if l_name in p_name.lower() and f_name in p_name.lower() and course in c_num:
            review_num += 1
            texts = data[i][6]['sentences']
            course_name = data[i][3]
            course_num = data[i][2]
            for t in texts:
                return_list.append((abs(float(t['sentiment']['magnitude'])*float(t['sentiment']['score'])), t['text'][
                    'content']))
    sorted_list = [x[1] for x in sorted(return_list, reverse=True)]

    return sorted_list[:3], course_name, course_num, review_num


if __name__ == "__main__":
    print(rank_course('COMS w1004 w4995 w3136 '))