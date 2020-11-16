#!/usr/bin/env python

# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

# [START storage_enforce_public_access_prevention]
from google.cloud import storage
from google.cloud.storage.bucket import PUBLIC_ACCESS_PREVENTION_ENFORCED


def enforce_public_access_prevention(bucket_name):
    """Enforce public access prevention for a bucket."""
    # bucket_name = "my-bucket"

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    bucket.iam_configuration.public_access_prevention = PUBLIC_ACCESS_PREVENTION_ENFORCED
    bucket.patch()

    print(
        "Public access prevention is set to enforced for {}.".format(bucket.name)
    )


# [END storage_enforce_public_access_prevention]

if __name__ == "__main__":
    enforce_public_access_prevention(bucket_name=sys.argv[1])
