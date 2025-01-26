import json
import os
import datetime

from typing import Any, Dict, Union


class HistorySaver:
    __PATH_TO_FILE: str = "D:\\Coding\\PYTHON\\small_projects\\text encoder\\hist.json"
    

    @staticmethod
    def __get_data_from_json() -> Union[Dict[Any, Any], None]: 
        try:
            with open(HistorySaver.__PATH_TO_FILE, 'r+', encoding='utf-8') as file: 
                data = json.load(file)
        except FileNotFoundError as e:
            print(f"[!] OOPS... there is no json file: {e}")
        except Exception as e:
            print(f"[!] OOPS... something went wrong during getting data from json: {e}")
        else: 
            return data
        
        return None
    

    @staticmethod
    def save(mes: str, start: str, result: str) -> None:
        data: Dict[Any, Any] = HistorySaver.__get_data_from_json()

        current_datetime = datetime.datetime.now()
        cur_time: str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        data[len(data.keys())+1] = f"{mes.upper()} in {cur_time}\nstart: {start}\nresult: {result}" 

        try:
            with open(HistorySaver.__PATH_TO_FILE, 'w', encoding='utf-8') as file: 
                json.dump(data, file, indent=4)
        except FileNotFoundError as e:
            print(f"[!] OOPS... there is no json file: {e}")
        except Exception as e:
            print(f"[!] OOPS... something went wrong during saving history into json: {e}")


if __name__ == '__main__':
    ...