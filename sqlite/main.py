from utils import xml_to_list , datalist_to_csv , country_seperate_to_csv , Clean_data
from database_utils import create_database , create_view , insert_database , sqlite_to_json

# datalist = xml_to_list("../data-devclub-1.xml")
# datalist = Clean_data(datalist)
# datalist_to_csv(datalist, "../csv_result/result.csv")
# country_seperate_to_csv(datalist, "../csv_result/By_country/")

create_database('devclub.db')
insert_database('../data-devclub-1.xml')
