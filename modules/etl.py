from typing import Dict, List
import pandas as pd

class Etl:
    def __init__(self, codebook, data):
        self.codebook = codebook
        self.data = data

    def get_group_id(self) -> List:
        '''
        Docstring for get_group_id
        
        :param self: Description
        :return: Returns list of group_ids in codebook
        :rtype: List[Str]
        '''
        group_ids = [str]
        for group_id in self.codebook['group_id']:
            group_ids.append(group_id)

        return group_ids


    def get_main_questions(self) -> List:
        '''
        Docstring for get_main_questions
        
        :param self: Description
        :return: Returns  list of main_questions in codebook
        :rtype: List[Str]
        '''
        main_questions = [str]
        for questions in self.codebook['main_question']:
            main_questions.append(questions)
        
        return main_questions
    
    def get_encoding(self) -> List:
        '''
        Docstring for get_encoding
        
        :param self: Description
        :return: Returns list of encodings in codebook
        :rtype: List[Any]
        '''
        encodings = [str]
        for item in self.codebook['items']:
            for k in item:
                encodings.append(k)
        
        return encodings
        

    def get_items(self) -> Dict:
        '''
        Docstring for get_items
        
        :param self: Description
        :return: Returns items, where the id is the key and the elemnts are dictionairies
        :rtype: Dict[Str, Dict]
        '''
        items = {str: dict}
        for item in self.codebook['items']:
            items.update(item)
        
        return items
    
    def _err_check_get_single_item(self, encoding: str) -> None:
        if encoding not in self.get_encoding():
            raise ValueError('Encoding does not exist')

    def get_single_item(self, encoding: str) -> List:
        '''
        Docstring for get_single_item
        
        :param self: Description
        :param encoding: Encoded question 'v_0000'
        :type encoding: str
        :return: Returns list of question information
        :rtype: List[Any]
        '''
        self._err_check_get_single_item(encoding)
        return [self.get_items()[encoding]]
    

        
    def get_item_label(self, encoding: str) -> str:
        '''
        Docstring for get_item_label
        
        :param self: Description
        :param encoding: Description
        :type encoding: str
        :return: Returns item label
        :rtype: str
        '''
        label = ""
        for k in self.get_single_item(encoding):
            label = k['label']
        return label       

    def get_item_type(self, encoding) -> str:
        item_type = ""
        for k in self.get_single_item(encoding):
            item_type = k['type']
        
        return item_type

    def _get_item_level_options(self, encoding: str) -> Dict:
        '''Returns options defined directly on the item, or empty dict if none'''
        item = self.get_items()[encoding]
        return item.get('options', {})
    
    def _get_group_level_options(self, encoding: str) -> Dict:
        '''Returns options defined at the group level for this item, or empty dict if none'''
        for group in self.codebook.to_dict('records'):
            if encoding in group.get('items', {}):
                options = group.get('options')
                return options if options else {}
        return {}

    def get_item_options(self, encoding: str) -> Dict:
        '''
        Returns options for a given encoding.
        Checks item-level options first, falls back to group-level options.
        
        :param encoding: Encoded question 'v_0000'
        :type encoding: str
        :return: Returns options dictionary
        :rtype: Dict
        '''
        self._encoding_check(encoding)
        
        item_options = self._get_item_level_options(encoding)
        if item_options:
            return item_options
        
        return self._get_group_level_options(encoding)

            
    def _encoding_check(self, encoding):
        if encoding not in self.get_encoding():
            raise ValueError('Invalid Encoding')

    def get_main_question(self, encoding: str) -> str:
        """
        Returns the main question for a given encoding.
        :param encoding: Encoded question (e.g., 'v_2897')
        :return: Main question string
        """
        for group in self.codebook.to_dict('records'):
            if encoding in group.get('items', {}):
                return group.get('main_question', '')
        return ''
        



        
if __name__ == "__main__":
    codebook = pd.read_json("./data/codebook.json")
    data = pd.read_csv("./data/data_project_metset.csv", sep=";")

    etl = Etl(codebook=codebook, data=data)

    # print(etl.get_group_id())
    # print(etl.get_main_questions())
    # print(etl.get_encoding())
    # print(etl.get_items())
    # print(etl.get_encoding())

    # items = etl.get_items()
    # print(items['v_1753'])

    # v_1753 = etl.get_single_item('v_1753')
    # print(v_1753)

    # print(etl.get_single_item('v_71'))
    # print('-----')
    # print(etl.get_item_label('v_71'))
    # print(etl.get_item_type('v_71'))
    # print(etl.get_item_options('v_2851'))

    print("Item-level options (v_1752):", etl.get_item_options('v_1752'))
    print("Item-level options (v_71):", etl.get_item_options('v_71'))
    
    print("Group-level options (v_2851):", etl.get_item_options('v_2851'))

    