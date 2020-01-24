# Imports
from flask import (Flask, render_template)
# import cd_sd_hd_county_counts 
# from cd_sd_hd_county_counts import cd_total_accounts, sd_total_accounts, hd_total_accounts, county_total_accounts, cd_total_members, sd_total_members, hd_total_members, county_total_members, cd_total_unverified, sd_total_unverified, hd_total_unverified, county_total_unverified, cd_total_nonmembers, sd_total_nonmembers, hd_total_nonmembers, county_total_nonmembers 
import pandas as pd
coded = pd.read_csv('/Users/sethjacobson/Desktop/COLOGOPCL/geocod.io exports/1.16.2020_geocodio_export.csv')
coded_df = pd.DataFrame(coded)

# Create the App

app = Flask(__name__, template_folder='/templates')

# Home route
@app.route("/")
def show_map():
     return render_template("/templates/index.html")

@app.route("/Users/sethjacobson/Desktop/COChoropleth/data/CR-admin-export_1.16.2020.csv")
def return_csv():
     return pd.read_csv('/Users/sethjacobson/Desktop/COChoropleth/data/CR-admin-export_1.16.2020.csv')

# @app.route('templates/css/style.css')
# def serve_css():
#      return send_from_directory('templates')

# @app.route('/static/style.css>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename, as_attachment=True)

# cd_routes

@app.route("/cd_1")
def get_cd1_counts():
     # Total Subscribers first
     x_district = coded_df['Congressional District'] == f'CO1'
     x_district_coded = coded_df[x_district]
     x_district_subscribers_count = coded_df[x_district].shape[0]
     # Next, do Total Members
     x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
     x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
     x_district_m_v = x_district_coded[x_district_members_verified_count]
     x_district_v_m = x_district_coded[x_district_verified_members_count]
     x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
     # Then, do Unverifieds
     x_district_unverified = x_district_coded['roles'] == 'unverified'
     x_district_unverified_member = x_district_coded['roles'] == 'unverified,member'
     x_district_member_unverified = x_district_coded['roles'] == 'member,unverified'
     x_district_unverified_nonmember = x_district_coded['roles'] == 'unverified,nonmember'
     xd_uv = x_district_coded[x_district_unverified]
     xd_uv_m = x_district_coded[x_district_unverified_member]
     xd_m_uv = x_district_coded[x_district_member_unverified]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmember]
     xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
     # Last, do Nonmembers
     x_district_nonmembers_verified = x_district_coded['roles'] == 'nonmember,verified'
     x_district_verified_nonmembers = x_district_coded['roles'] == 'verified,nonmember'
     x_district_unverified_nonmembers = x_district_coded['roles'] == 'unverified,nonmember'
     x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
     xd_nm_v = x_district_coded[x_district_nonmembers_verified]
     xd_v_nm = x_district_coded[x_district_verified_nonmembers]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
     xd_nm = x_district_coded[x_district_nonmembers]
     xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[0] + xd_nm.shape[0]
     json_object = {}
     keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_total_unverifieds', 'xd_nm_total']
     list_totals = [x_district_subscribers_count, x_district_total_members, xd_total_unverifieds, xd_nm_total]
     for key in keys: 
          for value in list_totals: 
               json_object[key] = value 
               list_totals.remove(value) 
               break
     df = pd.DataFrame([json_object])
     return df.to_json(orient='records')



