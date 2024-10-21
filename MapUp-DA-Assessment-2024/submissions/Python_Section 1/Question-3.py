# nested and flatten dict

def flatten(dictonary):

    flattened = {}

    for key, value in dictonary.items():

        if isinstance(value, dict):
            flattened.update(flatten(value, key + "."))
        
        elif isinstance(value, list):

            for i, item in enumerate(value):

                if isinstance(item, dict):

                    flattened.update(flatten(item, key + f"[{i}]."))
                else:
                    flattened[key + f"[{i}]"] = item

        else:
            flattened[key] = value

    return flattened

nested_dict = {
  "section1.subsection1.key1": "value1",
  "section1.subsection1.key2": "value2",
  "section1.subsection2.key3": "value3",
  "section2[0].key4": "value4",
  "section2[1].key5": "value5",
  "section2[1].sublist[0]": 1,
  "section2[1].sublist[1]": 2,
  "section2[1].sublist[2]": 3
}

flattened = flatten(nested_dict)
print(flattened)