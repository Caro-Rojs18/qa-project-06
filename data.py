headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

def get_kit_body(name):
    return kit_bodies[name].copy()

kit_bodies = {
    "one_character": {"name" :"a"},
    "maximum_characters" : {"name": ("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                                     "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                                     "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabC")},
     "empty_string": {"name": ""},
     "Maximum_plus_one_characters" : {"name": ("Abcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                              "abcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                              "abcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                              "abcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                              "abcdabcdabcdabcdabcdabcdabcdabcdabcda"
                                              "bcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                              "cdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                                              "dAbcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                              "abcdabcdabcdabcdabcdabcdabcdabcdabcda"
                                              "bcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                              "cdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                                              "dabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                              "abcdabcdabcdabcdabcdabcdabcdabcdabcda"
                                              "bcdabcdabcdabcdabcdabcdabcdabcdabcD")}
}






