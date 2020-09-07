import json


class Cat:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f"name is {self.name} and breed is {self.breed} "


c = Cat("Charles", "Tabby")

# json.dumps returns a JSON STRING:

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
# results in '["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(j)

j = json.dumps(c.__dict__)
# results in '{"name": "Charles", "breed": "Tabby"}'
print(j)
