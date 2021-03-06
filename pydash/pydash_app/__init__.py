"""
The `pydash_app` package contains all business domain logic of the PyDash application: Everything that is not part of rendering a set of webpages.
"""

import periodic_tasks

import pydash_app.user
import pydash_app.user.services.pruning
import pydash_app.user.services.seeding

import pydash_app.dashboard.services.fetching
import pydash_app.dashboard.services.seeding
import pydash_app.dashboard.services.pinging
import pydash_app.dashboard


def start_task_scheduler():
    """Starts the default task scheduler, which is declared in pydash.periodic_tasks."""
    periodic_tasks.default_task_scheduler.start()


def stop_task_scheduler():
    """Stops the default task scheduler, which is declared in pydash.periodic_tasks."""
    periodic_tasks.default_task_scheduler.stop()


def schedule_periodic_tasks():
    """Schedules all periodic tasks using the default task scheduler, which is declared in pydash.periodic_tasks."""
    import datetime  # <- remove this line when custom interval no longer necessary for testing.

    pydash_app.dashboard.services.fetching.schedule_all_periodic_dashboards_tasks(
        interval=datetime.timedelta(minutes=1)
    )

    # pydash_app.dashboard.services.pinging.schedule_all_periodic_dashboard_pinging(
    #     interval=datetime.timedelta(seconds=15)
    # )

    pydash_app.user.services.pruning.schedule_periodic_pruning_task()


def seed_datastructures():
    """Seeds user and dashboard repositories with preliminary values for testing in development and staging environments."""
    # Ensure no periodic tasks with old datastructures are run:
    stop_task_scheduler()

    user.services.seeding.seed()
    dashboard.services.seeding.seed()
