# Imports
from flask import (Flask, render_template)
# import cd_sd_hd_county_counts
# from cd_sd_hd_county_counts import cd_total_accounts, sd_total_accounts, hd_total_accounts, county_total_accounts, cd_total_members, sd_total_members, hd_total_members, county_total_members, cd_total_unverified, sd_total_unverified, hd_total_unverified, county_total_unverified, cd_total_nonmembers, sd_total_nonmembers, hd_total_nonmembers, county_total_nonmembers
import pandas as pd
# coded = pd.read_csv('/Users/sethjacobson/Desktop/COLOGOPCL/admin_exports_by_date/CR-admin-export_1.26.2020.csv')
coded = pd.read_csv('/Users/sethjacobson/Desktop/COLOGOPCL/admin_exports_by_date/CR-admin-export_1.26.2020.csv')
    # r'C:\git\flask_app_w_leaflet_d3\static\CR-admin-export_1.22.2020.csv'
# )  #'/Users/sethjacobson/Desktop/COLOGOPCL/admin_exports_by_date/CR-admin-export_1.26.2020.csv')
coded_df = pd.DataFrame(coded)

# Create the App

app = Flask(__name__)


# Home route
@app.route("/")
def show_map():
    return render_template("index.html")


@app.route("/user_data")
def get_user_data():
    coded_export = coded_df[[
        'longitude',
        'latitude',
        'county',
        'cd',
        'sd',
        'hd',
        'roles',
    ]]
    return coded_export.to_json(orient='records')


# cd_routes


