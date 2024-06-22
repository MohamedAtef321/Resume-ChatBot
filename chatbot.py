from transformers import pipeline
import time

class Bot:
    
    def __init__(self):
        
        self.task = "question-answering"
        self.model = "deepset/roberta-base-squad2"
        self.reader = pipeline(task=self.task , model=self.model)
        
        # Read the resume text from a file
        with open("Resume Text.txt", "r") as file:
            self.content = file.read()

    def answer_question(self, question):
        
        outputs = self.reader(question=question, context=self.content)
        return outputs['answer']
    
    def stream_data(self, data):
        for word in data.split(" "):
            yield word + " "
            time.sleep(0.02)