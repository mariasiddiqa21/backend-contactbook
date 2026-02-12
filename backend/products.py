import json
from pathlib import Path
from typing import List,Dict

data_file= Path("data","products.json")
def load_products() ->List[Dict]:
  if not data_file.exists():
    return []
  with data_file.open("r") as f:
    return json.load(f)
  
def get_all_products():
  return load_products()  