@app.route("/cd_1")
def get_cd1_counts():
    # Total Subscribers first
    x_district = coded_df['cd'] == 1
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded[
        'roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded[
        'roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0]
    # Last, do Nonmembers
    x_district_nonmembers_verified = x_district_coded[
        'roles'] == 'nonmember,verified'
    x_district_verified_nonmembers = x_district_coded[
        'roles'] == 'verified,nonmember'
    x_district_unverified_nonmembers = x_district_coded[
        'roles'] == 'unverified,nonmember'
    x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
    xd_nm_v = x_district_coded[x_district_nonmembers_verified]
    xd_v_nm = x_district_coded[x_district_verified_nonmembers]
    xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
    xd_nm = x_district_coded[x_district_nonmembers]
    xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[
        0] + xd_nm.shape[0]
    json_object = {}
    keys = [
        'x_district_subscribers_count', 'x_district_total_members',
        'xd_uv_count', 'xd_nm_total'
    ]
    list_totals = [
        x_district_subscribers_count, x_district_total_members, xd_uv_count,
        xd_nm_total
    ]
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
    x_district = coded_df['cd'] == 2
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded[
        'roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded[
        'roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0]
    # Last, do Nonmembers
    x_district_nonmembers_verified = x_district_coded[
        'roles'] == 'nonmember,verified'
    x_district_verified_nonmembers = x_district_coded[
        'roles'] == 'verified,nonmember'
    x_district_unverified_nonmembers = x_district_coded[
        'roles'] == 'unverified,nonmember'
    x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
    xd_nm_v = x_district_coded[x_district_nonmembers_verified]
    xd_v_nm = x_district_coded[x_district_verified_nonmembers]
    xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
    xd_nm = x_district_coded[x_district_nonmembers]
    xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[
        0] + xd_nm.shape[0]
    json_object = {}
    keys = [
        'x_district_subscribers_count', 'x_district_total_members',
        'xd_uv_count', 'xd_nm_total'
    ]
    list_totals = [
        x_district_subscribers_count, x_district_total_members, xd_uv_count,
        xd_nm_total
    ]
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
    x_district = coded_df['cd'] == 3
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded[
        'roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded[
        'roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0]
    # Last, do Nonmembers
    x_district_nonmembers_verified = x_district_coded[
        'roles'] == 'nonmember,verified'
    x_district_verified_nonmembers = x_district_coded[
        'roles'] == 'verified,nonmember'
    x_district_unverified_nonmembers = x_district_coded[
        'roles'] == 'unverified,nonmember'
    x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
    xd_nm_v = x_district_coded[x_district_nonmembers_verified]
    xd_v_nm = x_district_coded[x_district_verified_nonmembers]
    xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
    xd_nm = x_district_coded[x_district_nonmembers]
    xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[
        0] + xd_nm.shape[0]
    json_object = {}
    keys = [
        'x_district_subscribers_count', 'x_district_total_members',
        'xd_uv_count', 'xd_nm_total'
    ]
    list_totals = [
        x_district_subscribers_count, x_district_total_members, xd_uv_count,
        xd_nm_total
    ]
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
    x_district = coded_df['cd'] == 4
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded[
        'roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded[
        'roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0]
    # Last, do Nonmembers
    x_district_nonmembers_verified = x_district_coded[
        'roles'] == 'nonmember,verified'
    x_district_verified_nonmembers = x_district_coded[
        'roles'] == 'verified,nonmember'
    x_district_unverified_nonmembers = x_district_coded[
        'roles'] == 'unverified,nonmember'
    x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
    xd_nm_v = x_district_coded[x_district_nonmembers_verified]
    xd_v_nm = x_district_coded[x_district_verified_nonmembers]
    xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
    xd_nm = x_district_coded[x_district_nonmembers]
    xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[
        0] + xd_nm.shape[0]
    json_object = {}
    keys = [
        'x_district_subscribers_count', 'x_district_total_members',
        'xd_uv_count', 'xd_nm_total'
    ]
    list_totals = [
        x_district_subscribers_count, x_district_total_members, xd_uv_count,
        xd_nm_total
    ]
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
    x_district = coded_df['cd'] == 5
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded[
        'roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded[
        'roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0]
    # Last, do Nonmembers
    x_district_nonmembers_verified = x_district_coded[
        'roles'] == 'nonmember,verified'
    x_district_verified_nonmembers = x_district_coded[
        'roles'] == 'verified,nonmember'
    x_district_unverified_nonmembers = x_district_coded[
        'roles'] == 'unverified,nonmember'
    x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
    xd_nm_v = x_district_coded[x_district_nonmembers_verified]
    xd_v_nm = x_district_coded[x_district_verified_nonmembers]
    xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
    xd_nm = x_district_coded[x_district_nonmembers]
    xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[
        0] + xd_nm.shape[0]
    json_object = {}
    keys = [
        'x_district_subscribers_count', 'x_district_total_members',
        'xd_uv_count', 'xd_nm_total'
    ]
    list_totals = [
        x_district_subscribers_count, x_district_total_members, xd_uv_count,
        xd_nm_total
    ]
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
    x_district = coded_df['cd'] == 6
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded[
        'roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded[
        'roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0]
    # Last, do Nonmembers
    x_district_nonmembers_verified = x_district_coded[
        'roles'] == 'nonmember,verified'
    x_district_verified_nonmembers = x_district_coded[
        'roles'] == 'verified,nonmember'
    x_district_unverified_nonmembers = x_district_coded[
        'roles'] == 'unverified,nonmember'
    x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
    xd_nm_v = x_district_coded[x_district_nonmembers_verified]
    xd_v_nm = x_district_coded[x_district_verified_nonmembers]
    xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
    xd_nm = x_district_coded[x_district_nonmembers]
    xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[
        0] + xd_nm.shape[0]
    json_object = {}
    keys = [
        'x_district_subscribers_count', 'x_district_total_members',
        'xd_uv_count', 'xd_nm_total'
    ]
    list_totals = [
        x_district_subscribers_count, x_district_total_members, xd_uv_count,
        xd_nm_total
    ]
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
    x_district = coded_df['cd'] == 7
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded[
        'roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded[
        'roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0]
    # Last, do Nonmembers
    x_district_nonmembers_verified = x_district_coded[
        'roles'] == 'nonmember,verified'
    x_district_verified_nonmembers = x_district_coded[
        'roles'] == 'verified,nonmember'
    x_district_unverified_nonmembers = x_district_coded[
        'roles'] == 'unverified,nonmember'
    x_district_nonmembers = x_district_coded['roles'] == 'nonmember'
    xd_nm_v = x_district_coded[x_district_nonmembers_verified]
    xd_v_nm = x_district_coded[x_district_verified_nonmembers]
    xd_uv_nm = x_district_coded[x_district_unverified_nonmembers]
    xd_nm = x_district_coded[x_district_nonmembers]
    xd_nm_total = xd_nm_v.shape[0] + xd_v_nm.shape[0] + xd_uv_nm.shape[
        0] + xd_nm.shape[0]
    json_object = {}
    keys = [
        'x_district_subscribers_count', 'x_district_total_members',
        'xd_uv_count', 'xd_nm_total'
    ]
    list_totals = [
        x_district_subscribers_count, x_district_total_members, xd_uv_count,
        xd_nm_total
    ]
    for key in keys:
        for value in list_totals:
            json_object[key] = value
            list_totals.remove(value)
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route("/sd_1")
def get_sd1_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 1
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_2")
def get_sd2_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 2
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_3")
def get_sd3_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 3
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_4")
def get_sd4_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 4
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_5")
def get_sd5_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 5
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_6")
def get_sd6_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 6
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_7")
def get_sd7_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 7
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_8")
def get_sd8_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 8
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_9")
def get_sd9_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 9
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_10")
def get_sd10_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 10
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_11")
def get_sd11_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 11
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_12")
def get_sd12_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 12
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_13")
def get_sd13_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 13
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_14")
def get_sd14_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 14
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_15")
def get_sd15_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 15
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_16")
def get_sd16_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 16
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_17")
def get_sd17_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 17
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_18")
def get_sd18_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 18
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_19")
def get_sd19_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 19
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_20")
def get_sd20_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 20
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_21")
def get_sd21_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 21
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_22")
def get_sd22_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 22
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_23")
def get_sd23_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 23
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_24")
def get_sd24_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 24
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_25")
def get_sd25_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 25
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_26")
def get_sd26_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 26
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_27")
def get_sd27_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 27
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_28")
def get_sd28_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 28
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_29")
def get_sd29_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 29
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_30")
def get_sd30_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 30
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_31")
def get_sd31_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 31
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_32")
def get_sd32_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 32
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_33")
def get_sd33_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 33
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_34")
def get_sd34_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 34
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/sd_35")
def get_sd35_counts():
    # Total Subscribers first
    x_district = coded_df['sd'] == 35
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route("/hd_1")
def get_hd1_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 1
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_2")
def get_hd2_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 2
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_3")
def get_hd3_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 3
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_4")
def get_hd4_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 4
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_5")
def get_hd5_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 5
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_6")
def get_hd6_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 6
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_7")
def get_hd7_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 7
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_8")
def get_hd8_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 8
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_9")
def get_hd9_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 9
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_10")
def get_hd10_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 10
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_11")
def get_hd11_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 11
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_12")
def get_hd12_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 12
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_13")
def get_hd13_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 13
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_14")
def get_hd14_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 14
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_15")
def get_hd15_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 15
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_16")
def get_hd16_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 16
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_17")
def get_hd17_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 17
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_18")
def get_hd18_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 18
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_19")
def get_hd19_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 19
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_20")
def get_hd20_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 20
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_21")
def get_hd21_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 21
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_22")
def get_hd22_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 22
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_23")
def get_hd23_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 23
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_24")
def get_hd24_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 24
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_25")
def get_hd25_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 25
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_26")
def get_hd26_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 26
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_27")
def get_hd27_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 27
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_28")
def get_hd28_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 28
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_29")
def get_hd29_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 29
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_30")
def get_hd30_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 30
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_31")
def get_hd31_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 31
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_32")
def get_hd32_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 32
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_33")
def get_hd33_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 33
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_34")
def get_hd34_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 34
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_35")
def get_hd35_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 35
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_36")
def get_hd36_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 36
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_37")
def get_hd37_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 37
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_38")
def get_hd38_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 38
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_39")
def get_hd39_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 39
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_40")
def get_hd40_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 40
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_41")
def get_hd41_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 41
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_42")
def get_hd42_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 42
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_43")
def get_hd43_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 43
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_44")
def get_hd44_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 44
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_45")
def get_hd45_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 45
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_46")
def get_hd46_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 46
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_47")
def get_hd47_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 47
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_48")
def get_hd48_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 48
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_49")
def get_hd49_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 49
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_50")
def get_hd50_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 50
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_51")
def get_hd51_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 51
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_52")
def get_hd52_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 52
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_53")
def get_hd53_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 53
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_54")
def get_hd54_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 54
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_55")
def get_hd55_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 55
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_56")
def get_hd56_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 56
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_57")
def get_hd57_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 57
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_58")
def get_hd58_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 58
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_59")
def get_hd59_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 59
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_60")
def get_hd60_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 60
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_61")
def get_hd61_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 61
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_62")
def get_hd62_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 62
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_63")
def get_hd63_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 63
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')
    
    

@app.route("/hd_64")
def get_hd64_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 64
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')



@app.route("/hd_65")
def get_hd65_counts():
    # Total Subscribers first
    x_district = coded_df['hd'] == 65
    x_district_coded = coded_df[x_district]
    x_district_subscribers_count = coded_df[x_district].shape[0]
    # Next, do Total Members
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
    # Then, do Unverifieds
    x_district_unverified = x_district_coded['verified'] == 'False'
    xd_uv_count = x_district_coded[x_district_unverified].shape[0]
    # xd_total_unverifieds = xd_uv.shape[0] + xd_uv_m.shape[0] + xd_m_uv.shape[0] + xd_uv_nm.shape[0] 
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_uv_count', 'xd_nm_total']
    list_totals = [x_district_subscribers_count, x_district_total_members, xd_uv_count, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/BOULDER')
def BOULDER_total_counts():
    x_district = coded_df['county'] == f'BOULDER'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/JEFFERSON')
def JEFFERSON_total_counts():
    x_district = coded_df['county'] == f'JEFFERSON'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/ADAMS')
def ADAMS_total_counts():
    x_district = coded_df['county'] == f'ADAMS'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/DENVER')
def DENVER_total_counts():
    x_district = coded_df['county'] == f'DENVER'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/ARAPAHOE')
def ARAPAHOE_total_counts():
    x_district = coded_df['county'] == f'ARAPAHOE'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/DOUGLAS')
def DOUGLAS_total_counts():
    x_district = coded_df['county'] == f'DOUGLAS'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/PUEBLO')
def PUEBLO_total_counts():
    x_district = coded_df['county'] == f'PUEBLO'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/EL_PASO')
def EL_PASO_total_counts():
    x_district = coded_df['county'] == f'EL PASO'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/WELD')
def WELD_total_counts():
    x_district = coded_df['county'] == f'WELD'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/KIT_CARSON')
def KIT_CARSON_total_counts():
    x_district = coded_df['county'] == f'KIT CARSON'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/ELBERT')
def ELBERT_total_counts():
    x_district = coded_df['county'] == f'ELBERT'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/BROOMFIELD')
def BROOMFIELD_total_counts():
    x_district = coded_df['county'] == f'BROOMFIELD'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/ROUTT')
def ROUTT_total_counts():
    x_district = coded_df['county'] == f'ROUTT'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/YUMA')
def YUMA_total_counts():
    x_district = coded_df['county'] == f'YUMA'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/MESA')
def MESA_total_counts():
    x_district = coded_df['county'] == f'MESA'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/MONTEZUMA')
def MONTEZUMA_total_counts():
    x_district = coded_df['county'] == f'MONTEZUMA'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/LARIMER')
def LARIMER_total_counts():
    x_district = coded_df['county'] == f'LARIMER'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/CLEAR_CREEK')
def CLEAR_CREEK_total_counts():
    x_district = coded_df['county'] == f'CLEAR CREEK'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/LA_PLATA')
def LA_PLATA_total_counts():
    x_district = coded_df['county'] == f'LA PLATA'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/TELLER')
def TELLER_total_counts():
    x_district = coded_df['county'] == f'TELLER'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/FREMONT')
def FREMONT_total_counts():
    x_district = coded_df['county'] == f'FREMONT'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/SUMMIT')
def SUMMIT_total_counts():
    x_district = coded_df['county'] == f'SUMMIT'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/RIO_BLANCO')
def RIO_BLANCO_total_counts():
    x_district = coded_df['county'] == f'RIO BLANCO'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/CUSTER')
def CUSTER_total_counts():
    x_district = coded_df['county'] == f'CUSTER'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/HUERFANO')
def HUERFANO_total_counts():
    x_district = coded_df['county'] == f'HUERFANO'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/DELTA')
def DELTA_total_counts():
    x_district = coded_df['county'] == f'DELTA'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/PARK')
def PARK_total_counts():
    x_district = coded_df['county'] == f'PARK'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')


@app.route('/EAGLE')
def EAGLE_total_counts():
    x_district = coded_df['county'] == f'EAGLE'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/LOGAN')
def LOGAN_total_counts():
    x_district = coded_df['county'] == f'LOGAN'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/GILPIN')
def GILPIN_total_counts():
    x_district = coded_df['county'] == f'GILPIN'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')


@app.route('/GARFIELD')
def GARFIELD_total_counts():
    x_district = coded_df['county'] == f'GARFIELD'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/BENT')
def BENT_total_counts():
    x_district = coded_df['county'] == f'BENT'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')


@app.route('/MORGAN')
def MORGAN_total_counts():
    x_district = coded_df['county'] == f'MORGAN'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/LAS_ANIMAS')
def LAS_ANIMAS_total_counts():
    x_district = coded_df['county'] == f'LAS ANIMAS'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/OTERO')
def OTERO_total_counts():
    x_district = coded_df['county'] == f'OTERO'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/GUNNISON')
def GUNNISON_total_counts():
    x_district = coded_df['county'] == f'GUNNISON'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/PITKIN')
def PITKIN_total_counts():
    x_district = coded_df['county'] == f'PITKIN'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/MONTROSE')
def MONTROSE_total_counts():
    x_district = coded_df['county'] == f'MONTROSE'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/GRAND')
def GRAND_total_counts():
    x_district = coded_df['county'] == f'GRAND'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/SAGUACHE')
def SAGUACHE_total_counts():
    x_district = coded_df['county'] == f'SAGUACHE'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/CHAFFEE')
def CHAFFEE_total_counts():
    x_district = coded_df['county'] == f'CHAFFEE'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')


@app.route('/JACKSON')
def JACKSON_total_counts():
    x_district = coded_df['county'] == f'JACKSON'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/LINCOLN')
def LINCOLN_total_counts():
    x_district = coded_df['county'] == f'LINCOLN'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/CONEJOS')
def CONEJOS_total_counts():
    x_district = coded_df['county'] == f'CONEJOS'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/WASHINGTON')
def WASHINGTON_total_counts():
    x_district = coded_df['county'] == f'WASHINGTON'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/SAN_MIGUEL')
def SAN_MIGUEL_total_counts():
    x_district = coded_df['county'] == f'SAN MIGUEL'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/SEDGWICK')
def SEDGWICK_total_counts():
    x_district = coded_df['county'] == f'SEDGWICK'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/MINERAL')
def MINERAL_total_counts():
    x_district = coded_df['county'] == f'MINERAL'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/MOFFAT')
def MOFFAT_total_counts():
    x_district = coded_df['county'] == f'MOFFAT'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')


@app.route('/LAKE')
def LAKE_total_counts():
    x_district = coded_df['county'] == f'LAKE'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')

@app.route('/ARCHULETA')
def ARCHULETA_total_counts():
    x_district = coded_df['county'] == f'ARCHULETA'
    x_district_coded = coded_df[x_district]
    x_district_count = coded_df[x_district].shape[0]
    x_district_members_verified_count = x_district_coded['roles'] == 'member,verified'
    x_district_verified_members_count = x_district_coded['roles'] == 'verified,member'
    x_district_m_v = x_district_coded[x_district_members_verified_count]
    x_district_v_m = x_district_coded[x_district_verified_members_count]
    x_district_total_members = x_district_m_v.shape[0] + x_district_v_m.shape[0]
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
    keys = ['x_district_subscribers_count', 'x_district_total_members', 'xd_nm_total']
    list_totals = [x_district_count, x_district_total_members, xd_nm_total]
    for key in keys: 
        for value in list_totals: 
            json_object[key] = value 
            list_totals.remove(value) 
            break
    df = pd.DataFrame([json_object])
    return df.to_json(orient='records')


if __name__ == "__main__":
    app.run(debug=True)