#!/usr/bin/env python3
"""
   Copyright 2022 NetApp, Inc

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import yaml
import json

from .common import SDKCommon


class getEntitlements(SDKCommon):
    """Get the Astra Control entitlements, which can be used to determine if it's
    an Astra Control Service or Center environment."""

    def __init__(self, quiet=True, verbose=False, output="json"):
        """quiet: Will there be CLI output or just return (datastructure)
        verbose: Print all of the ReST call info: URL, Method, Headers, Request Body
        output: table: pretty print the data
                json: (default) output in JSON
                yaml: output in yaml"""
        self.quiet = quiet
        self.verbose = verbose
        self.output = output
        super().__init__()

    def main(self):
        endpoint = "core/v1/entitlements"
        url = self.base + endpoint

        data = {}
        params = {}

        ret = super().apicall(
            "get",
            url,
            data,
            self.headers,
            params,
            self.verifySSL,
            quiet=self.quiet,
            verbose=self.verbose,
        )

        if ret.ok:
            entitlements = super().jsonifyResults(ret)
            if self.output == "json":
                dataReturn = entitlements
            elif self.output == "yaml":
                dataReturn = yaml.dump(entitlements)
            elif self.output == "table":
                dataReturn = self.basicTable(
                    ["entitlementID", "product", "type", "value", "consumption"],
                    [
                        "id",
                        "product",
                        "entitlementType",
                        "entitlementValue",
                        "entitlementConsumption",
                    ],
                    entitlements,
                )
            if not self.quiet:
                print(json.dumps(dataReturn) if type(dataReturn) is dict else dataReturn)
            return dataReturn

        else:
            if not self.quiet:
                super().printError(ret)
            return False
