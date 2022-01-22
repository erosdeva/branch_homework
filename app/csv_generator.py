from app.constants.table_headers import USER_TABLE_HEADER
from app.constants.table_headers import NAME_TABLE_HEADER
from app.constants.table_headers import LOCATION_TABLE_HEADER
from app.constants.table_headers import STREET_TABLE_HEADER
from app.constants.table_headers import COORDINATES_TABLE_HEADER
from app.constants.table_headers import TIMEZONE_TABLE_HEADER
from app.constants.table_headers import LOGIN_TABLE_HEADER
from app.constants.table_headers import DOB_TABLE_HEADER
from app.constants.table_headers import REGISTERED_TABLE_HEADER
from app.constants.table_headers import ID_TABLE_HEADER
from app.constants.table_headers import PICTURE_TABLE_HEADER
import csv
import json
import os
import uuid


def generate_csv_data():
    user_table_csv_data = [USER_TABLE_HEADER]
    name_table_csv_data = [NAME_TABLE_HEADER]
    location_table_csv_data = [LOCATION_TABLE_HEADER]
    street_table_csv_data = [STREET_TABLE_HEADER]
    coordinates_table_csv_data = [COORDINATES_TABLE_HEADER]
    timezone_table_csv_data = [TIMEZONE_TABLE_HEADER]
    login_table_csv_data = [LOGIN_TABLE_HEADER]
    dob_table_csv_data = [DOB_TABLE_HEADER]
    registered_table_csv_data = [REGISTERED_TABLE_HEADER]
    id_table_csv_data = [ID_TABLE_HEADER]
    picture_table_csv_data = [PICTURE_TABLE_HEADER]

    root_dir = os.path.abspath(os.curdir)
    with open((root_dir + '/app/data/api_output.json'), 'rb') as f:
        json_data = json.load(f)

    json_data_results = json_data['results']

    for result in json_data_results:
        # user row data
        login_uuid = result['login']['uuid']
        id = uuid.uuid4().hex
        gender = result['gender']
        name_id = uuid.uuid4().hex
        location_id = uuid.uuid4().hex
        email = result['email']
        dob_id = uuid.uuid4().hex
        registered_id = uuid.uuid4().hex
        phone = result['phone']
        cell = result['cell']
        picture_id = uuid.uuid4().hex
        nat = result['nat']

        user_row = [
            login_uuid,
            id,
            gender,
            name_id,
            location_id,
            email,
            dob_id,
            registered_id,
            phone,
            cell,
            picture_id,
            nat
        ]

        user_table_csv_data.append(user_row)

        # name table data
        name_row = [
            name_id,
            result['name']['title'],
            result['name']['first'],
            result['name']['last'],
        ]

        name_table_csv_data.append(name_row)

        # location table data
        street_id = uuid.uuid4().hex
        coordinated_id = uuid.uuid4().hex
        timezone_id = uuid.uuid4().hex

        location_row = [
            location_id,
            street_id,
            result['location']['city'],
            result['location']['state'],
            result['location']['country'],
            result['location']['postcode'],
            coordinated_id,
            timezone_id
        ]

        location_table_csv_data.append(location_row)

        # street table data
        street_row = [
            street_id,
            result['location']['street']['number'],
            result['location']['street']['name'],
        ]

        street_table_csv_data.append(street_row)

        # coordinates table data
        coordinates_row = [
            coordinated_id,
            result['location']['coordinates']['latitude'],
            result['location']['coordinates']['longitude'],
        ]

        coordinates_table_csv_data.append(coordinates_row)

        # timezone table data
        timezone_row = [
            timezone_id,
            result['location']['timezone']['offset'],
            result['location']['timezone']['description'],
        ]

        timezone_table_csv_data.append(timezone_row)

        # login table data
        login_row = [
            login_uuid,
            result['login']['username'],
            result['login']['password'],
            result['login']['salt'],
            result['login']['md5'],
            result['login']['sha1'],
            result['login']['sha256'],
        ]

        login_table_csv_data.append(login_row)

        # dob table data
        dob_row = [
            dob_id,
            result['dob']['date'],
            result['dob']['age'],
        ]

        dob_table_csv_data.append(dob_row)

        # registered table data
        registered_row = [
            registered_id,
            result['registered']['date'],
            result['registered']['age'],
        ]

        registered_table_csv_data.append(registered_row)

        # id table data
        id_row = [
            id,
            result['id']['name'],
            result['id']['value'],
        ]

        id_table_csv_data.append(id_row)

        # picture table data
        picture_row = [
            picture_id,
            result['picture']['large'],
            result['picture']['medium'],
            result['picture']['thumbnail'],
        ]

        picture_table_csv_data.append(picture_row)

        # WRITE TABLE DATA AS CSV FILES IN RESULTS DIRECTORY

        # USER TABLE
        with open((root_dir + '/app/results/user_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(user_table_csv_data)

        # NAME TABLE
        with open((root_dir + '/app/results/name_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(name_table_csv_data)

        # LOCATION TABLE
        with open((root_dir + '/app/results/location_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(location_table_csv_data)

        # STREET TABLE
        with open((root_dir + '/app/results/street_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(street_table_csv_data)

        # COORDINATES TABLE
        with open((root_dir + '/app/results/coordinates_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(coordinates_table_csv_data)

        # TIMEZONE TABLE
        with open((root_dir + '/app/results/timezone_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(timezone_table_csv_data)

        # LOGIN TABLE
        with open((root_dir + '/app/results/login_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(login_table_csv_data)

        # DOB TABLE
        with open((root_dir + '/app/results/dob_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(dob_table_csv_data)

        # REGISTERED TABLE
        with open((root_dir + '/app/results/registered_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(registered_table_csv_data)

        # ID TABLE
        with open((root_dir + '/app/results/id_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(id_table_csv_data)

        # PICTURE TABLE
        with open((root_dir + '/app/results/picture_data.csv'), "w+") as my_csv:
            csv_writer = csv.writer(my_csv, delimiter=',')
            csv_writer.writerows(picture_table_csv_data)
