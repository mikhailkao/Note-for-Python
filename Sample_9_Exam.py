grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
	for i in grades_input:
		return (i)

print (print_grades(grades))


def grades_sum(scores):
	result = 0
	for i in scores:
		result += i
	return result

print (grades_sum(grades))


def grades_average(grades_input):
	return ((grades_sum(grades_input)) / (float(len(grades_input))))

print (grades_average(grades))



def grades_variance(scores):
	average = grades_average(scores)
	variance = 0
	for i in scores:
		variance += (average - i) ** 2
	return (variance / (len(scores)))	 

print (grades_variance(grades))


def grades_std_deviation(variance):
	return variance ** 0.5

variance = grades_variance(grades)

print (grades_std_deviation(variance))