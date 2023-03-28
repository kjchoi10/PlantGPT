
import pandas as pd
import numpy as  np
import openai

class ChatGPTModule():

    def return_plant_list(textFilePath: str, plantName: str):
        """
        textFile: the file path of the text file with plant names. Hardcoded for USDA. Exampe: "./data/plant_lexicon/USDAPlantNames.txt"
        plantName: the column name of the plant name. Example "Common Name"
        return: list of plant names.
        """
        # plant names database
        list_plant_names = list(set(pd.read_csv(textFilePath, sep=",")[plantName].dropna()))

        return(list_plant_names)

    def filter_plant_list(list_plant_names: list, filterNum: int):
        """
        list_plant_names: list of plant names.
        filterNum: the number of filterable plant names. Use case to keep the plant list name small
        return: list of filtered plant names.
        """
        return(list_plant_names[0:filterNum])


    def ask_chat_gpt(list_plant_names: list, message_history: dict, type_of_questions: list, gpt_model: str):
        """
        message_history: config["message_history"]
        type_of_questions: config["type_of_questions"]
        gpt_model: config["gpt_model"]
        return: pandas dataframe of message_history
        """

        for plant_name in list_plant_names:
            list_of_questions = [
            f"What is the most poular use of {plant_name}? Reply in a list.",
            f"What are the ideal grow conditions for {plant_name}? Reply in a list.",
            f"What is the origin and history of {plant_name}?"
            ]
            for question in list_of_questions:
                completion = openai.ChatCompletion.create(
                    model=gpt_model,
                    messages=[{"role": "user", "content": question}]
                )
                message_history["plant_name"].append(plant_name)
                message_history["question"].append(question)
                message_history["content"].append(completion.choices[0].message.content)
        
        return(pd.DataFrame(message_history))
    