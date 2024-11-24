from ollama import generate
from ollama import GenerateResponse

prefix = '''import datetime
def calculate_age(birth_year):
    """Calculates a person's age based on their birth year."""
    current_year = datetime.date.today().year'''

suffix = '''return age'''

genResponse: GenerateResponse = generate(
  model='codegemma:2b-code',
  prompt=f'<|fim_prefix|>{prefix}<|fim_suffix|>{suffix}<|fim_middle|>',
  options={
    'num_predict': 128,
    'temperature': 0,
    'top_p': 0.9,
    'stop': ['<|file_separator|>'],
  },
)

print(genResponse.response)
