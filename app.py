#new name site
import os
from NamingApp.forms import  AddForm
from NamingApp.models import N2
from NamingApp import db
from flask import Flask, render_template, url_for, redirect
from os import path
from wordcloud import WordCloud
import arabic_reshaper
from bidi.algorithm import get_display
from NamingApp import app

################################
@app.route('/',methods=['POST','GET'])
def index():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        new_Name = N2(name)
        db.session.add(new_Name)
        db.session.commit()

        return redirect(url_for('list'))

    return render_template('home.html', form = form)


@app.route('/list')
def list():

    NList=N2.query.limit(5).all()
    text = arabic_reshaper.reshape(str(N2.query.all()))
    text = get_display(text)
    # Generate a word cloud image
    wordcloud = WordCloud(background_color='White',font_path="NamingApp/static/arial.ttf").generate(text)
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")


    wordcloud.to_file('NamingApp/static/testing.jpg')

    return render_template('list.html', NList=NList)

###########################################################################
if __name__ == '__main__':
    app.run(debug=True)
