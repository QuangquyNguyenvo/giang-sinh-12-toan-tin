
# from flask import Flask, render_template, request, redirect, url_for
# app = Flask(__name__)

# # Home route
# @app.route('/')
# def home():
#     return render_template('home.html', message="Welcome to my Flask Web App!")

# # About route
# @app.route('/about')
# def about():
#     return render_template('about.html', title="About", description="This is a simple Flask application.")

# # Contact form route
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
#         # Normally, you would save this data or send an email
#         return render_template('contact.html', success=True, name=name)
#     return render_template('contact.html', success=False)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/next')
def next_page():
    return render_template('next.html')

if __name__ == '__main__':
    app.run(debug=True)
