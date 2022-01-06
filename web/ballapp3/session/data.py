from ballapp3.config import SessionConfig
from string import Template
import os
import json



class SessionManager:
    def __init__(self, session_type):
        self.session_type = session_type


    FREE_THROW = 'free_throw'


    def files_dir(self):
        return os.path.join(SessionConfig.DATA_DIR, self.session_type)


    def get_json_files(self, remove_extension=False):
        extension = '.json'
        if not remove_extension:
            return [f for f in os.listdir(self.files_dir()) if f.endswith(extension)]
        else:
            return [f.replace('.json','') for f in os.listdir(self.files_dir()) if f.endswith(extension)]

    def all(self):
        return list(
            map(
                lambda x: x.replace('.json', ''),self.get_json_files()
            )
        )

    def get_template_content(self):
        '''
        Return template content
        WARNING: It is not possible to return this as json as it includes special characters
            because it's a template file ($ is a variable that is meant to be replaced)
        :return:
        '''
        with open(SessionConfig.TEMPLATE_FILE, 'r') as f:
            return f.read()

    def get_content(self, session_name):
        json_content_dir = os.path.join(self.files_dir(), session_name)
        with open(f'{json_content_dir}.json', 'r') as f:
            return json.load(f)

    def create_file(self, name):
        new_file = f"{os.path.join(self.files_dir(), name)}.json"
        src = Template(self.get_template_content())

        with open(new_file, 'w') as f:
            f.write(src.template)

    def edit_file_attempts_str(self, name, attempts_str, delete_last=False):
        file_path = os.path.join(self.files_dir(), name)
        file_exists = os.path.isfile(file_path)
        if file_exists:
            with open(file_path, 'r+') as f:
                data = json.load(f)
                f.seek(0)
                if not delete_last:
                    data['session']['attempts_str'] += attempts_str
                else:
                    data['session']['attempts_str'] =  data['session']['attempts_str'][:-1]
                f.truncate()
                json.dump(data, f, indent=4)


class DataAnalyzation:
    def __init__(self):
        pass