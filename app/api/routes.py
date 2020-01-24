from app.api.api import RatesApi


def add_resources(api):
    api.add_resource(RatesApi, '/rates/<date:date>')
    print('Resources: {}'.format(api.resources))
    return api
