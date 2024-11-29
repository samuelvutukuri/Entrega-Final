from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class GrammarCorrectionWithBart:
    def __init__(self):
        """
        Initialize the grammar correction model with a specialized model for grammatical error correction.
        """
        try:
            self.model_name = "grammarly/coedit-large"  # Specialized grammar correction model
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        except Exception as e:
            print(f"Error loading grammar correction model: {e}")
            # Fallback to a more generic approach
            self.model_name = "t5-base"
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def check_and_correct(self, preprocessed_text):
        """
        Corrects grammatical errors in the input text.
        
        Args:
            preprocessed_text (list): Preprocessed input text
        
        Returns:
            tuple: (list of grammar errors, corrected text)
        """
        try:
            # Convert preprocessed text back to a string
            input_text = " ".join(preprocessed_text)
            
            # Prepare input for the model
            inputs = self.tokenizer(
                f"grammar: {input_text}", 
                return_tensors="pt", 
                max_length=512, 
                truncation=True
            )
            
            # Generate corrected text
            outputs = self.model.generate(
                inputs["input_ids"], 
                max_length=512, 
                num_return_sequences=1,
                num_beams=4,
                early_stopping=True
            )
            
            # Decode the corrected text
            corrected_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Compare original and corrected text to identify errors
            grammar_errors = [f"Original: {input_text}\nCorrected: {corrected_text}"]
            
            return grammar_errors, corrected_text
        
        except Exception as e:
            print(f"Grammar correction error: {e}")
            # Fallback error handling
            return [f"Unable to correct grammar: {e}"], input_text
