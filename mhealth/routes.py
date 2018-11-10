import mhealth.dishes

def configure_routes(app):
	    app.add_url_rule('/', 'landing', view_func=mhealth.dishes.views.landing, methods=['GET'])
	    app.add_url_rule('/learn', 'learn', view_func=mhealth.dishes.views.learn, methods=['GET', 'POST'])
	    app.add_url_rule('/brew', 'brew', view_func=mhealth.dishes.views.brew, methods=['GET', 'POST'])

	    # user urls
	    app.add_url_rule('/login', 'login', view_func=mhealth.dishes.views.login, methods=['GET', 'POST'])
	    app.add_url_rule('/register', 'register', view_func=mhealth.dishes.views.register, methods=['GET', 'POST'])
	    app.add_url_rule('/profile', 'profile', view_func=mhealth.dishes.views.profile, methods=['GET'])
	    app.add_url_rule('/logout', 'logout', view_func=mhealth.dishes.views.logout, methods=['GET'])

	    app.add_url_rule('/404.html', '404', view_func=mhealth.dishes.views.error404, methods=['GET'])
	    app.add_url_rule('/error', 'error', view_func=mhealth.dishes.views.error500, methods=['GET'])
