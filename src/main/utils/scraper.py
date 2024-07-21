

def split_text_into_chunks(text, chunk_size):
    # Split the text into a list of words
    words = text.split().replace("  ", "").replace("\n", " ")
    
    # Create chunks of the specified size
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    
    return chunks