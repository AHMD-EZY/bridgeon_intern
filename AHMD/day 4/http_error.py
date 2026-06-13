class HTTPError(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        super().__init__(f"error{status_code}")
def get_404(collection:dict,id:int)->dict:
    if id in collection:
        return collection[id]
    raise HTTPError(404)
users={1:{"name":"Ahmd"},2:{"name":"Aberr"},3:{"name":"Shyaaam"}}
print("valid")
try:
    user=get_404(users,2)
    print("Found:", user)
except  HTTPError as e:
    print (e)
print("invalid error")
print("\n invalid test")
try:
    user=get_404(users,10)
    print("found:",user)
except HTTPError as e:
    print(e)