import data_upload
import dotenv
import os
def UOM_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'UOM Conversions - DPL.xlsx'
    sheet_name ='UOM'
    header_row= 4
    lookup_type = 'unit_of_measurement'
    usecols = ['UNIT NAME',
               'PA UNIT NAME', 'UNIT ALT NAME', 'CONVERSION FORMULA',
               'CONVERSION FORMULA2', 'UNIT SYSTEM', 'UNIT TYPE', 'BASE UNIT']
    lookup_val_column = 'UNIT NAME'
    category_column = 'UNIT TYPE'
    rename_cols = {'PA UNIT NAME': 'pa_unit_name', 'UNIT ALT NAME': 'unit_alt_name',
                   'CONVERSION FORMULA': 'conversion_formula',
                   'CONVERSION FORMULA2': 'conversion_formula2', 'UNIT SYSTEM': 'unit_system',
                   'BASE UNIT': 'base_unit'}
    database=data_upload.get_database(endpoint,
                             key,
                             database_name)
    data_upload.data_upload(database,container_name,file_name,sheet_name,lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row,usecols=usecols,
                            rename_cols=rename_cols
                            )
def SealClass_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='SealClass'
    header_row= 4
    lookup_type = 'seal_class'
    usecols = ['SealClass','Default','Restrictions','World Area']
    lookup_val_column = 'SealClass'
    category_column = 'Unnamed: 3'
    rename_cols = {'Default': 'default', 'Restrictions': 'restrictions',
                   'World Area': 'world_area'}
    database=data_upload.get_database(endpoint,
                             key,
                             database_name)
    data_upload.data_upload(database,container_name,file_name,sheet_name,lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row,usecols=usecols,
                            rename_cols=rename_cols
                            )


def DiaphragmCompatibility_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='DiaphragmCompatibility'
    header_row= 5
    usecols = ['ProcessFillFluid']
    lookup_type = 'process_fluid'
    lookup_val_column = 'ProcessFillFluid'
    database=data_upload.get_database(endpoint,
                             key,
                             database_name)
    data_upload.data_upload(database,container_name,file_name,sheet_name,lookup_type,
                            lookup_val_column,
                            header=header_row,usecols=usecols
                            )


def IndustryStandard_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='IndustryStandard'
    header_row= 1
    usecols = ['IndustryStandard','Default','Restrictions']
    lookup_type = 'industry_standard'
    lookup_val_column = 'IndustryStandard'
    rename_cols = {'Default': 'default', 'Restrictions': 'restrictions'}
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )

def GasketSurface_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='GasketSurface'
    header_row= 1
    usecols = ['ConnectionType','Default','Restrictions']
    lookup_type = 'gasket_surface'
    lookup_val_column = 'ConnectionType'
    rename_cols = {'Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )

def ConnectionSize_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='ConnectionSize'
    header_row= 1
    usecols = ['ConnectionSize','Default','Restrictions']
    lookup_type = 'connection_size'
    lookup_val_column = 'ConnectionSize'
    rename_cols = {'Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )


def PressureRating_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='PressureRating'
    header_row= 1
    usecols = ['PressureRating','Default','Restrictions']
    lookup_type = 'pressure_rating'
    lookup_val_column = 'PressureRating'
    rename_cols = {'Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )

def ExtensionDiameter_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='ExtensionDiameter'
    header_row= 1
    usecols = ['ExtensionDiameter','Default','Restrictions']
    lookup_type = 'extension_diameter'
    lookup_val_column = 'ExtensionDiameter'
    rename_cols = {'Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )


def ExtensionLength_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='ExtensionLength'
    header_row= 1
    usecols = ['ExtensionLength','LNomExL (inches)','Default','Restrictions']
    lookup_type = 'extension_length'
    lookup_val_column = 'ExtensionLength'
    rename_cols = {'LNomExL (inches)':'ExlenValue','Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )


def AddExtensionLength_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='AddExtensionLength'
    header_row= 1
    usecols = ['AddExtensionLength','LAddExL (inches)','Default','Restrictions']
    lookup_type = 'additional_extension_length'
    lookup_val_column = 'AddExtensionLength'
    rename_cols = {'LAddExL (inches)':'AddExlenValue','Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )

def DiaphragmMaterial_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='DiaphragmMaterial'
    header_row= 1
    usecols = ['DiaphragmMaterial','Tmax','Default','Restrictions']
    lookup_type = 'diaphragm_material'
    lookup_val_column = 'DiaphragmMaterial'
    rename_cols = {'Tmax':'max_temp','Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )

def DiaphragmCoating_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='DiaphragmCoating'
    header_row= 1
    usecols = ['Diaphragm Coating','Default','Restrictions']
    lookup_type = 'diaphragm_coating'
    lookup_val_column = 'Diaphragm Coating'
    rename_cols = {'Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )


def FlangeMaterial_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='FlangeMaterial'
    header_row= 1
    usecols = ['FlangeMaterial','Default','Restrictions']
    lookup_type = 'flange_material'
    lookup_val_column = 'FlangeMaterial'
    rename_cols = {'Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )


def LowerHousingMaterial_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='LowerHousingMaterial'
    header_row= 1
    usecols = ['LowerHousingMaterial']
    lookup_type = 'lower_housing_material'
    lookup_val_column = 'LowerHousingMaterial'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,
                            header=header_row, usecols=usecols,
                            )

def FlushSizeQty_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='FlushSizeQty'
    header_row= 1
    usecols = ['FlushSizeQty','Default','Restrictions']
    lookup_type = 'flush_size_quantity'
    lookup_val_column = 'FlushSizeQty'
    rename_cols = {'Default': 'default', 'Restrictions': 'restrictions'}
    category_column = 'Rule Logic'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,category_column=category_column,
                            header=header_row, usecols=usecols,
                            rename_cols=rename_cols
                            )


def GasketMaterial_upload():
    dotenv.read_dotenv()
    endpoint = os.environ['URL']
    key = os.environ['CREDENTIAL']
    database_name = os.environ['DATABASE_NAME']
    container_name = 'lpa-lookup'
    file_name = 'DP Level Product Advisor Logic_MVP_rev7_2020 Oct 5.xlsx'
    sheet_name ='GasketMaterial'
    header_row= 1
    usecols = ['GasketMaterial']
    lookup_type = 'gasket_material'
    lookup_val_column = 'GasketMaterial'
    database = data_upload.get_database(endpoint,
                                        key,
                                        database_name)
    data_upload.data_upload(database, container_name, file_name, sheet_name, lookup_type,
                            lookup_val_column,
                            header=header_row, usecols=usecols,
                            )


if __name__== '__main__':
    UOM_upload()
    SealClass_upload()
    DiaphragmCompatibility_upload()
    IndustryStandard_upload()
    GasketSurface_upload()
    ConnectionSize_upload()
    PressureRating_upload()
    ExtensionDiameter_upload()
    ExtensionLength_upload()
    AddExtensionLength_upload()
    DiaphragmMaterial_upload()
    DiaphragmCoating_upload()
    FlangeMaterial_upload()
    LowerHousingMaterial_upload()
    FlushSizeQty_upload()
    GasketMaterial_upload()