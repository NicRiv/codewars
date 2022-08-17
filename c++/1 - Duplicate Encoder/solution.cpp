// Duplicate Encoder
// Level: 6 kyu

#include <string>
#include <cctype>

std::string duplicate_encoder(const std::string& word){
  std::string new_word;
  bool aprs;
  
  for (unsigned int i = 0; i < word.length(); i++) {
    aprs = false;
    
    for (unsigned int j = 0; j < word.length(); j++) {
      if ((i != j) && (tolower(word[i]) == tolower(word[j]))) {
        aprs = true;
      }
    }
    
    if (aprs) {
      new_word += ")";
    } else {
      new_word += "(";
    }
  }
  return new_word;
}