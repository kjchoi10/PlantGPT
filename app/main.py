

# library imports
import openai
from src.chatgpt import ChatGPTModule
import app_config.config as config

def main():
    # use openai key
    openai.api_key = open("key.txt", "r").read().strip('\n')

    # list of plant names from USDA
    list_plant_names = ChatGPTModule.return_plant_list("./data/plant_lexicon/USDAPlantNames.txt", "Common Name")
    # filter plant list
    if config.data_structures["filter"]:
        list_plant_names = ChatGPTModule.filter_plant_list(list_plant_names, filterNum=5)
    # get chatgpt data
    message_history = ChatGPTModule.ask_chat_gpt(list_plant_names, 
                                                config.data_structures["message_history"],
                                                config.data_structures["type_of_questions"],
                                                config.data_structures["gpt_model"]
    )
    # save data
    message_history.to_csv('./data/output/plant_meta_data.csv', sep ='\t')

if __name__ == '__main__':
    main()
