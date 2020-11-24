import uuid
import pandas as pd
import numpy as np
import datetime
from azure.cosmos import exceptions, CosmosClient, PartitionKey

def get_database(endpoint,key,database_name):
    endpoint = endpoint
    key = key
    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database_name)
    return database

def data_upload(database,container_name,file_name,sheet_name,lookup_type,lookup_val_column,
                category_column=None,header=0,usecols=None,rename_cols=None,
                source_system=None,source_identifier=None,lang='en_us',isDefault=False,isActive=True,
               security_group=['Internal','External'],created_by=-1):

    df = pd.read_excel(file_name, sheet_name=sheet_name,header=header,usecols=usecols)

    df.rename(columns={lookup_val_column:'lookup_value'},inplace=True)
    if category_column:
        df.rename(columns={category_column:'category'},inplace=True)
        df['category'].fillna(method='ffill', inplace=True)
    if rename_cols:
        df.rename(columns=rename_cols,inplace=True)

    df.replace({np.NAN:None},inplace=True)

    rec = df.to_dict(orient='records')
    container = database.get_container_client(container_name)
    for item in rec:
        item['id'] = str(uuid.uuid4())
        item['source'] = {'source_system':source_system,'source_identifier':source_identifier}
        item['lookup_type'] = lookup_type
        item['lookup_code'] = lookup_type+'_'+item['id']
        if category_column:
            item['description'] = {'language_code':lang,'category':item['category']}
        else:
            item['description'] = {'language_code': lang}
        item['isDefault'] = isDefault
        item['isActive'] = isActive
        item['security_group'] = security_group
        item['created_date'] = datetime.datetime.now().isoformat()
        item['created_by'] = created_by
        item['updated_date'] = None
        item['updated_by'] = None
        container.create_item(body=item)

