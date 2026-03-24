# Define different types of Samasa (Compound Words) with their components
dvandva_samasa = {
    'ಮಹಾಪುರುಷ': ['ಮಹಾ', 'ಪುರುಷ'],
    'ಹಾಲಹರ': ['ಹಾಲ', 'ಹರ']
}
tatpurusha_samasa = {
    'ರಕ್ತಪಾತ': ['ರಕ್ತ', 'ಪಾತ'],
    'ಅವನತಿ': ['ಅವ', 'ನತಿ']
}
bahuvrihi_samasa = {
    'ಚಂದ್ರಮತಿ': ['ಚಂದ್ರ', 'ಮತಿ'],
    'ಅಮೃತಮತು': ['ಅಮೃತ', 'ಮತು']
}
dvigu_samasa = {
    'ನಾಟಕಮಣಿಯ': ['ನಾಟಕ', 'ಮಣಿಯ'],
    'ಬಲಿದಾನ': ['ಬಲಿ', 'ದಾನ']
}

# Function to check if a word is a compound word and its type
def identify_samasa_type(word):
    if word in dvandva_samasa:
        return 'Dvandva Samasa', dvandva_samasa[word]
    elif word in tatpurusha_samasa:
        return 'Tatpurusha Samasa', tatpurusha_samasa[word]
    elif word in bahuvrihi_samasa:
        return 'Bahuvrihi Samasa', bahuvrihi_samasa[word]
    elif word in dvigu_samasa:
        return 'Dvigu Samasa', dvigu_samasa[word]
    return 'Not a Samasa', []

# Main Program
def main():
    while True:
        word = input("Enter a Kannada word (or type 'exit' to quit): ").strip()
        if word.lower() == 'exit':
            break
        samasa_type, components = identify_samasa_type(word)
        if samasa_type != 'Not a Samasa':
            print(f"'{word}' is a {samasa_type} composed of {components}")
        else:
            print(f"'{word}' is not a compound word")

if __name__ == "__main__":
    main()
