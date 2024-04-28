from pathlib import Path
import json
import google.generativeai as genai


safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
    ]


def generate_recipe_from_image(image_path,safety_settings):
    # Set up the model
    genai.configure(api_key="AIzaSyAMXxR0hDneJxWj46kkLr8t3DSc1_jRDpY")
    prompt = "im strictly asking you to give me the name of hte  dish , only dish name,the dictionary should be (the key should be dish_name) give this into a perfect json format, so that while doing recipe_dict = json.loads(cleaned_string) it should not return any json.JSONDecodeError"


    generation_config = {
      "temperature": 0.4,
      "top_p": 1,
      "top_k": 32,
      "max_output_tokens": 4096,
    }


    model = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    # Validate that an image is present
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Could not find image: {image_path}")

    image_parts = [
      {
        "mime_type": "image/jpeg",
        "data": Path(image_path).read_bytes()
      },
    ]

    prompt_parts = [
      image_parts[0],
      prompt
    ]

    response = model.generate_content(prompt_parts)

    text_output = response.text

    cleaned_string = text_output.replace('\n', '').replace('\\n', '').replace('```','').replace('json','')
    # print(cleaned_string)

    # Convert the cleaned string to a dictionary
    recipe_dict = json.loads(cleaned_string)

    return recipe_dict



def generate_recipe_description_from_search(search_query,safety_settings):
    genai.configure(api_key="AIzaSyAMXxR0hDneJxWj46kkLr8t3DSc1_jRDpY")

    # Set up the model
    generation_config = {
      "temperature": 0.3,
      "top_p": 1,
      "top_k": 32,
      "max_output_tokens": 2096,
    }


    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message("im strictly asking you to generate with my requirements ,Generate a detailed and accurate description of the dish "+search_query+ ", including its name, ingredients required for preparation (quantity seperated with '-' example1: 1 cup - all-purpose flour,example2: 1/2 teaspoon - baking powder, example3- 1 - onion), and step-by-step instructions to prepare the dish with time. Ensure that each component of the description is clearly separated and organized. Give the output in a dictionary format {Name of the Dish, Ingredients Required, Step-by-Step Instructions}. Give it in a perfect dictionary format (json), in key value pair in dictionary give every values  in a list without instruction and steps seperated additional to that in the dictionary add time to make the dish in minutes and (easy medium or difficuilt) and how many servings. give this into a perfect json format, so that while doing recipe_dict = json.loads(cleaned_string) it should not return any json.JSONDecodeError")

    text_output = convo.last.text

    # Replace "\n" and "\\n" with empty string
    cleaned_string = text_output.replace('\n', '').replace('\\n', '').replace('```','').replace('json','')
    print(cleaned_string)

    try:
        recipe_dict = json.loads(cleaned_string)
        return recipe_dict
    except json.JSONDecodeError:
        convo.send_message(cleaned_string+ "   convert this into a perfect json format, so that while doing recipe_dict = json.loads(cleaned_string) it should not return any json.JSONDecodeError ")
        text_output = convo.last.text
        cleaned_string = text_output.replace('\n', '').replace('\\n', '').replace('```', '').replace('json', '')

        print(cleaned_string)

        recipe_dict = json.loads(cleaned_string)
        return recipe_dict


def generate_random_recipe_description(safety_settings):
    genai.configure(api_key="AIzaSyAMXxR0hDneJxWj46kkLr8t3DSc1_jRDpY")

    # Set up the model
    generation_config = {
      "temperature": 0.3,
      "top_p": 1,
      "top_k": 32,
      "max_output_tokens": 2096,
    }


    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[
    ])

    convo.send_message("im strictly asking you to give me a complete random dish name, only dish name,the dictionary should be (the key should be dish_name) give this into a perfect json format, so that while doing recipe_dict = json.loads(cleaned_string) it should not return any json.JSONDecodeError")

    text_output = convo.last.text

    # Replace "\n" and "\\n" with empty string
    cleaned_string = text_output.replace('\n', '').replace('\\n', '').replace('```','').replace('json','')
    print(cleaned_string)

    try:
        recipe_dict = json.loads(cleaned_string)
        return recipe_dict
    except json.JSONDecodeError:
        convo.send_message(cleaned_string+ "   convert this into a perfect json format, so that while doing recipe_dict = json.loads(cleaned_string) it should not return any json.JSONDecodeError ")
        text_output = convo.last.text
        cleaned_string = text_output.replace('\n', '').replace('\\n', '').replace('```', '').replace('json', '')

        print(cleaned_string)

        recipe_dict = json.loads(cleaned_string)
        return recipe_dict


# def generate_recipe_description_from_search(search_query, safety_settings):
#     genai.configure(api_key="AIzaSyAMXxR0hDneJxWj46kkLr8t3DSc1_jRDpY")  # Assuming you have an API key
#
#     # Set up the model
#     generation_config = {
#         "temperature": 0.3,
#         "top_p": 1,
#         "top_k": 32,
#         "max_output_tokens": 2096,
#     }
#
#     model = genai.GenerativeModel(
#         model_name="gemini-1.0-pro",
#         generation_config=generation_config,
#         safety_settings=safety_settings
#     )
#
#     def get_recipe():
#         convo = model.start_chat(history=[])
#         convo.send_message("Generate a detailed and accurate description of the dish " + search_query +
#                            ", including its name, ingredients required for preparation, and step-by-step instructions to prepare the dish with time. Ensure that each component of the description is clearly separated and organized. Give the output in a dictionary format {Name of the Dish, Ingredients Required, Step-by-Step Instructions}. Give it in a perfect dictionary format (json), in key value pair in dictionary give every values  in a list without instruction and steps separated additional to that in the dictionary add time to make the dish in minutes and (easy medium or difficult) and how many servings.")
#         text_output = convo.last.text
#
#         # Replace "\n" and "\\n" with empty string
#         cleaned_string = text_output.replace('\n', '').replace('\\n', '').replace('```', '').replace('json', '')
#         print(cleaned_string)
#
#
#         # Try to load the cleaned string as JSON
#         try:
#             recipe_dict = json.loads(cleaned_string)
#             return recipe_dict
#         except json.JSONDecodeError:
#             # If JSON decoding fails, retry by calling the function again recursively
#             return get_recipe()
#
#     return get_recipe()

#write a program for reverse string
