from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the template for the parsing instructions
template = (
    "You are tasked with extracting specific real estate information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract real estate information that directly matches the provided description: {parse_description}. "
    "2. **Categories:** Organize the extracted information into categories such as Price, Address, Bedrooms, Bathrooms, etc. "
    "3. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "4. **Empty Response:** If no information matches the description, return an empty string ('')."
    "5. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)


# Initialize the language model with the specified model type
model = OllamaLLM(model="llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
    # Create a chat prompt using the template
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    # Iterate through each chunk of the DOM content
    for i, chunk in enumerate(dom_chunks, start=1):
        # Invoke the model to parse the chunk based on the user's description
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})

        # Log the progress of parsing
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    # Combine all parsed results into a single string
    return "\n".join(parsed_results)
