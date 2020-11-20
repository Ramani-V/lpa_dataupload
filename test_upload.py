import data_upload
import dotenv
import os
def test_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa_uom'
    file_name = 'UOM Conversions - DPL.xlsx'
    sheet_name ='UOM'
    header_row=4
    usecols = ['UNIT NAME',
               'PA UNIT NAME', 'UNIT ALT NAME', 'CONVERSION FORMULA',
               'CONVERSION FORMULA2', 'UNIT SYSTEM', 'UNIT TYPE', 'BASE UNIT']
    rename_cols = {'UNIT NAME': 'unit_name',
                   'PA UNIT NAME': 'pa_unit_name', 'UNIT ALT NAME': 'unit_alt_name',
                   'CONVERSION FORMULA': 'conversion_formula',
                   'CONVERSION FORMULA2': 'conversion_formula2', 'UNIT SYSTEM': 'unit_system', 'UNIT TYPE': 'unit_type',
                   'BASE UNIT': 'base_unit'}
    database=data_upload.get_database(endpoint,
                             key,
                             database_name)
    data_upload.data_upload(database,container_name,file_name,sheet_name,header=header_row,usecols=usecols,rename_cols=rename_cols
                            )


if __name__== '__main__':
    test_upload()