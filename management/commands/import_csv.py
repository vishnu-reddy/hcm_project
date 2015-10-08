import csv
import os
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from cornerstone.models import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True


class Command(BaseCommand):
    args = BASE_DIR  + "/data/CSOD_Users.csv"
    help = 'Imports from local csv file'

    def handle(self, *args, **options):
        if args:
            file_path = args[0]
        else:
            raise CommandError('provide a path for csv')

        # Renamed "file" variable to "f" as "file" is a Python builtin and
        #   should not be used as a variable name
        with open(file_path) as f:
            rows = csv.reader(f)

            # Skip the header row here
            rows.next()

            for row in rows:
                # Retrieve each row's value as a variable.
                guid = row[0].strip()
                user_id = row[1].strip()
                first_name = row[2].strip()
                last_name = row[3].strip()

                if not all([guid, user_id, first_name, last_name]):
                    continue

                # Print out the results.
                print "guid:        " + guid
                print "user_id:     " + user_id
                print "first_name:  " + first_name
                print "last_name:   " + last_name


                #   updated. You will need to read Django's documentation to
                #   understand this fully.
                CornerstoneUserProfile.objects.update_or_create(
                    guid=guid,
                    user_id=user_id,
                    defaults={
                        'first_name': first_name,
                        'last_name': last_name,
                    }
                )

            # Seek back to the beginning of the file
            f.seek(0)

            # Re-initialize the CSV reader
            rows = csv.reader(f)

            # Skip the header row here instead
            rows.next()

            # Loop through each row and add the parent if it exists
            for row in rows:

                # Retrieve each row's value as a variable.
                guid = row[0].strip()
                user_id = row[1].strip()
                first_name = row[2].strip()
                last_name = row[3].strip()
                manager_user_id = row[4].strip()


                if not all([guid, user_id, first_name, last_name]):
                    continue

                try:
                    user = CornerstoneUserProfile.objects.get(user_id=user_id)

                    # We will only attempt to retrieve the parent if the
                    #   manager's user id was provided for this row.
                    if manager_user_id:
                        parent = CornerstoneUserProfile.objects.get(
                            user_id=manager_user_id
                        )
                    else:
                        parent = None
                except CornerstoneUserProfile.DoesNotExist:
                    continue

                user.parent = parent
                user.save()