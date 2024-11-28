from transformers import BartForConditionalGeneration, BartTokenizer

class GrammarCorrectionWithBart:
    def __init__(self):
        # Load the BART model and tokenizer for text generation
        self.model_name = "facebook/bart-large-mnli"  # You can use any appropriate BART variant
        self.model = BartForConditionalGeneration.from_pretrained(self.model_name)
        self.tokenizer = BartTokenizer.from_pretrained(self.model_name)

    def check_and_correct(self, preprocessed_text):
        """
        Uses the BART model to correct grammar and suggest improvements.
        """
        # Convert the input text to a format suitable for the BART model
        input_text = "grammar correction: " + " ".join(preprocessed_text)
        
        # Tokenize and generate the corrected output
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        summary_ids = self.model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
        
        # Decode the generated output
        corrected_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        # Return the original and corrected text for feedback
        grammar_errors = [f"Original: {' '.join(preprocessed_text)}\nSuggested: {corrected_text}"]
        
        return grammar_errors, corrected_text
