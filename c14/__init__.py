# Copyright 2016 Yanis Guenane <yanis@guenane.org>
# Author: Yanis Guenane <yanis@guenane.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import requests
import slumber

API_URL = 'https://api.online.net/api/v1'


class C14(object):
    """This module is a wrapper around the Online.net `C14`_ storage solution.

       This module implements every publicly made available by Online.net API
       calls.

       .. _C14: https://www.online.net/en/c14
    """

    def __init__(self, token):
        api_session = requests.session()
        api_session.headers['Authorization'] = 'Bearer %s' % token
        api_session.headers['User-Agent'] = 'c14 python wrapper'
        self.api = slumber.API(API_URL,
                               session=api_session, append_slash=False)

    def handle_error(self, exception):
        content = json.loads(exception.response._content)
        return {'error': content['error'],
                'code': content['code'],
                'status_code': exception.response.status_code,
                'url': exception.response.url}

    def list_platforms(self):
        """Get a list of links to the platforms."""

        try:
            res = self.api.storage.c14.platform.get()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def get_platform(self, id):
        """Get information on a platform.

        :param id: ID of the platform.
        """

        try:
            res = self.api.storage.c14.platform(id).get()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def list_protocols(self):
        """Get a list of available file transfer protocols."""

        try:
            res = self.api.storage.c14.protocol.get()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def create_safe(self, name, description=None):
        """Create a safe.

        :param name: Name of the safe.
        :param description: Description of the safe.
        """

        try:
            res = self.api.storage.c14.safe.post({'name': name,
                                                  'description': description})
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def get_safe(self, uuid):
        """Get information on a safe.

        :param uuid: Id of the safe.
        """

        try:
            res = self.api.storage.c14.safe(uuid).get()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def update_safe(self, uuid, name=None, description=None):
        """Edit a safe.

        :param uuid: Id of the safe.
        :param name: Name of the safe.
        :param description: Description of the safe.
        """

        data = {'name': name,
                'description': description}

        data = dict((k, v) for k, v in data.iteritems() if v is not None)
        try:
            res = (self.api.storage.c14.safe(uuid).patch(data))
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def list_safes(self):
        """Get a list of links to the user's safes."""

        try:
            res = self.api.storage.c14.safe.get()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def delete_safe(self, uuid):
        """Delete a safe.

        :param uuid: Id of the safe.
        """

        try:
            res = self.api.storage.c14.safe(uuid).delete()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def create_archive(self, safe_id, name, description, protocols, platforms,
                       parity=None, ssh_keys=None, days=None):
        """Create an archive.

        :param safe_id: Id of the safe.
        :param name: Name of the archive.
        :param description: Description of the archive.
        :param protocols: File transfer protocols used.
        :param platforms: Ids of platforms where the archive will be stored.
        :param parity: Parity (standard, or enterprise; default: standard).
        :param ssh_keys: UUIDs of SSH keys.
        :param days: Number of days until the files are archived automatically
                     (2, 5, or 7; default: 7).
        """

        try:
            data = {'name': name,
                    'description': description,
                    'parity': parity,
                    'protocols': protocols,
                    'ssh_keys': ssh_keys,
                    'days': days,
                    'platforms': platforms}

            data = dict((k, v) for k, v in data.iteritems() if v is not None)
            res = self.api.storage.c14.safe(safe_id).archive.post(data)
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def get_archive(self, safe_id, uuid):
        """Get information on an Archive.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        """

        try:
            res = self.api.storage.c14.safe(safe_id).archive(uuid).get()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def update_archive(self, safe_id, uuid, name=None, description=None):
        """Edit an archive.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        :param name: Name of the archive.
        :param description: Description of the archive.
        """

        data = {'name': name,
                'description': description}

        data = dict((k, v) for k, v in data.iteritems() if v is not None)
        try:
            res = (self.api.storage.c14.safe(safe_id).archive(uuid)
                   .patch(data))
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def list_archives(self, safe_id):
        """Get a list of archives in the user's safe.

        :param safe_id: Id of the safe.
        """

        try:
            res = self.api.storage.c14.safe(safe_id).archive.get()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def delete_archive(self, safe_id, uuid):
        """Delete an archive.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        """

        try:
            res = self.api.storage.c14.safe(safe_id).archive(uuid).delete()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def archive_archive(self, safe_id, uuid):
        """Archive files from temporary storage.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        """

        try:
            res = (self.api.storage.c14.safe(safe_id).archive(uuid).archive
                   .post())
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def archive_informations(self, safe_id, uuid):
        """Get information on an archive's temporary storage.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        """

        try:
            res = (self.api.storage.c14.safe(safe_id).archive(uuid).bucket
                   .get())
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def archive_list_jobs(self, safe_id, uuid):
        """Get list of archive jobs.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        """

        try:
            res = self.api.storage.c14.safe(safe_id).archive(uuid).job.get()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def archive_get_job(self, safe_id, uuid, job_id):
        """Get informations of a job.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        :param job_id: Id of the job.
        """

        try:
            res = (self.api.storage.c14.safe(safe_id).archive(uuid)
                   .job(job_id).get())
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def archive_get_encryption_key(self, safe_id, uuid):
        """Get an archive's encryption key.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        """

        try:
            res = self.api.storage.c14.safe(safe_id).archive(uuid).key.get()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def archive_set_encryption_key(self, safe_id, uuid, key):
        """Set an archive's encryption key.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        :param key: Encryption key.
        """

        try:
            data = {'key': key}
            res = (self.api.storage.c14.safe(safe_id).archive(uuid).key
                   .post(data))
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def archive_delete_encryption_key(self, safe_id, uuid):
        """Delete an archive's encryption key.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        """

        try:
            res = self.api.storage.c14.safe(safe_id).archive(uuid).key.delete()
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def archive_list_locations(self, safe_id, uuid):
        """Get a list of locations on the user's archive.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        """

        try:
            res = (self.api.storage.c14.safe(safe_id).archive(uuid).location
                   .get())
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def archive_get_location(self, safe_id, uuid, location_id):
        """Get information on an archive location.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        """

        try:
            res = (self.api.storage.c14.safe(safe_id).archive(uuid)
                   .location(location_id).get())
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def verify_archive(self, safe_id, uuid, location_id):
        """Verify the files on an archive's location.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        :param location_id: Id of the location.
        """

        try:
            res = (self.api.storage.c14.safe(safe_id).archive(uuid)
                   .location(location_id).verify.post())
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res

    def unarchive(self, safe_id, uuid, location_id, protocols, rearchive=None,
                  key=None, ssh_keys=None):
        """Unarchive files into temporary storage.

        :param safe_id: Id of the safe.
        :param uuid: Id of the archive.
        :param location_id: Id of the location.
        :param protocols: File transfer protocols used.
        :param rearchive: Rearchive the data after 7 days (default: true).
        :param key: Encryption key.
        :param ssh_keys: UUIDs of SSH keys.
        """

        try:
            data = {'location_id': location_id,
                    'protocols': protocols,
                    'rearchive': rearchive,
                    'key': key,
                    'ssh_keys': ssh_keys}

            data = dict((k, v) for k, v in data.iteritems() if v is not None)
            res = (self.api.storage.c14.safe(safe_id).archive(uuid).unarchive
                   .post(data))
        except slumber.exceptions.HttpClientError as e:
            res = self.handle_error(e)
        except slumber.exceptions.HttpServerError as e:
            res = self.handle_error(e)

        return res
