import requests
def download_original_json():
  url = "https://huggingface.co/rhasspy/piper-voices/raw/v1.0.0/voices.json"
  response = requests.get(url)

  if response.status_code == 200:
      with open("voices.json", "wb") as file:
          file.write(response.content)
      print("Download successful. File saved as voices.json")
  else:
      print(f"Failed to download. Status code: {response.status_code}")
import json
def format_json(input_file,output_file):
  download_original_json()
  with open(input_file, 'r', encoding='utf-8') as f:
      data = json.load(f)
  ### Only keep available high quality voice models
  keys = data.keys()
  filtered_keys = set()

  for key in keys:
      parts = key.split('-')
      language = parts[0]
      voice_name = parts[1]
      quality = parts[-1]  # Use the last part to get the quality

      # Check if there is a higher quality version already in the set
      if voice_name in filtered_keys:
          if quality == 'high':
              # If 'high' quality is found, remove the existing versions
              filtered_keys.discard(voice_name)
          elif quality == 'medium' and voice_name + '-high' not in filtered_keys:
              # If 'medium' quality is found and 'high' is not present, remove existing versions
              filtered_keys.discard(voice_name)
          elif quality == 'low' and voice_name + '-high' not in filtered_keys and voice_name + '-medium' not in filtered_keys:
              # If 'low' quality is found and 'high' and 'medium' are not present, remove existing versions
              filtered_keys.discard(voice_name)

      # Add the current key to the set
      filtered_keys.add(key)
  result_data = {}
  for i in filtered_keys:
      voice_model = data[i]
      voice_name = voice_model['name']
      name_english = voice_model['language']['name_english']
      country_english=voice_model['language']['country_english']

      unique_code=f"{name_english} ({name_english}, {country_english})"

      if unique_code not in result_data:
          result_data[unique_code] = {}

      result_data[unique_code][voice_name] = {
          "model_name": i,
          # Add other relevant information from voice_model if needed
      }



  with open(output_file, 'w', encoding='utf-8') as f:
      json.dump(result_data, f, indent=2)

format_json("voices.json","best_quality.json")
