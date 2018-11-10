import pickle
import numpy as np

def append_y(user, val):
	print('enter append_y')
	if user.y == None:
		user.y = pickle.dumps([val])
		y_array = y(user)
	else:
		y_array = y(user)
		y_array.append(val)
		user.y = pickle.dumps(y_array)
	print('y length: ',len(y_array))

def append_X(user):
	print('enter append_X')
	d = prev_dish(user)
	if user.X == None:
		user.X = pickle.dumps([pickle.loads(d.dish_bitmap)])
		X_array = X(user)
	else:
		X_array = X(user)
		X_array.append(pickle.loads(d.dish_bitmap))
		user.X = pickle.dumps(X_array)
	print('X length: ',len(X_array))

def skip(user):
	d = prev_dish(user)

	if user.eval_dish_ids == None:
		user.eval_dish_ids = pickle.dumps([d.id])
	else:
		edi_array = eval_dish_ids(user, d.id)
		edi_array.append(d.id)
		user.eval_dish_ids = pickle.dumps(edi_array)

def clf_fit(user):
	clf_function = clf(user)
	if user.X == None:
		d = prev_dish(user)
		X_array = [pickle.loads(d.dish_bitmap)]
		user.X = pickle.dumps(X_array)
	else:
		X_array = X(user)
	
	y_array = y(user)
	# for arr in X_array:
	# 	temp_arr = []
	# 	for k in arr:
	# 		temp_arr.append(np.typas)
	print(X_array[0][0])
	temp_arr = np.array(X_array)
	clf_function.fit(temp_arr.reshape(user.num_of_dishes,1206),y_array)

	user.clf = pickle.dumps(clf_function)

def eval_dish_ids(user, val):
	if user.eval_dish_ids is None:
		tempList = [val]
		user.eval_dish_ids = pickle.dumps(tempList)
	return pickle.loads(user.eval_dish_ids)

def y(user):
	return pickle.loads(user.y)

def X(user):
	return pickle.loads(user.X)

def prev_dish(user):
	return pickle.loads(user.prev_dish)

def clf(user):
	return pickle.loads(user.clf)