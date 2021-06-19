from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route("/")
def main():
    output = render_template("index.html")
    return output


@app.route("/departures/<departure>/")
def departures(departure):
    output = render_template("departure.html")
    return output


@app.route("/tours/<id>/")
def tours(id):
    output = render_template("tour.html")
    return output


@app.route("/data/")
def data_all():
    output = "<h1>Все туры:</h1>"
    for id, tour in data.tours.items():
        info = f"{tour['title']} {tour['price']} {tour['stars']}*"
        output += f"<p>{tour['country']}: <a href='/data/tours/{id}/'>{info}</a></p>"
    return output


@app.route("/data/departures/<departure>")
def data_departure(departure):
    departure_name = data.departures[departure]
    departure_name = departure_name[0].lower() + departure_name[1:]
    output = f"<h1>Туры {departure_name}:</h1>"
    for id, tour in data.tours.items():
        if tour['departure'] != departure:
            continue
        info = f"{tour['title']} {tour['price']} {tour['stars']}*"
        output += f"{tour['country']}: <a href='/data/tours/{id}/'>{info}</a> "
    return output


@app.route("/data/tours/<int:id>/")
def data_tour(id):
    tour = data.tours[id]
    output = f"<h1>{tour['country']}: {tour['title']} {tour['price']}:</h1>"
    output += f"<p>{tour['nights']} ночей</p>"
    output += f"<p> Стоимость: {tour['price']} Р</p>"
    output += f"<p>{tour['description']}</p>"
    return output


app.run('0.0.0.0', 8000, debug=True)
