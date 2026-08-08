from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SearchEngine:
   def __init__(self, dataframe, text_processor):
       self.dataframe = dataframe
       self.text_processor = text_processor

       self.questions = None
       self.processed_questions = None

       self.vectorizer = None
       self.tfidf_matrix = None

       self.prepare_questions()
       self.create_tfidf_matrix()


   def prepare_questions(self):
        
        self.questions = self.dataframe["Question"].tolist()
        self.processed_questions = []
        for question in self.questions:
            tokens = self.text_processor.process_text(question)
            processed_question = " ".join(tokens)
            self.processed_questions.append(processed_question)


   def create_tfidf_matrix(self):
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(self.processed_questions)
                

   def search(self, user_question):
      
      tokens = self.text_processor.process_text(user_question)
      processed_question = " ".join(tokens)
      user_vector = self.vectorizer.transform([processed_question])

      similarity_scores = cosine_similarity( user_vector, self.tfidf_matrix)
      best_match_index = similarity_scores.argmax()

      best_score = similarity_scores[0][best_match_index]

      if best_score < 0.10:
           return "Sorry, I don't understand your question."
      
      answer = self.dataframe.iloc[best_match_index]["Answer"]
      return answer      