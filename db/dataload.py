from sqlalchemy import create_engine
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String, Boolean, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Launches(Base):
    __tablename__ = 'launches'

    launch_id = Column(Integer, primary_key=True)
    mission_name = Column(String)
    launch_site = Column(String)
    launch_success = Column(Boolean)
    launch_date_unix = Column(BIGINT)
    flikr_img = Column(String)


import json

with open("launchdata.json") as launch_datafile:
    launch_data = json.load(launch_datafile)
    launches = launch_data['data']['launchesPast']
    launch_arr = []

    for launch in launches:
        launch_arr.append(
            Launches(launch_id=launch['id'], mission_name=launch['mission_name'],
                     launch_site=launch['launch_site']['site_name'], launch_success=launch['launch_success'],
                     launch_date_unix=launch['launch_date_unix'],
                     flikr_img=",".join(launch['links']['flickr_images'])
                     )
        )

engine = create_engine(
    "mysql+pymysql://root@localhost:3308/spacex")

Session = sessionmaker(bind=engine)
session = Session()
session.add_all(launch_arr)
session.commit()
