from flask import request, render_template, redirect, url_for, flash, g
from flask_login import current_user, login_required, login_user, logout_user
from mhealth.app import DB
from mhealth.dishes.models import Dish
from mhealth.users.models import User
import numpy as np
from sklearn import svm
import random
from matplotlib import style
import pickle
from mhealth.dishes.helpers import append_y, append_X, skip, clf_fit, eval_dish_ids, y, X, prev_dish, clf
from mhealth.users.helpers import check_password, hash_pwd
import requests
import urllib,json

NUM_OF_RECIPES = 10955
HTML_FILEPATH = "https://raw.githubusercontent.com/theCreedo/bbc-food-recipe-pages/master/BBC_Food_Repo/"

style.use("ggplot")

def landing():
	return render_template("static_pages/index.html", current_user=current_user)

def login():
	if request.method == 'GET':
		return render_template("users/login.html", current_user=current_user)

	email = request.form['email']
	password = request.form['password']
	user = User.query.filter_by(email=request.form['email']).first()

	if user is None or not check_password(user.password, password):
		print('Login Failed')
		print(user is None)
		flash("Invalid email/password. Please try again.", "warning")
		return redirect(url_for('login', current_user=current_user))
	g.log.info('Successfully logged in')
	login_user(user, remember=True)
	return redirect(url_for('landing', current_user=current_user))

def register():
	if request.method == 'GET':
		return render_template("users/register.html")
	tempUser = User.query.filter_by(email=request.form['email']).first()
	if not tempUser is None and tempUser.username == request.form['username']:
		print('user not valid')
		print(tempUser is None)
		flash('The account already exists, please try a different email', 'error')
		return redirect(url_for('register', current_user=current_user))
	print('user valid')
	user_info = {
		'is_auth': 1,
		'is_fitted': 0,
		'username': request.form['username'],
		'email': request.form['email'],
		'fname': request.form['fname'],
		'lname': request.form['lname'],
		'password': request.form['password'],
		'num_of_dishes': 0,
		'num_of_pos_dishes': 0,
		'num_of_neg_dishes': 0,
		'num_of_pos_recipes': 0,
		'num_of_neg_recipes': 0
	}
	g.log.info('Creating a user')
	g.log = g.log.bind(email=user_info['email'])
	g.log.info('Creating a new user from local information')
	user = User(user_info)
	DB.session.add(user)
	DB.session.commit()
	g.log.info('Successfully created user')
	current_user = user
	login_user(user, remember=True)
	return redirect(url_for('landing', current_user=current_user))

def error404():
	return render_template("static_pages/404.html", current_user=current_user)

def error500():
	return render_template("static_pages/error.html", current_user=current_user)

@login_required
def logout():
    logout_user()
    return redirect(url_for('landing'))

@login_required
def profile():
	if not current_user.prev_dish is None:
		return render_template("users/profile.html", dish=pickle.loads(current_user.prev_dish), current_user=current_user)
	else:
		return render_template("users/profile.html", dish=None, current_user=current_user)

@login_required
def learn():
	global current_user
	if not current_user.is_auth:
		return redirect(url_for('landing', current_user=current_user))
	if request.method == 'GET':
		dish_found = False
		while not dish_found:
			dish_id = random.randint(1,NUM_OF_RECIPES)
			if eval_dish_ids(current_user, dish_id) is None:
				current_user.eval_dish_ids = pickle.dumps(list(dish_id))
			dish = Dish.query.filter_by(id=dish_id).first()
			if not dish.id in eval_dish_ids(current_user, dish_id):
				dish_found = True
				dish.dish_url = HTML_FILEPATH + dish.dish_url
				current_user.prev_dish = pickle.dumps(dish)
		update_user(current_user)
		return render_template("dishes/learn.html", dish=dish, current_user=current_user)
# what button did user press
	if request.form["button"] == 's':
		skip(current_user)
	else:
		current_user.num_of_dishes+=1
		if request.form["button"] == 'd':
			current_user.num_of_neg_dishes+=1
			append_y(current_user, 0)
			append_X(current_user)
		elif request.form["button"] == 'l':
			current_user.num_of_pos_dishes+=1
			append_y(current_user, 1)
			append_X(current_user)

	# Find random recipe and present it in learn.html
	dish_found = False
	while not dish_found:
		dish_id = random.randint(1,NUM_OF_RECIPES)
		if eval_dish_ids(current_user, dish_id) is None:
			current_user = pickle.dumps(list(dish_id))
		dish = Dish.query.filter_by(id=dish_id).first()
		if not dish.id in eval_dish_ids(current_user, dish_id): 
			dish_found = True
			dish.dish_url = HTML_FILEPATH + dish.dish_url
			current_user.prev_dish = pickle.dumps(dish)
	update_user(current_user)
	return redirect(url_for('learn', dish=dish, current_user=current_user))

@login_required
def brew():
	global current_user
	if not current_user.is_auth:
		return redirect(url_for('landing', current_user=current_user))
	clf_value = svm.SVC(kernel='linear', C = 1.0)
	current_user.clf = pickle.dumps(clf_value)
	clf_fit(current_user)
	if request.method == 'GET':
		dish_found = False
		while not dish_found:
			dish_id = random.randint(1,NUM_OF_RECIPES)
			if eval_dish_ids(current_user, dish_id) is None:
				current_user.eval_dish_ids = pickle.dumps(list(dish_id))
			dish = Dish.query.filter_by(id=dish_id).first()
			if not dish.id in eval_dish_ids(current_user, dish_id) and pickle.loads(current_user.clf).predict([pickle.loads(dish.dish_bitmap)]): 
				dish_found = True
				dish.dish_url = HTML_FILEPATH + dish.dish_url
				current_user.prev_dish = pickle.dumps(dish)
		update_user(current_user)
		return render_template("dishes/brew.html", dish=dish, current_user=current_user)
	# what button did user press
	if request.form["button"] == 's':
		skip(current_user)
	else:
		current_user.num_of_dishes+=1
		if request.form["button"] == 'd':
			current_user.num_of_neg_dishes+=1
			current_user.num_of_neg_recipes+=1
			append_y(current_user, 0)
			append_X(current_user)
		elif request.form["button"] == 'l':
			current_user.num_of_pos_dishes+=1
			current_user.num_of_pos_recipes+=1
			append_y(current_user, 1)
			append_X(current_user)
	
	# Find random recipe and present it in learn.html
	dish_found = False
	while not dish_found:
		dish_id = random.randint(1,NUM_OF_RECIPES)
		if eval_dish_ids(current_user, dish_id) is None:
			current_user = pickle.dumps(list(dish_id))
		dish = Dish.query.filter_by(id=dish_id).first()
		if not dish.id in eval_dish_ids(current_user, dish_id) and pickle.loads(current_user.clf).predict([np.array(pickle.loads(dish.dish_bitmap))]):
			dish_found = True
			dish.dish_url = HTML_FILEPATH + dish.dish_url
			current_user.prev_dish = pickle.dumps(dish)
	update_user(current_user)
	return render_template("dishes/brew.html", dish=dish, current_user=current_user)


@login_required
def update_user(user):
	DB.session.add(user)
	DB.session.commit()



