from flask import render_template



@main.route('/')
def index():
    """
    View root page function to 
    """
    
    return render_template('index.html')