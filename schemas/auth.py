from pydantic import BaseModel

class Auth(BaseModel):
  user_name:str
  pass_word:str