@app.route("/cd_2")
def get_cd2_counts():
     # Total Subscribers first
     x_district = coded_df['Congressional District'] == f'CO2'
     x_district_coded = coded_df[x_district]
     x_district_subscribers_count = coded_df[x_district].shape[0]
     # Next, do Total Members
     x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
     x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
     x_district_m_v = x_district_coded[x_district_members_verified_count]
     x_district_v_m = x_district_coded[x_district_verified_members_count]
     x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
     # Then, do Unverifieds
     x_district_unverified = x_district_coded['roles'] == 'unverified'
     x_district_unverified_member = x_district_coded['roles'] == 'unverified,member'
     x_district_member_unverified = x_district_coded['roles'] == 'member,unverified'
     x_district_unverified_nonmember = x_district_coded['roles'] == 'unverified,nonmember'
     xd_uv = x_district_coded[x_district_unverified]
     xd_uv_m = x_district_coded[x_district_unverified_member]
     xd_m_uv = x_district_coded[x_district_member_unverified]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmember]
     xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
     # Last, do Nonmembers
     x_district_nonmembers_verified = x_district_coded['roles'] == 'nonmember,verified'
     x_district_verified_nonmembers = x_district_coded['roles'] == 'verified,nonmember'
     x_district_unverified_nonmembers = x_district_coded['roles'] == 'unverified,nonmember'
     x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
     xd_nm_v = x_district_coded[x_district_nonmembers_verified]
     xd_v_nm = x_district_coded[x_district_verified_nonmembers]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
     xd_nm = x_district_coded[x_district_nonmembers]
     xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[0] + xd_nm.shape[0]
     json_object = {}
     keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_total_unverifieds', 'xd_nm_total']
     list_totals = [x_district_subscribers_count, x_district_total_members, xd_total_unverifieds, xd_nm_total]
     for key in keys: 
          for value in list_totals: 
               json_object[key] = value 
               list_totals.remove(value) 
               break
     df = pd.DataFrame([json_object])
     return df.to_json(orient='records')



@app.route("/cd_3")
def get_cd3_counts():
     # Total Subscribers first
     x_district = coded_df['Congressional District'] == f'CO3'
     x_district_coded = coded_df[x_district]
     x_district_subscribers_count = coded_df[x_district].shape[0]
     # Next, do Total Members
     x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
     x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
     x_district_m_v = x_district_coded[x_district_members_verified_count]
     x_district_v_m = x_district_coded[x_district_verified_members_count]
     x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
     # Then, do Unverifieds
     x_district_unverified = x_district_coded['roles'] == 'unverified'
     x_district_unverified_member = x_district_coded['roles'] == 'unverified,member'
     x_district_member_unverified = x_district_coded['roles'] == 'member,unverified'
     x_district_unverified_nonmember = x_district_coded['roles'] == 'unverified,nonmember'
     xd_uv = x_district_coded[x_district_unverified]
     xd_uv_m = x_district_coded[x_district_unverified_member]
     xd_m_uv = x_district_coded[x_district_member_unverified]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmember]
     xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
     # Last, do Nonmembers
     x_district_nonmembers_verified = x_district_coded['roles'] == 'nonmember,verified'
     x_district_verified_nonmembers = x_district_coded['roles'] == 'verified,nonmember'
     x_district_unverified_nonmembers = x_district_coded['roles'] == 'unverified,nonmember'
     x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
     xd_nm_v = x_district_coded[x_district_nonmembers_verified]
     xd_v_nm = x_district_coded[x_district_verified_nonmembers]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
     xd_nm = x_district_coded[x_district_nonmembers]
     xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[0] + xd_nm.shape[0]
     json_object = {}
     keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_total_unverifieds', 'xd_nm_total']
     list_totals = [x_district_subscribers_count, x_district_total_members, xd_total_unverifieds, xd_nm_total]
     for key in keys: 
          for value in list_totals: 
               json_object[key] = value 
               list_totals.remove(value) 
               break
     df = pd.DataFrame([json_object])
     return df.to_json(orient='records')



