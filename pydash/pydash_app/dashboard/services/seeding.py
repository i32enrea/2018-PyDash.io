"""
Fills the application with some preliminary dashboards
to make it easier to test code in development and staging environments.
"""


from pydash_app.dashboard.entity import Dashboard
import pydash_app.dashboard.repository as repository
import pydash_app.user.repository as user_repository

import pydash_app.dashboard.services.fetching as fetching


def seed():
    """
    For each user, stores some preliminary debug dashboards in the datastore,
    to be used during development.
    Note: For now it only generates a dashboard for the user named "Arjan", to speed up seeding.
    """

    repository.clear_all()

    # for user in user_repository.all():
    for user in [user_repository.find_by_name("Arjan")]:
        dashboard_new = Dashboard('http://flask-sample.koenbolhuis.nl/dashboard',
                                  'cc83733cb0af8b884ff6577086b87909',
                                  user.get_id(),
                                  'Testing Dashboard (FMD v1.12.0+)',
                                  True)
        dashboard_old = Dashboard('http://flask-sample-old.koenbolhuis.nl/dashboard',
                                  'cc83733cb0af8b884ff6577086b87909',
                                  user.get_id(),
                                  'Unsupported Dashboard (FMD v1.11.5)')
        pydash = Dashboard('http://localhost:5000/api/fmd',
                                  'cc83733cb0af8b884ff6577086b87909',
                                  user.get_id(),
                                  'PyDash Meta')
        for dashboard in [dashboard_new, dashboard_old, pydash]:
            print(f'Adding dashboard {dashboard}')
            repository.add(dashboard)
            print(f'Fetching remote info for dashboard {dashboard}.')
            fetching.fetch_and_update_historic_dashboard_info(dashboard.id)

    print('Seeding of dashboards is done!')
