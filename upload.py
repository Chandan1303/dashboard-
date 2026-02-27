import pandas as pd
from sqlalchemy import create_engine
import getpass
import urllib.parse


password = getpass.getpass("Enter MySQL password: ")


encoded_password = urllib.parse.quote_plus(password)


df = pd.read_excel("cleaned_data.xlsx")


df.columns = df.columns.str.strip().str.replace(" ", "_")


engine = create_engine(
    f"mysql+pymysql://root:{encoded_password}@localhost/sales_project"
)


df.to_sql("sales_data", engine, if_exists="replace", index=False)

print("Uploaded Successfully ")