@app.route("/cd_4")
def get_cd4_counts():
     # Total Subscribers first
     x_district = coded_df['Congressional District'] == f'CO4'
     x_district_coded = coded_df[x_district]
     x_district_subscribers_count = coded_df[x_district].shape[0]
     # Next, do Total Members
     x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
     x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
     x_district_m_v = x_district_coded[x_district_members_verified_count]
     x_district_v_m = x_district_coded[x_district_verified_members_count]
     x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
     # Then, do Unverifieds
     x_district_unverified = x_district_coded['roles'] == 'unverified'
     x_district_unverified_member = x_district_coded['roles'] == 'unverified,member'
     x_district_member_unverified = x_district_coded['roles'] == 'member,unverified'
     x_district_unverified_nonmember = x_district_coded['roles'] == 'unverified,nonmember'
     xd_uv = x_district_coded[x_district_unverified]
     xd_uv_m = x_district_coded[x_district_unverified_member]
     xd_m_uv = x_district_coded[x_district_member_unverified]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmember]
     xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
     # Last, do Nonmembers
     x_district_nonmembers_verified = x_district_coded['roles'] == 'nonmember,verified'
     x_district_verified_nonmembers = x_district_coded['roles'] == 'verified,nonmember'
     x_district_unverified_nonmembers = x_district_coded['roles'] == 'unverified,nonmember'
     x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
     xd_nm_v = x_district_coded[x_district_nonmembers_verified]
     xd_v_nm = x_district_coded[x_district_verified_nonmembers]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
     xd_nm = x_district_coded[x_district_nonmembers]
     xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[0] + xd_nm.shape[0]
     json_object = {}
     keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_total_unverifieds', 'xd_nm_total']
     list_totals = [x_district_subscribers_count, x_district_total_members, xd_total_unverifieds, xd_nm_total]
     for key in keys: 
          for value in list_totals: 
               json_object[key] = value 
               list_totals.remove(value) 
               break
     df = pd.DataFrame([json_object])
     return df.to_json(orient='records')



@app.route("/cd_5")
def get_cd5_counts():
     # Total Subscribers first
     x_district = coded_df['Congressional District'] == f'CO5'
     x_district_coded = coded_df[x_district]
     x_district_subscribers_count = coded_df[x_district].shape[0]
     # Next, do Total Members
     x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
     x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
     x_district_m_v = x_district_coded[x_district_members_verified_count]
     x_district_v_m = x_district_coded[x_district_verified_members_count]
     x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
     # Then, do Unverifieds
     x_district_unverified = x_district_coded['roles'] == 'unverified'
     x_district_unverified_member = x_district_coded['roles'] == 'unverified,member'
     x_district_member_unverified = x_district_coded['roles'] == 'member,unverified'
     x_district_unverified_nonmember = x_district_coded['roles'] == 'unverified,nonmember'
     xd_uv = x_district_coded[x_district_unverified]
     xd_uv_m = x_district_coded[x_district_unverified_member]
     xd_m_uv = x_district_coded[x_district_member_unverified]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmember]
     xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
     # Last, do Nonmembers
     x_district_nonmembers_verified = x_district_coded['roles'] == 'nonmember,verified'
     x_district_verified_nonmembers = x_district_coded['roles'] == 'verified,nonmember'
     x_district_unverified_nonmembers = x_district_coded['roles'] == 'unverified,nonmember'
     x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
     xd_nm_v = x_district_coded[x_district_nonmembers_verified]
     xd_v_nm = x_district_coded[x_district_verified_nonmembers]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
     xd_nm = x_district_coded[x_district_nonmembers]
     xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[0] + xd_nm.shape[0]
     json_object = {}
     keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_total_unverifieds', 'xd_nm_total']
     list_totals = [x_district_subscribers_count, x_district_total_members, xd_total_unverifieds, xd_nm_total]
     for key in keys: 
          for value in list_totals: 
               json_object[key] = value 
               list_totals.remove(value) 
               break
     df = pd.DataFrame([json_object])
     return df.to_json(orient='records')



