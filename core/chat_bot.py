from core.dataSet_Loader import DataSetLoader
from core.search_engine import SearchEngine
from core.textProcessor import TextProcessor

class Chat_Bot:
    def __init__(self):
        self.loader = DataSetLoader()
        self.dataframe = self.loader.load_dataset()
        self.Text_Processor = TextProcessor()
        self.Search_Engine = SearchEngine(self.dataframe, self.Text_Processor)


    def get_sent_Return_Function(self, user_question):
        answer = self.Search_Engine.search(user_question)
        return answer


    