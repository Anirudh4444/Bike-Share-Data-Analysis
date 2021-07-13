import pymongo
import json
from pymongo import MongoClient
client = MongoClient("mongodb://admin:password@ae8c9d88ccf0b42c2aed41d4191b077d-1772724681.us-west-2.elb.amazonaws.com:80/devnetops37?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")

client_details=client["devnetops37"]
coll=client_details["test"]
coll2=client_details["test_suite"]
b=coll2.find({},{"_id":0})
a=coll.find({},{"_id":0})
nf="EPC"
gh="Test_suite1"
ak=[]
aw=True
for z in b:
    xx=z["Test_suite_name"]
    if(xx==gh):
        print("Error")
        aw=False
        break
if(aw==True):
    for x in a:
        y=x['NF_Type']
        if(y==nf):
            ak.append(x)
    final={
        "Test_suite_name":"Test_suite1",
        "test_cases ": ak
    }
    coll2.insert_one(final)





# coll2=client_details["assets"]
# y=input("Enter NF tag")
# yy=input("Enter project name ")
# project_asset=[]
# asset_list=[]
# final={}
# for project_manag in coll.find({},{ "_id": 0, "releases": 1,"project_name":1,"project_id":1}):
#     release =project_manag["releases"]
#     projectname=project_manag["project_name"]
#
#     if (len(release)>0):
#         for index in range(len(release)):
#             check_assets=True
#             if((release[index]["release_status"]==y) and (projectname==yy)):
#                 asset_detail=coll2.find({},{"_id":0,"release_no":release[index]["release_number"],"name":1,"projectid":1,"assetid":1})
#                 for assets in asset_detail:
#                     if((project_manag["project_id"]==assets["projectid"])and(assets["release_no"]==release[index]["release_number"])):
#                         assets.pop("projectid",None)
#                         onboard_date = ''
#                         onboard_date = onboard_date + assets['assetid'][8:10] + '-' + assets['assetid'][6:8] + '-' + \
#                                        assets['assetid'][2:6]
#                         assets.pop("assetid", None)
#                         assets.pop("release_no", None)
#                         assets["Onboarding_date"]=onboard_date
#                         check_assets=False
#                         asset_list.append(assets)
#                 if(check_assets!=False):
#                     final = {
#                         'release_details': release[index],
#                         'asset_details': "No Assets associated"
#                     }
#
#                 else:
#                     final = {
#                         'release_details': release[index],
#                         'asset_details': asset_list
#                     }
#                 project_asset.append(final)
#                 asset_list=[]
#
#
#
# json_object = json.dumps(project_asset, indent = 4)
# print(json_object)