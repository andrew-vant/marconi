# Copyright (c) 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from marconi import storage


class Driver(storage.DriverBase):
    @property
    def queue_controller(self):
        return QueueController(self)

    @property
    def message_controller(self):
        return MessageController(self)

    @property
    def claim_controller(self):
        return None


class QueueController(storage.QueueBase):
    def __init__(self, driver):
        pass

    def list(self, project=None):
        raise NotImplementedError()

    def get(self, name, project=None):
        raise NotImplementedError()

    def create(self, name, project=None):
        raise NotImplementedError()

    def set_metadata(self, name, metadata, project=None):
        raise NotImplementedError()

    def delete(self, name, project=None):
        raise NotImplementedError()

    def stats(self, name, project=None):
        raise NotImplementedError()

    def actions(self, name, project=None, marker=None, limit=10):
        raise NotImplementedError()


class MessageController(storage.MessageBase):
    def __init__(self, driver):
        pass

    def get(self, queue, project=None, message_ids=None,
            marker=None, echo=False, client_uuid=None):
        raise NotImplementedError()

    def list(self, queue, project=None, marker=None,
             limit=10, echo=False, client_uuid=None):
        raise NotImplementedError()

    def post(self, queue, messages, project=None):
        raise NotImplementedError()

    def delete(self, queue, message_id, project=None, claim=None):
        raise NotImplementedError()