@app.route("/cd_6")
def get_cd6_counts():
     # Total Subscribers first
     x_district = coded_df['Congressional District'] == f'CO6'
     x_district_coded = coded_df[x_district]
     x_district_subscribers_count = coded_df[x_district].shape[0]
     # Next, do Total Members
     x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
     x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
     x_district_m_v = x_district_coded[x_district_members_verified_count]
     x_district_v_m = x_district_coded[x_district_verified_members_count]
     x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
     # Then, do Unverifieds
     x_district_unverified = x_district_coded['roles'] == 'unverified'
     x_district_unverified_member = x_district_coded['roles'] == 'unverified,member'
     x_district_member_unverified = x_district_coded['roles'] == 'member,unverified'
     x_district_unverified_nonmember = x_district_coded['roles'] == 'unverified,nonmember'
     xd_uv = x_district_coded[x_district_unverified]
     xd_uv_m = x_district_coded[x_district_unverified_member]
     xd_m_uv = x_district_coded[x_district_member_unverified]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmember]
     xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
     # Last, do Nonmembers
     x_district_nonmembers_verified = x_district_coded['roles'] == 'nonmember,verified'
     x_district_verified_nonmembers = x_district_coded['roles'] == 'verified,nonmember'
     x_district_unverified_nonmembers = x_district_coded['roles'] == 'unverified,nonmember'
     x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
     xd_nm_v = x_district_coded[x_district_nonmembers_verified]
     xd_v_nm = x_district_coded[x_district_verified_nonmembers]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
     xd_nm = x_district_coded[x_district_nonmembers]
     xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[0] + xd_nm.shape[0]
     json_object = {}
     keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_total_unverifieds', 'xd_nm_total']
     list_totals = [x_district_subscribers_count, x_district_total_members, xd_total_unverifieds, xd_nm_total]
     for key in keys: 
          for value in list_totals: 
               json_object[key] = value 
               list_totals.remove(value) 
               break
     df = pd.DataFrame([json_object])
     return df.to_json(orient='records')



@app.route("/cd_7")
def get_cd7_counts():
     # Total Subscribers first
     x_district = coded_df['Congressional District'] == f'CO7'
     x_district_coded = coded_df[x_district]
     x_district_subscribers_count = coded_df[x_district].shape[0]
     # Next, do Total Members
     x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
     x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
     x_district_m_v = x_district_coded[x_district_members_verified_count]
     x_district_v_m = x_district_coded[x_district_verified_members_count]
     x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
     # Then, do Unverifieds
     x_district_unverified = x_district_coded['roles'] == 'unverified'
     x_district_unverified_member = x_district_coded['roles'] == 'unverified,member'
     x_district_member_unverified = x_district_coded['roles'] == 'member,unverified'
     x_district_unverified_nonmember = x_district_coded['roles'] == 'unverified,nonmember'
     xd_uv = x_district_coded[x_district_unverified]
     xd_uv_m = x_district_coded[x_district_unverified_member]
     xd_m_uv = x_district_coded[x_district_member_unverified]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmember]
     xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
     # Last, do Nonmembers
     x_district_nonmembers_verified = x_district_coded['roles'] == 'nonmember,verified'
     x_district_verified_nonmembers = x_district_coded['roles'] == 'verified,nonmember'
     x_district_unverified_nonmembers = x_district_coded['roles'] == 'unverified,nonmember'
     x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
     xd_nm_v = x_district_coded[x_district_nonmembers_verified]
     xd_v_nm = x_district_coded[x_district_verified_nonmembers]
     xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
     xd_nm = x_district_coded[x_district_nonmembers]
     xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[0] + xd_nm.shape[0]
     json_object = {}
     keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_total_unverifieds', 'xd_nm_total']
     list_totals = [x_district_subscribers_count, x_district_total_members, xd_total_unverifieds, xd_nm_total]
     for key in keys: 
          for value in list_totals: 
               json_object[key] = value 
               list_totals.remove(value) 
               break
     df = pd.DataFrame([json_object])
     return df.to_json(orient='records')




if __name__ == "__main__":
    app.run(debug=True)