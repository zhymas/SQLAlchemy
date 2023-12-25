from pydantic import BaseModel, ValidationError, Field, field_validator
import json


class Tag(BaseModel):
    id: int
    name: str

    @field_validator('name')
    @classmethod
    def name_should_be_first_upper_letter(cls, v: str) -> str:
        if v[0].islower():
            raise ValueError('Work only with first upper letter')
        return v


class User(BaseModel):
    username: str = Field(alias='username_client')
    email: str
    balance: float
    tags: list[Tag]


input_json = {
        'username_client': 'Dima',
        'email': 'shvachko319@gmail.com',
        'balance': '100',
        'tags': [{
            'id': '1', 'name': 'Expert'
        }]
}

json_string = json.dumps(input_json)

try:
    new_user = User.model_validate_json(json_string)
    print(new_user.model_dump_json(by_alias=True, exclude={'balance'}))
except ValidationError as e:
    print(e.json())

# user = User.model_validate_json(json_string)
# print(json_string)
# print(user.username)

# new_user = User(username='Andrey', email='shvachko319@gmail.com', balance=10000)


