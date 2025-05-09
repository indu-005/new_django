 pip install dj-database-url
import dj-database-url
 import os
DATABASES  
 "default": dj_database_url.parse(os.environ.get("postgresql://test_db_o8rh_user:IgvbuxxnXURWUmcw63Bif7qk9BNmVDDw@dpg-d0epgsemcj7s7382ol8g-a.oregon-postgres.render.com/test_db_o8rh"))
