from flask import render_template



@main.route('/')
def index():
    """
    View root page function to present homepage.
    """
    return render_template('index.html')

@main.route('/all_pitches')
def all_pitches():
    
    
   
    return render_template('all_pitches.html',general=general)



@main.route('/interview')
def interview():
    
    
    return render_template('interview.html',interview=interview,comment=comment)


@main.route('/promotion')
def promotion():
    
    
    return render_template('promotion.html',promotion=promotion,comment=comment)



@main.route('/product')
def product():
    
    
    return render_template('product.html',product=product,comment=comment)


@main.route('/pickup')
def pickup():
    
    
     return render_template('pickup.html', pickup=pickup,comment=comment)
 
 
 