C14 Python Wrapper
==================

This module is a python wrapper around the Online.net `C14`_ storage solution.

This module implements every publicly made available by Online.net API calls.

.. _C14: https://www.online.net/en/c14


Usage
-----

.. code-block::

  from c14 import C14

  token = 'thisismyprivatetoken'

  c14api = C14(token)

  # Create a safe
  c14api.create_safe('My Safe', 'This is the description of my safe')

  # List all safes
  c14api.list_safes()


List of available methods
-------------------------

``def list_platforms(self)``: Get a list of links to the platforms.

``def get_platform(self, id)``: Get information on a platform.

- ``id``: ID of the platform.

``def list_protocols(self)`` Get a list of available file transfer protocols.

``def create_safe(self, name, description=None)``: Create a safe.

- ``name``: Name of the safe.
- ``description``: Description of the safe.

``def get_safe(self, uuid)``: Get information on a safe.

- ``uuid``: Id of the safe.

``def update_safe(self, uuid, name=None, description=None)``: Edit a safe.

- ``uuid``: Id of the safe.
- ``name``: Name of the safe.
- ``description``: Description of the safe.

``def list_safes(self)``: Get a list of links to the user's safes."""

``def delete_safe(self, uuid)``: Delete a safe.

- ``uuid``: Id of the safe.

``def create_archive(self, safe_id, name, description, protocols, platforms, parity=None, ssh_keys=None, days=None)``: Create an archive.

- ``safe_id``: Id of the safe.
- ``name``: Name of the archive.
- ``description``: Description of the archive.
- ``protocols``: File transfer protocols used.
- ``platforms``: Ids of platforms where the archive will be stored.
- ``parity``: Parity (standard, or enterprise; default: standard).
- ``ssh_keys``: UUIDs of SSH keys.
- ``days``: Number of days until the files are archived automatically (2, 5, or 7; default: 7).


``def get_archive(self, safe_id, uuid)``: Get information on an Archive.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.

``def update_archive(self, uuid, name=None, description=None)``: Edit an archive.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.
-  ``name``: Name of the archive.
-  ``description``: Description of the archive.

``def list_archives(self, safe_id)``: Get a list of archives in the user's safe.

-  ``safe_id``: Id of the safe.

``def delete_archive(self, safe_id, uuid)``: Delete an archive.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.

``def archive_archive(self, safe_id, uuid)``: Archive files from temporary storage.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.

``def archive_informations(self, safe_id, uuid)``: Get information on an archive's temporary storage.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.

``def archive_list_jobs(self, safe_id, uuid)``: Get list of archive jobs.

-  ``safe_id``: Id of the safe.
-  ``uuid: Id`` of the archive.

``def archive_get_job(self, safe_id, uuid, job_id)``: Get informations of a job.

-  ``safe_id``: Id of the safe.
-  ``uuid: Id`` of the archive.
-  ``job_id``: Id of the job.

``def archive_get_encryption_key(self, safe_id, uuid)``: Get an archive's encryption key.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.

``def archive_set_encryption_key(self, safe_id, uuid, key)``: Set an archive's encryption key.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.
-  ``key``: Encryption key.

``def archive_delete_encryption_key(self, safe_id, uuid)``: Delete an archive's encryption key.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.

``def archive_list_locations(self, safe_id, uuid)``: Get a list of locations on the user's archive.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.

``def archive_get_location(self, safe_id, uuid, location_id)``: Get information on an archive location.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.

``def verify_archive(self, safe_id, uuid, location_id)``: Verify the files on an archive's location.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.
-  ``location_id``: Id of the location.

``def unarchive(self, safe_id, uuid, location_id, protocols, rearchive=None, key=None, ssh_keys=None)``: Unarchive files into temporary storage.

-  ``safe_id``: Id of the safe.
-  ``uuid``: Id of the archive.
-  ``location_id``: Id of the location.
-  ``protocols``: File transfer protocols used.
-  ``rearchive``: Rearchive the data after 7 days (default: true).
-  ``key``: Encryption key.
-  ``ssh_keys``: UUIDs of SSH keys.
