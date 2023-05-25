# 1.Import 
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# 2. Database Setup 

engine=create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model

Base=automap_base()

#reflect the tables 

Base.prepare(autoload_with=engine)

#Save reference to the table 

Station=Base.classes.station
Measurement=Base.classes.measurement

#Flask Setup

app=Flask(__name__)

#Flask Routes

@app.route("/")
def Home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )
    

@app.route(f"/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session=Session(engine)

    # Create a query date and precipitation
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    recentdate = dt.datetime.strptime(recent_date, '%Y-%m-%d')
    querydate = dt.date(recentdate.year -1, recentdate.month, recentdate.day)


    prcp_query = session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date > querydate).\
    order_by((Measurement.date).asc()).all()
    
    session.close()
    
    # Create a dictionary from the row data and append to a list of all precipitation
    precipitation=[]
    for date, prcp in prcp_query:
        prcp_dict={}
        prcp_dict[date]= prcp
        precipitation.append(prcp_dict)
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session=Session(engine)
    
    #Query all stations 
    station_query = session.query(Station.station,Station.name, Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all stations
    all_stations=[]
    for station, name, latitude, longitude, elevation in station_query:
        stations_dict={}
        stations_dict["station"]= station
        stations_dict["name"]=name
        stations_dict["latitude"]=latitude
        stations_dict["longitude"]=longitude
        stations_dict["elevation"]=elevation
        all_stations.append(stations_dict)
   

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs(querydate=None):
    # Create our session (link) from Python to the DB
    session=Session(engine)

    
    # Using the most active station id
    # Query the last 12 months of temperature observation data for this station 

    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    recentdate = dt.datetime.strptime(recent_date, '%Y-%m-%d')
    querydate = dt.date(recentdate.year -1, recentdate.month, recentdate.day)
    
    last_12_months_tobs = session.query(Measurement.tobs).\
    filter(Measurement.date >= querydate).filter(Measurement.station=='USC00519281').all()
    
    session.close()
    
    #Convert to list

    tobs= list(np.ravel(last_12_months_tobs))

    return jsonify(tobs)
    
@app.route("/api/v1.0/<start>")
def start(start=None):
    
    session=Session(engine)
     
    #Calculate the start date and calculate TMIN, TAVG, and TMAX
    
    start = '2010-01-01' 
    start_date_query = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start).all()  

    session.close()
    
    # Convert list of tuples into normal list

    start_date_list= list(np.ravel(start_date_query))

    return jsonify(start_date_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start=None, end=None):
    
    session=Session(engine)
     
    #Calculate the start date and calculate TMIN, TAVG, and TMAX

    start='2010-01-01'
    end='2017-08-23'
    start_end_query = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start).filter(Measurement.date<= end).all()   

    session.close()
    
    # Convert list of tuples into normal list
    
    start_end_list= list(np.ravel(start_end_query))

    return jsonify(start_end_list)


if __name__ == '__main__':
    app.run(debug=True)







