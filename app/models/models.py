class Info:
    """
        Represents more of the metadata associated with the API
        output
    """
    def __init__(self, **kwargs):
        self.seed = kwargs['seed']
        self.results = kwargs['results']  # will represent an integer (500 in this case)
        self.page = kwargs['page']
        self.version = kwargs['version']


class User:
    """
        Represents a top level result entry from the API output
    """
    def __init__(self, **kwargs):
        self.gender = kwargs['gender']
        self.name = kwargs['name']
        self.location = kwargs['email']
        self.email = kwargs['email']
        self.login = kwargs['gender']
        self.dob = kwargs['dob']
        self.registered = kwargs['registered']
        self.phone = kwargs['phone']
        self.cell = kwargs['cell']
        self.id = kwargs['id']
        self.picture = kwargs['picture']
        self.nat = kwargs['nat']


class Name:
    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.first = kwargs['first']
        self.last = kwargs['last']


class Location:
    def __init__(self, **kwargs):
        self.street = kwargs['street']
        self.city = kwargs['city']
        self.state = kwargs['state']
        self.country = kwargs['country']
        self.postcode = kwargs['postcode']
        self.coordinates = kwargs['coordinates']
        self.timezone = kwargs['coordinates']


class Street:
    def __init__(self, **kwargs):
        self.number = kwargs['number']
        self.name = kwargs['name']


class Coordinates:
    def __init__(self, **kwargs):
        self.latitude = kwargs['latitude']
        self.longitude = kwargs['longitude']


class Timezone:
    def __init__(self, **kwargs):
        self.offset = kwargs['offset']
        self.description = kwargs['description']


class Login:
    def __init__(self, **kwargs):
        self.uuid = kwargs['uuid']
        self.username = kwargs['username']
        self.password = kwargs['password']
        self.salt = kwargs['salt']
        self.md5 = kwargs['md5']
        self.sha1 = kwargs['sha1']
        self.sha256 = kwargs['sha256']


class Dob:
    def __init__(self, **kwargs):
        self.date = kwargs['date']
        self.age = kwargs['age']


class Registered:
    def __init__(self, **kwargs):
        self.date = kwargs['date']
        self.age = kwargs['age']


class Id:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.value = kwargs['value']


class Picture:
    def __init__(self, **kwargs):
        self.large = kwargs['large']
        self.medium = kwargs['medium']
        self.thumbnail = kwargs['thumbnail']
