from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
import pymongo
import sys
import json

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://Aline1:aline1@ds061355.mlab.com:61355/heroku_njkl5bj0'
mongo = PyMongo(app)

@app.route("/", methods=['GET'])
def get_time():
    time = mongo.db.time_record
    output = []
    for t in time.find() :
        output.append({'absolute_humidity_2m:gm3': t['absolute_humidity_2m:gm3'], 'clear_sky_rad:W': t['clear_sky_rad:W'],
       'dew_point_2m:C': t['dew_point_2m:C'], 'diffuse_rad:W': t['diffuse_rad:W'], 'diffuse_rad:W': t['diffuse_rad:W'],
        'diffuse_rad_1h:Ws': t['diffuse_rad_1h:Ws'], 'direct_rad:W': t['direct_rad:W'], 'direct_rad_1h:Ws': t['direct_rad_1h:Ws'],
        'dust_0p03um_0p55um:ugm3': t['dust_0p03um_0p55um:ugm3'], 'dust_0p55um_0p9um:ugm3': t['dust_0p55um_0p9um:ugm3'],
        'dust_0p9um_20um:ugm3': t['dust_0p9um_20um:ugm3'], 'effective_cloud_cover:p': t['effective_cloud_cover:p'], 
        'fresh_snow_1h:cm': t['fresh_snow_1h:cm'], 'frost_depth:cm': t['frost_depth:cm'], 'global_rad:W': t['global_rad:W'], 
        'global_rad_1h:Ws': t['global_rad_1h:Ws'],'high_cloud_cover:p': t['high_cloud_cover:p'], 'is_fog_1h:idx': t['is_fog_1h:idx'],
        'is_rain_1h:idx': t['is_rain_1h:idx'], 'is_sleet_1h:idx': t['is_sleet_1h:idx'],
        'is_snow_1h:idx': t['is_snow_1h:idx'],'low_cloud_cover:p': t['low_cloud_cover:p'], 'medium_cloud_cover:p': t['medium_cloud_cover:p'],
        'neff:p': t['neff:p'], 'pm1:ugm3': t['pm1:ugm3'], 'pm2p5:ugm3': t['pm2p5:ugm3'], 'precip_1h:mm': t['precip_1h:mm'],
        'prob_precip_1h:p': t['prob_precip_1h:p'], 'relative_humidity_2m:p': t['relative_humidity_2m:p'], 'sfc_pressure_mean_1h:hPa': t['sfc_pressure_mean_1h:hPa'],
        'snowdepth:cm': t['snowdepth:cm'],'snow_melt_1h:mm': t['snow_melt_1h:mm'],'sunrise:sql': t['sunrise:sql'],
        'sunset:sql': t['sunset:sql'],'sunshine_duration_1h:min': t['sunshine_duration_1h:min'],'t_0m:C': t['t_0m:C'],
        't_2m:C': t['t_2m:C'],'t_max_0m_1h:C': t['t_max_0m_1h:C'],'t_mean_0m_1h:C': t['t_mean_0m_1h:C'], 
        't_min_0m_1h:C': t['t_min_0m_1h:C'],'total_cloud_cover:p': t['total_cloud_cover:p'],'wet_bulb_t_2m:C': t['wet_bulb_t_2m:C'],
        'wind_dir_10m:d': t['wind_dir_10m:d'],'wind_dir_mean_10m_1h:d': t['wind_dir_mean_10m_1h:d'],'wind_gusts_10m:ms': t['wind_gusts_10m:ms'],
        'wind_speed_10m:ms': t['wind_speed_10m:ms'],'wind_speed_mean_10m_1h:ms': t['wind_speed_mean_10m_1h:ms'],
        'wind_speed_u_10m:ms': t['wind_speed_u_10m:ms'], 'wind_speed_v_10m:ms': t['wind_speed_v_10m:ms']})
    return jsonify ({'result': output})

if __name__ == "__main__":
    app.run(debug=True)